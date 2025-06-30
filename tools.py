import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
# ✅ correct
from crewai.tools.base_tool import BaseTool  # ✅ This now works
from typing import Optional

class BloodReportReaderTool(BaseTool):
    name: str = "Read Blood Report PDF"
    description: str = "Reads a blood test report from a PDF file path and returns the text."

    def _run(self, path: Optional[str] = "data/sample.pdf") -> str:
        docs = PyPDFLoader(file_path=path).load()
        return "\n".join(doc.page_content.strip() for doc in docs)

# ✅ This is your working tool instance
blood_report_reader_tool = BloodReportReaderTool()

# Optional placeholders
class NutritionTool:
    async def analyze_nutrition_tool(self, blood_report_data):
        return "Nutrition analysis functionality to be implemented"

class ExerciseTool:
    async def create_exercise_plan_tool(self, blood_report_data):
        return "Exercise planning functionality to be implemented"
