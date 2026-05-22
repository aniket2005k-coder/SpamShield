import streamlit as st
import os

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SpamShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global dark-mode CSS ───────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}
.stApp {
    background: #0a0a14;
    color: #e2e8f0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0f0f1e !important;
    border-right: 1px solid #1e1e3a;
}
[data-testid="stSidebar"] .stMarkdown p { color: #94a3b8; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stRadio label { color: #94a3b8; }

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: all 0.25s ease !important;
    padding: 0.5rem 1.2rem !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(102,126,234,0.45) !important;
    filter: brightness(1.15) !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
}

/* ── Inputs ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: #131320 !important;
    border: 1px solid #2d2d4a !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
    transition: border-color 0.2s !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 2px rgba(102,126,234,0.25) !important;
}

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: #131320;
    border: 1px solid #1e1e3a;
    border-radius: 12px;
    padding: 1rem;
    transition: border-color 0.2s;
}
[data-testid="metric-container"]:hover { border-color: #667eea; }
[data-testid="metric-container"] label { color: #94a3b8 !important; }
[data-testid="metric-container"] [data-testid="metric-value"] { color: #e2e8f0 !important; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #0f0f1e;
    border-radius: 10px;
    gap: 4px;
    padding: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    color: #94a3b8 !important;
    font-weight: 500;
    padding: 0.5rem 1.2rem;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
}

/* ── Dataframe ── */
.stDataFrame { border-radius: 12px; overflow: hidden; }
[data-testid="stDataFrame"] { background: #131320; }

/* ── File uploader ── */
[data-testid="stFileUploadDropzone"] {
    background: #131320 !important;
    border: 2px dashed #2d2d4a !important;
    border-radius: 12px !important;
    transition: border-color 0.2s !important;
}
[data-testid="stFileUploadDropzone"]:hover { border-color: #667eea !important; }

/* ── Alerts ── */
.stAlert { border-radius: 10px !important; }
.stSuccess { background: rgba(34,197,94,0.12) !important; border-color: #22c55e !important; }
.stError   { background: rgba(239,68,68,0.12) !important; border-color: #ef4444 !important; }
.stWarning { background: rgba(245,158,11,0.12) !important; border-color: #f59e0b !important; }
.stInfo    { background: rgba(102,126,234,0.12) !important; border-color: #667eea !important; }

/* ── Forms ── */
[data-testid="stForm"] {
    background: #131320;
    border: 1px solid #1e1e3a;
    border-radius: 16px;
    padding: 1.5rem;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: #131320 !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0f0f1e; }
::-webkit-scrollbar-thumb { background: #2d2d4a; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #667eea; }

/* ── Nav radio ── */
div[data-testid="stRadio"] > div { flex-direction: column; gap: 0.3rem; }
div[data-testid="stRadio"] label {
    background: #131320;
    border: 1px solid #1e1e3a;
    border-radius: 10px;
    padding: 0.5rem 1rem;
    color: #94a3b8 !important;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 0.9rem;
}
div[data-testid="stRadio"] label:hover { border-color: #667eea; color: #e2e8f0 !important; }

/* ── Download button ── */
.stDownloadButton > button {
    background: linear-gradient(135deg, #11998e, #38ef7d) !important;
    color: #0a0a14 !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
}

/* ── Progress bar ── */
.stProgress > div > div > div { background: linear-gradient(135deg, #667eea, #764ba2); }

/* ── Divider ── */
hr { border-color: #1e1e3a !important; }

/* ── Number input ── */
.stNumberInput input {
    background: #131320 !important;
    border: 1px solid #2d2d4a !important;
    color: #e2e8f0 !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Ensure directories exist ───────────────────────────────────────────────────
for d in ["auth", "dataset", "uploads", "history", "model", "assets", "utils"]:
    os.makedirs(d, exist_ok=True)

# ── Auth guard ────────────────────────────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    from auth.auth_manager import render_auth_ui
    render_auth_ui()
    st.stop()

# ── Sidebar navigation ────────────────────────────────────────────────────────
username = st.session_state.get("username", "User")
role     = st.session_state.get("role", "user")

with st.sidebar:
    # Logo / brand
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0 0.5rem 0;">
        <div style="font-size:2.5rem;">🛡️</div>
        <div style="font-size:1.3rem; font-weight:800;
                    background:linear-gradient(135deg,#667eea,#764ba2);
                    -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            SpamShield AI
        </div>
        <div style="color:#64748b; font-size:0.75rem; margin-top:0.2rem;">
            Advanced Email Protection
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # User badge
    badge_color = "#f59e0b" if role == "admin" else "#667eea"
    badge_icon  = "🛡️ Admin" if role == "admin" else "👤 User"
    st.markdown(f"""
    <div style="background:#131320; border:1px solid {badge_color}44;
                border-radius:10px; padding:0.6rem 0.8rem; margin-bottom:0.8rem;
                display:flex; align-items:center; gap:0.5rem;">
        <span style="color:{badge_color}; font-weight:600; font-size:0.85rem;">
            {badge_icon}
        </span>
        <span style="color:#94a3b8; font-size:0.85rem;">{username}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Navigation**")

    # Build nav options
    nav_options = ["🏠 Dashboard", "📧 Scan Email", "📬 Gmail Sync", "📜 Scan History", "🤖 Train Models"]
    if role == "admin":
        nav_options.append("🛡️ Admin Panel")

    page = st.radio("", nav_options, label_visibility="collapsed")

    st.divider()

    # Model status indicator
    from model.ml_engine import get_trained_models
    trained = get_trained_models()
    st.markdown("**Model Status**")
    for mname in ["Naive Bayes", "Logistic Regression", "Random Forest", "SVM"]:
        dot = "🟢" if mname in trained else "🔴"
        st.markdown(f"<span style='font-size:0.8rem;color:#94a3b8'>{dot} {mname}</span>",
                    unsafe_allow_html=True)

    st.divider()

    # Logout
    if st.button("🚪 Logout", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.markdown("""
    <div style="text-align:center; color:#374151; font-size:0.7rem; margin-top:1rem;">
        SpamShield AI v1.0.0<br>Built with Streamlit & scikit-learn
    </div>
    """, unsafe_allow_html=True)

# ── Route to pages ────────────────────────────────────────────────────────────
if page == "🏠 Dashboard":
    from utils.dashboard_page import render_dashboard
    render_dashboard()

elif page == "📧 Scan Email":
    from utils.scan_page import render_scan_page
    render_scan_page()

elif page == "📬 Gmail Sync":
    from utils.gmail_page import render_gmail_page
    render_gmail_page()

elif page == "📜 Scan History":
    from utils.history_page import render_history_page
    render_history_page()

elif page == "🤖 Train Models":
    from utils.training_page import render_training_page
    render_training_page()

elif page == "🛡️ Admin Panel" and role == "admin":
    from utils.admin_page import render_admin_panel
    render_admin_panel()

else:
    st.error("🚫 Access denied.")
