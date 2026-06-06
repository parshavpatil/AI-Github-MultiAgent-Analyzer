import os
import requests


def extract_repo(repo_url: str):
    """
    Converts:

    https://github.com/langchain-ai/langgraph

    into:

    owner = langchain-ai
    repo = langgraph
    """

    repo_url = repo_url.strip("/")

    parts = repo_url.split("/")

    if len(parts) < 5:
        raise ValueError(
            "Invalid GitHub repository URL"
        )

    owner = parts[-2]
    repo = parts[-1]

    return owner, repo


def get_headers():

    token = os.getenv("GITHUB_TOKEN")

    headers = {
        "Accept": "application/vnd.github+json"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers


def get_repo_data(repo_url):

    owner, repo = extract_repo(repo_url)

    api_url = (
        f"https://api.github.com/repos/{owner}/{repo}"
    )

    response = requests.get(
        api_url,
        headers=get_headers(),
        timeout=30
    )

    if response.status_code == 404:
        raise Exception(
            "Repository not found"
        )

    if response.status_code != 200:
        raise Exception(
            f"GitHub API Error: {response.status_code}"
        )

    return response.json()


def get_readme(repo_url):

    owner, repo = extract_repo(repo_url)

    branches = [
        "main",
        "master"
    ]

    for branch in branches:

        readme_url = (
            f"https://raw.githubusercontent.com/"
            f"{owner}/{repo}/{branch}/README.md"
        )

        response = requests.get(
            readme_url,
            timeout=30
        )

        if response.status_code == 200:

            return response.text[:5000]

    return "README not found."


def get_languages(repo_url):

    owner, repo = extract_repo(repo_url)

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/languages"
    )

    response = requests.get(
        url,
        headers=get_headers(),
        timeout=30
    )

    if response.status_code != 200:
        return {}

    return response.json()


def get_contributors(repo_url):

    owner, repo = extract_repo(repo_url)

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/contributors"
    )

    response = requests.get(
        url,
        headers=get_headers(),
        timeout=30
    )

    if response.status_code != 200:
        return []

    data = response.json()

    return data[:10]


def get_repository_context(repo_url):

    repo_data = get_repo_data(repo_url)

    languages = get_languages(repo_url)

    readme = get_readme(repo_url)

    return {
        "name": repo_data.get("name"),
        "full_name": repo_data.get("full_name"),
        "description": repo_data.get("description"),
        "stars": repo_data.get("stargazers_count"),
        "forks": repo_data.get("forks_count"),
        "watchers": repo_data.get("watchers_count"),
        "open_issues": repo_data.get("open_issues_count"),
        "language": repo_data.get("language"),
        "topics": repo_data.get("topics", []),
        "languages": languages,
        "readme": readme,
    }

def extract_repo(repo_url: str):
    repo_url = repo_url.strip("/")
    parts = repo_url.split("/")

    owner = parts[-2]
    repo = parts[-1]

    return owner, repo
