from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
from crewai import Agent, Task, Crew, Process

from agents import doctor, verifier, nutritionist, exercise_specialist
from task import help_patients

# ✅ NEW: DB integration
from db import SessionLocal
from models import ReportResult

app = FastAPI(title="Blood Test Report Analyser")

# Crew execution logic
def run_crew(query: str, file_path: str = "data/sample.pdf"):
    medical_crew = Crew(
        agents=[doctor, verifier, nutritionist, exercise_specialist],
        tasks=[help_patients],
        process=Process.sequential,
    )
    result = medical_crew.kickoff(inputs={"query": query, "file_path": file_path})
    return result

@app.get("/")
async def root():
    return {"message": "Blood Test Report Analyser API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        if not query.strip():
            query = "Summarise my Blood Test Report"

        try:
            response = run_crew(query=query.strip(), file_path=file_path)
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"LLM or agent error: {str(e)}")

        # ✅ SAVE TO DATABASE
        db = SessionLocal()
        new_entry = ReportResult(
            query=query,
            result=str(response),
            filename=file.filename
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        db.close()

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing blood report: {str(e)}")

    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
