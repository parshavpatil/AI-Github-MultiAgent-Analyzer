from langgraph.graph import StateGraph
from state import RepoState

from agents import (
    metadata_agent,
    tech_stack_agent,
    readme_agent,
    reviewer_agent,
    interview_agent,
    report_agent
)

builder = StateGraph(RepoState)

builder.add_node(
    "metadata",
    metadata_agent
)

builder.add_node(
    "tech",
    tech_stack_agent
)

builder.add_node(
    "readme",
    readme_agent
)

builder.add_node(
    "reviewer",
    reviewer_agent
)

builder.add_node(
    "interview",
    interview_agent
)

builder.add_node(
    "report",
    report_agent
)

builder.set_entry_point("metadata")

builder.add_edge("metadata", "tech")
builder.add_edge("tech", "readme")
builder.add_edge("readme", "reviewer")
builder.add_edge("reviewer", "interview")
builder.add_edge("interview", "report")

graph = builder.compile()