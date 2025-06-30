# blood-test-analyser-debug

This project is an AI-powered system designed to analyze blood test reports. It uses FastAPI for the backend, CrewAI for managing specialized agents (doctor, verifier, nutritionist, and exercise specialist), and SQLite for storing analysis results. Users can upload PDF reports and receive detailed, human-like analysis, recommendations, and summaries.

**Features**
Upload a PDF blood report and receive detailed AI-generated analysis
CrewAI agents simulate expert reasoning from multiple roles (doctor, verifier, nutritionist, etc.)
SQLite database stores all queries and results
Clean API documentation at /docs (powered by FastAPI Swagger)
Modular architecture with clearly separated agents, tasks, tools, and database layers

**Bugs Identified & Fixes**
1.CrewAI Tool Integration Issue
Bug: Tools used in agents were not compatible with CrewAI v0.30+ structure.
Fix: Refactored tools using proper Tool structure from Langchain and connected to CrewAI via tools=[tool_instance].

2.PDF Parsing Error
Bug: Old versions of Langchain used deprecated PDF loaders.
Fix: Replaced PyPDFLoader with updated import:
from langchain_community.document_loaders import PyPDFLoader.

3.Environment Variables
Bug: Missing OpenAI API key handling.
Fix: Environment variable check using os.getenv("OPENAI_API_KEY").

4.Circular Import in Celery
Bug: Importing run_crew from main.py inside Celery task caused circular import.
Fix: Moved run_crew function to crew_runner.py to decouple main app from logic.

5.Database Not Storing Results
Bug: No DB layer for storing results.
Fix: Added SQLAlchemy models and DB session to log each analysis.

6.Several bugs were discovered and fixed during development. One critical bug was using an uninitialized LLM variable with the line llm = llm, which caused a NameError. This was fixed by properly initializing the LLM using the ChatOpenAI class. Another issue was using tool instead of tools when assigning tools to agents. This was corrected to comply with CrewAI's expected schema.
Other minor issues included missing memory flags for agents, incorrect import usage, and poor formatting of tool functions. Agents were improved by making sure their tool methods were instantiated properly and not accessed as class attributes. Additionally, imports were cleaned up and modularization was done for better file organization

**Technologies Used**
1.FastAPI
2.CrewAI
3.Langchain
4.OpenAI GPT (via langchain_openai)
5.SQLite3 with SQLAlchemy ORM
6.Uvicorn
7.Pydantic
8.Python 3.10

**Setup Instructions**
1.Clone the repository
git clone https://github.com/SurajPadalkar17/blood-test-analyser-debug
2.cd blood-test-analyzer
3.Create a virtual environment and activate
4.python -m venv venv
5.venv\Scripts\activate  # For Windows
6.Install dependencies
7.pip install -r requirements.txt
8.Set environment variable
9.set OPENAI_API_KEY=your_openai_key_here 
10.Run the FastAPI server
11.uvicorn main:app --reload
12.Access the API
13.Go to: http://localhost:8000/docs
14.Upload a PDF and query using the /analyze endpoint

**Project Structure**
The codebase is divided into several key modules. The agents are defined in agents.py and include the Doctor, Verifier, Nutritionist, and Exercise Specialist. The tools used by these agents are defined in tools.py. The task definitions used by the CrewAI system are in task.py. Database setup is handled in db.py and models.py, and the main application logic is in main.py.
