from graph import graph


async def analyze_repo(repo_url):

    result = graph.invoke(
        {
            "repo_url": repo_url
        }
    )

    return result["final_report"]