import asyncio
import streamlit as st

from analyzer import analyze_repo
from pdf_generator import generate_pdf
from github_tools import extract_repo

st.set_page_config(
    page_title="AI GitHub Intelligence System",
    page_icon="🚀"
)

# ---------- Custom CSS ----------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:900px;
}

.main-title{
    text-align:center;
    font-size:2.5rem;
    font-weight:700;
    margin-bottom:0.2rem;
}

.sub-title{
    text-align:center;
    color:#888;
    font-size:1.1rem;
    margin-bottom:2rem;
}

.metric-card{
    padding:1rem;
    border-radius:12px;
    border:1px solid rgba(128,128,128,0.2);
    text-align:center;
}

div[data-testid="stTextInput"] input{
    border-radius:12px;
}

div[data-testid="stButton"] button{
    width:100%;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:600;
}

div[data-testid="stDownloadButton"] button{
    width:100%;
    border-radius:12px;
    height:50px;
    font-size:16px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ---------- Hero Section ----------

st.markdown(
    """
    <div class="main-title">
        🚀 AI GitHub Intelligence System
    </div>

    <div class="sub-title">
        Multi-Agent Repository Analysis using LangGraph, Gemini and GitHub API
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Input ----------

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/langchain-ai/langgraph"
)

analyze_btn = st.button(
    "🔍 Analyze Repository"
)

# ---------- Analysis ----------

if analyze_btn:

    if not repo_url:

        st.error(
            "Please enter a GitHub repository URL."
        )

        st.stop()

    if "github.com" not in repo_url:

        st.error(
            "Please enter a valid GitHub repository URL."
        )

        st.stop()

    progress = st.empty()

    progress.info(
        "🤖 Multi-Agent System is analyzing the repository..."
    )

    try:

        with st.spinner(
            "Running analysis..."
        ):

            report = asyncio.run(
                analyze_repo(repo_url)
            )

        progress.success(
            "✅ Analysis Completed Successfully"
        )

        owner, repo_name = extract_repo(
            repo_url
        )

        # Repository Card

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f"""
                <div class="metric-card">
                    <h4>Repository</h4>
                    <p>{repo_name}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="metric-card">
                    <h4>Owner</h4>
                    <p>{owner}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")

        # Report

        st.subheader(
            "📄 Repository Intelligence Report"
        )

        st.markdown(report)

        # PDF Export

        pdf_file = generate_pdf(
            report,
            repo_name
        )

        st.download_button(
            label="📥 Download PDF Report",
            data=pdf_file,
            file_name=f"{repo_name}_analysis.pdf",
            mime="application/pdf"
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

# ---------- Footer ----------

st.markdown("---")

st.caption(
    "Powered by LangGraph • LangChain • Gemini • GitHub API"
)

