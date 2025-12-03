# # run.py — launcher (streamlit run run.py)
# import streamlit as st
# from importlib import import_module
# import os

# st.set_page_config(page_title="Google Play Store Analytics - Launcher", layout="wide", page_icon="📱")

# st.markdown("""
# # 📱 Google Play Store Analytics — Launcher
# Use the navigation below to open the dashboard you want.
# """)

# PAGES = {
#     "Overview": "dashboard_1_project_overview.py",
#     "Category Analysis": "dashboard_2_app_domain.py",
#     "ML Models": "dashboard_3_user_domain_and_trends.py",
#     "Data Explorer": "dashboard_4_overall_modeling_overview.py"
# }

# choice = st.sidebar.selectbox("Choose dashboard", list(PAGES.keys()))

# module_name = PAGES[choice]
# module = import_module(module_name)

# # Every dashboard file exposes a `run()` function
# module.run()



# intro.py — robust launcher (imports by file path; works with any filename)
import streamlit as st
from importlib import util
from pathlib import Path
import traceback

st.set_page_config(page_title="Dashboard Launcher", layout="wide", page_icon="📱")
st.title("📱 Dashboard Launcher (robust)")

# --- Update filenames below EXACTLY as they appear in your folder (include .py) ---
PAGES = {
    "Project Overview": "dashboard_1_project_overview.py",
    "Category Analysis": "dashboard_2_category_analysis.py",
    "User Behaviour": "dashboard_3_user_behaviour.py",
    "Modeling": "dashboard_4_modeling.py",
    "Data Explorer": "dashboard_5_data_explorer.py"
}

BASE_DIR = Path(__file__).resolve().parent

def import_from_path(name: str, path: Path):
    spec = util.spec_from_file_location(name, str(path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot import from {path}")
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

choice = st.sidebar.selectbox("Choose dashboard", list(PAGES.keys()))
filename = PAGES[choice]
module_path = BASE_DIR / filename

if not module_path.exists():
    st.error(f"Dashboard file not found: {module_path}\n\nMake sure the filename in PAGES matches exactly (case-sensitive).")
else:
    try:
        # create a safe module name (no dots or hyphens)
        modname = f"dashboard_{filename.replace('.', '_').replace('-', '_')}"
        module = import_from_path(modname, module_path)

        # Preferred: each dashboard file should define a `run()` function.
        if hasattr(module, "run") and callable(module.run):
            module.run()
        else:
            # If no run(), module top-level code already executed on import.
            st.warning(f"Module '{filename}' does not define run(). If you see no UI, wrap code inside `def run():` and re-run.")
    except Exception:
        st.error("Error importing or executing the dashboard module — see full traceback below.")
        st.text(traceback.format_exc())

