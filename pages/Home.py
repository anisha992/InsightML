import streamlit as st

def show():
    # Hero Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("🚀 InsightML")
        st.markdown("""
        <h3 style='color: #4a6bff;'>Your Complete Machine Learning Workflow Solution</h3>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://via.placeholder.com/300x200?text=ML+Illustration", width=300)
    
    st.markdown("---")
    
    # Features Section
    st.markdown("<h2 style='text-align: center;'>✨ Key Features</h2>", unsafe_allow_html=True)
    
    features = st.columns(4)
    with features[0]:
        with st.container():
            st.markdown("""
            <div class='card'>
                <h3>📊 Data Management</h3>
                <p>Load, store, and manage datasets with our intuitive interface</p>
            </div>
            """, unsafe_allow_html=True)
    
    with features[1]:
        with st.container():
            st.markdown("""
            <div class='card'>
                <h3>🤖 Model Training</h3>
                <p>Train multiple ML models with various algorithms</p>
            </div>
            """, unsafe_allow_html=True)
    
    with features[2]:
        with st.container():
            st.markdown("""
            <div class='card'>
                <h3>🔮 Predictions</h3>
                <p>Make and export predictions on new data</p>
            </div>
            """, unsafe_allow_html=True)
    
    with features[3]:
        with st.container():
            st.markdown("""
            <div class='card'>
                <h3>📈 Analytics</h3>
                <p>Comprehensive visualization and model analysis</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Getting Started Section
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>🚀 Getting Started</h2>", unsafe_allow_html=True)
    
    steps = st.columns(4)
    with steps[0]:
        st.markdown("""
        <div style='text-align: center;'>
            <h3>1</h3>
            <p>Load your dataset</p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps[1]:
        st.markdown("""
        <div style='text-align: center;'>
            <h3>2</h3>
            <p>Train models</p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps[2]:
        st.markdown("""
        <div style='text-align: center;'>
            <h3>3</h3>
            <p>Make predictions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps[3]:
        st.markdown("""
        <div style='text-align: center;'>
            <h3>4</h3>
            <p>Analyze results</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <p>Need help? <a href='mailto:support@insightml.com'>Contact our team</a></p>
        <p>© 2023 InsightML - All rights reserved</p>
    </div>
    """, unsafe_allow_html=True)