import streamlit as st
from pages import Home, Dataset_Load, Train_Models, Upload_Predict, Visualization
from streamlit_option_menu import option_menu  # Requires pip install streamlit-option-menu

# Set page config with new theme
st.set_page_config(
    page_title="InsightML",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# In your app.py, replace the CSS with this:
st.markdown("""
    <style>
    /* Main content */
    .main {
        background-color: #ffffff;
        padding: 2rem 4rem;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #4a6bff 0%, #2541b2 100%);
    }
    
    /* Text colors */
    h1, h2, h3, h4, h5, h6 {
        color: #1a3a8f !important;
    }
    
    /* Tables and dataframes */
    .stDataFrame {
        background-color: white !important;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #4a6bff;
        color: white !important;
    }
    
    /* Markdown text */
    .stMarkdown {
        color: #333333 !important;
    }
    
    /* Alerts */
    .stAlert {
        background-color: #f8f9fa !important;
    }
    
    /* Input widgets */
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>select {
        background-color: white !important;
        color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Modern sidebar navigation
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: white;'>InsightML</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Using option_menu for modern navigation
    page = option_menu(
        menu_title=None,
        options=["Home", "Dataset Load", "Train Models", "Upload & Predict", "Visualization"],
        icons=["house", "database", "robot", "cloud-upload", "bar-chart"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "white", "font-size": "16px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "color": "white"},
            "nav-link-selected": {"background-color": "#1e3a8a"},
        }
    )
    
    st.session_state["page"] = page
    
    st.markdown("---")
    st.markdown("""
    <div style='color: white;'>
    <h3>Quick Guide</h3>
    <ol>
        <li>Load your dataset</li>
        <li>Train ML models</li>
        <li>Make predictions</li>
        <li>Analyze results</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: white;'>
        <p>Version 2.0</p>
        <p>Powered by Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# Render the selected page with new styling
if st.session_state["page"] == "Home":
    Home.show()
elif st.session_state["page"] == "Dataset Load":
    Dataset_Load.show()
elif st.session_state["page"] == "Train Models":
    Train_Models.show()
elif st.session_state["page"] == "Upload & Predict":
    Upload_Predict.show()
elif st.session_state["page"] == "Visualization":
    Visualization.show()