import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from github_tools import get_repo_data, get_readme


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def metadata_agent(state):

    repo = get_repo_data(state["repo_url"])

    result = f"""
Repository Name: {repo['name']}

Stars: {repo['stargazers_count']}

Forks: {repo['forks_count']}

Description:
{repo['description']}
"""

    return {
        "metadata_output": result
    }


def tech_stack_agent(state):

    readme = get_readme(state["repo_url"])

    prompt = f"""
Analyze this repository.

Return only:

## Technologies Used
- Languages
- Frameworks
- Libraries

Maximum 150 words.

README:

{readme}
"""

    response = llm.invoke(prompt)

    return {
        "tech_output": response.content
    }


def readme_agent(state):

    readme = get_readme(state["repo_url"])

    prompt = f"""
Create a concise repository summary.

Maximum 100 words.

README:

{readme}
"""

    response = llm.invoke(prompt)

    return {
        "readme_output": response.content
    }


def reviewer_agent(state):

    readme = get_readme(state["repo_url"])

    prompt = f"""
Analyze this project.

Return:

- Difficulty Level
- 3 Use Cases
- 2 Improvement Suggestions

Maximum 150 words.

README:

{readme}
"""

    response = llm.invoke(prompt)

    return {
        "reviewer_output": response.content
    }


def interview_agent(state):

    readme = get_readme(state["repo_url"])

    prompt = f"""
Generate:

- Top 5 Interview Questions
- Key Concepts
- Learning Roadmap

Maximum 200 words.

README:

{readme}
"""

    response = llm.invoke(prompt)

    return {
        "interview_output": response.content
    }


def report_agent(state):

    prompt = f"""
Create a professional repository report.

Format:

# Repository Analysis

## Overview
(50 words)

## Repository Statistics

## Technologies Used
(max 8 bullet points)

## Key Features
(max 5 bullet points)

## Suitable Use Cases
(max 5 bullet points)

## Difficulty Level

## Top Interview Questions
(max 5)

## Recommendation
(max 50 words)

Keep entire report under 700 words.

Metadata:
{state["metadata_output"]}

Technology:
{state["tech_output"]}

README:
{state["readme_output"]}

Review:
{state["reviewer_output"]}

Interview:
{state["interview_output"]}

Make it human readable.
"""

    response = llm.invoke(prompt)

    return {
        "final_report": response.content
    }