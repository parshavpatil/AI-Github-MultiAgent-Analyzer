---

title: AI Github Intelligence System
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.46.1
app_file: app.py
pinned: false
-------------

# 🚀 AI GitHub Intelligence System

A Multi-Agent AI System that analyzes GitHub repositories and generates professional intelligence reports using LangGraph, LangChain, Gemini, and the GitHub REST API.


## ✨ Features

### 🤖 Multi-Agent Architecture

The application uses specialized AI agents:

* Metadata Agent
* Technology Analysis Agent
* README Analysis Agent
* Project Reviewer Agent
* Interview Preparation Agent
* Report Generation Agent

---

### 📊 Repository Intelligence

Automatically extracts:

* Repository Name
* Description
* Stars
* Forks
* Topics
* Programming Languages
* Open Issues

---

### 🧠 AI-Powered Analysis

Generates:

* Project Summary
* Technology Stack Analysis
* Use Cases
* Difficulty Assessment
* Improvement Suggestions
* Learning Roadmap
* Interview Questions

---

### 📄 Professional PDF Reports

Download a complete intelligence report containing:

* Repository Overview
* Technology Analysis
* Project Review
* Interview Preparation Material
* Recommendations

---

## 🏗️ System Architecture

```text
User Input
     │
     ▼
GitHub Repository URL
     │
     ▼
LangGraph Workflow
     │
     ├── Metadata Agent
     ├── Technology Agent
     ├── README Agent
     ├── Reviewer Agent
     ├── Interview Agent
     │
     ▼
Report Generator Agent
     │
     ▼
Streamlit UI
     │
     ▼
PDF Report
```

---

## 🛠️ Tech Stack

### AI & Agents

* LangGraph
* LangChain
* Google Gemini 2.5 Flash

### Backend

* Python
* GitHub REST API
* Requests

### Frontend

* Streamlit

### Reporting

* ReportLab

---

## 📂 Project Structure

```text
AI-GitHub-Intelligence-System/

│
├── app.py
├── analyzer.py
├── agents.py
├── graph.py
├── state.py
├── github_tools.py
├── pdf_generator.py
│
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-GitHub-Intelligence-System.git

cd AI-GitHub-Intelligence-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

GITHUB_TOKEN=YOUR_GITHUB_TOKEN
```

### Get Google API Key

Google AI Studio:
https://aistudio.google.com/app/apikey

### Get GitHub Token

GitHub Settings → Developer Settings → Personal Access Tokens

---

## ▶️ Run Locally

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📸 Example Input

```text
https://github.com/langchain-ai/langgraph
```

---

## 📄 Example Output

* Repository Overview
* Technology Stack
* Difficulty Level
* Interview Questions
* Learning Roadmap
* Recommendations
* Downloadable PDF Report

---




