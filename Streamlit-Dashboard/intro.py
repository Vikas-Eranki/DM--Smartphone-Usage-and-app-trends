
import streamlit as st
from importlib import util
from pathlib import Path
import traceback

st.set_page_config(
    page_title="Dashboard Launcher",
    layout="wide",
    page_icon=""
)

st.markdown("""
<style>
    .sidebar-selectbox div[data-baseweb="select"] {
            border: 2px solid #02C389 !important;
            border-radius: 8px !important;
            padding: 4px !important;
        }
    .main { background-color: #f8f9fa; }

    [data-testid="stSidebar"] {
       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        border-right: 1px solid #e0e0e0;
    }

    .dashboard-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 8px;
        margin-bottom: 2rem;
        color: white;
    }

    .dashboard-header h1 {
        margin: 0;
        font-size: 2rem;
        font-weight: 600;
    }

    .dashboard-header p {
        margin: 0.5rem 0 0;
        font-size: 1rem;
        opacity: 0.9;
    }

    .dashboard-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin-bottom: 1rem;
        transition: box-shadow 0.2s;
    }

    .dashboard-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 0.4rem;
    }

    .card-description {
        font-size: 0.9rem;
        color: black;
        margin-bottom: 0.6rem;
    }

    .card-file {
        font-size: 0.8rem;
        color: black;
        font-family: monospace;
        background: #f5f5f5;
        padding: 0.3rem 0.5rem;
        border-radius: 4px;
        display: inline-block;
    }

    .metric-container {
        background: white;
        padding: 1.25rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        text-align: center;
    }

    .metric-label {
        font-size: 0.85rem;
        color: black;
        letter-spacing: 0.5px;
        margin-top: 0.3rem;
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 6px;
        font-weight: 500;
        width: 100%;
        transition: transform 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dashboard-header">
    <h1> Dashboard Launcher</h1>
    <p>Professional dashboard suite — Select a module to begin</p>
</div>
""", unsafe_allow_html=True)

PAGES = {
    "Project Overview": "dashboard_1_project_overview.py",
    "App Domain": "dashboard_2_app_domain.py",
    "Smartphone Usage Efficiency": "dashboard_5_smartphone_efficiency.py",
    "Category Analysis": "dashboard_3_category_analysis.py",
    "Overall Modeling Overview": "dashboard_4_overall_modeling_overview.py",
}

BASE_DIR = Path(__file__).resolve().parent

def import_from_path(name: str, path: Path):
    spec = util.spec_from_file_location(name, str(path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot import from {path}")
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

with st.sidebar:


    st.markdown("### Select Dashboard")

    select_container = st.container()
    with select_container:
        select_container.markdown(
            "<div class='sidebar-selectbox'>", unsafe_allow_html=True
        )
        choice = st.selectbox("", list(PAGES.keys()))
        select_container.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"**Total Dashboards:** {len(PAGES)}")
    st.markdown("**Data Source:** Google Play Store")
    st.markdown("**Last Updated:** Dec 2025")


filename = PAGES[choice]

st.markdown(f"""
<div class="dashboard-card">
    <div class="card-title"> {choice}</div>
    <div class="card-description">Launching dashboard interface…</div>
    <div class="card-file">{filename}</div>
</div>
""", unsafe_allow_html=True)

module_path = BASE_DIR / filename

if not module_path.exists():
    st.error(f" Dashboard file not found: `{module_path}`")
    st.info("Make sure the filename in PAGES matches exactly (case-sensitive).")

else:
    try:
        modname = f"dashboard_{filename.replace('.', '_').replace('-', '_')}"
        module = import_from_path(modname, module_path)

        if hasattr(module, "run") and callable(module.run):
            module.run()
        else:
            st.warning(f" Module '{filename}' does not define a run() function.")
            st.info("Wrap your dashboard code in a def run(): function.")
    except Exception:
        st.error(" Error importing or executing the dashboard module.")
        st.text(traceback.format_exc())
