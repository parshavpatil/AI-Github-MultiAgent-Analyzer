from typing import TypedDict


class RepoState(TypedDict):
    repo_url: str

    metadata_output: str
    tech_output: str
    readme_output: str
    reviewer_output: str
    interview_output: str

    final_report: str