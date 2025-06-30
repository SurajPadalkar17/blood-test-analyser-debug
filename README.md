# Project Setup and Execution Guide

This project is an AI-powered system designed to analyze blood test reports. It uses FastAPI for the backend, CrewAI for managing specialized agents (doctor, verifier, nutritionist, and exercise specialist), and SQLite for storing analysis results. Users can upload PDF reports and receive detailed, human-like analysis, recommendations, and summaries.

Features
Upload a PDF blood report and receive detailed AI-generated analysis
CrewAI agents simulate expert reasoning from multiple roles (doctor, verifier, nutritionist, etc.)
SQLite database stores all queries and results
Clean API documentation at /docs (powered by FastAPI Swagger)
Modular architecture with clearly separated agents, tasks, tools, and database layers

# Bugs Identified & Fixes

**1.**CrewAI Tool Integration Issue
Bug: Tools used in agents were not compatible with CrewAI v0.30+ structure.
Fix: Refactored tools using proper Tool structure from Langchain and connected to CrewAI via tools=[tool_instance].

**2.**PDF Parsing Error
Bug: Old versions of Langchain used deprecated PDF loaders.
Fix: Replaced PyPDFLoader with updated import:
from langchain_community.document_loaders import PyPDFLoader.

**3.**Environment Variables
Bug: Missing OpenAI API key handling
Fix: Environment variable check using os.getenv("OPENAI_API_KEY").

**4.**Circular Import in Celery
Bug: Importing run_crew from main.py inside Celery task caused circular import.
Fix: Moved run_crew function to crew_runner.py to decouple main app from logic.

**5.**Database Not Storing Results
Bug: No DB layer for storing results.
Fix: Added SQLAlchemy models and DB session to log each analysis.

**6.**Other minor issues included missing memory flags for agents, incorrect import usage, and poor formatting of tool functions. Agents were improved by making sure their tool methods were instantiated properly and not accessed as class attributes. Additionally, imports were cleaned up and modularization was done for better file organization.

# Technologies Used
**1.**FastAPI
**2.**CrewAI
**3.**Langchain
**4.**OpenAI GPT (via langchain_openai)
**5.**SQLite3 with SQLAlchemy ORM
**6.**Uvicorn
**7.**Pydantic
**8.**Python 3.10

## Getting Started

### Create a virtual environment and activate
```sh
python -m venv venv
venv\Scripts\activate  # For Windows
```
### Install dependencies
```sh
pip install -r requirement.txt
```
### Set environment variable
```sh
set OPENAI_API_KEY=your_openai_key_here 
```
### Run the FastAPI server
```sh
uvicorn main:app --reload
```


### Project Structure
The codebase is divided into several key modules. The agents are defined in agents.py and include the Doctor, Verifier, Nutritionist, and Exercise Specialist. The tools used by these agents are defined in tools.py. The task definitions used by the CrewAI system are in task.py. Database setup is handled in db.py and models.py, and the main application logic is in main.py.

