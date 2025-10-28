# ==============================
# upgraded_dashboard.py
# ==============================

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Education & Economic Growth Dashboard", layout="wide")

# ==============================
# # ==============================
st.markdown(
    """
    <style>
    /* Full page background image */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1470&q=80");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Login header style */
    h1 {
        text-align: center;
        color: white;
        background-color: rgba(76, 175, 80, 0.8); /* semi-transparent green */
        padding: 12px;
        border-radius: 10px;
    }

    /* Input boxes */
    div.stTextInput > label, div.stTextInput > input {
        color: white !important;
    }

    /* Login button style */
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size:16px;
        border-radius: 8px;
        padding: 8px 24px;
    }
    div.stButton > button:hover {
        background-color: #45a049;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# Dummy Login
# ==============================
def login():
    st.markdown("<h1>🔒 Login</h1>", unsafe_allow_html=True)
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.login_status = True
            st.success("Login Successful!")
        else:
            st.error("Incorrect username/password")

# ==============================
# Session State
# ==============================
if 'login_status' not in st.session_state:
    st.session_state.login_status = False

if not st.session_state.login_status:
    login()
else:
    st.success("✅ You are logged in!")

    # ==============================
    # Load Dataset
    # ==============================
    @st.cache_data
    def load_data():
        df = pd.read_csv("G:\demo_project\data\data.csv")
        return df

    df = load_data()

    # ==============================
    # Sidebar Navigation & Filters
    # ==============================
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Basic Visualizations", "Advanced Visualizations", "Feature Analysis", "About"])

    st.sidebar.markdown("---")
    st.sidebar.title("Filters")
    continents = st.sidebar.multiselect("Select Continent", options=df['Continent'].unique(), default=df['Continent'].unique())
    gdp_category = st.sidebar.multiselect("Select GDP Category", options=df['GDP per Capita Category'].unique(), default=df['GDP per Capita Category'].unique())
    filtered_df = df[(df['Continent'].isin(continents)) & (df['GDP per Capita Category'].isin(gdp_category))]

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    # ==============================
    # Page 1: Home
    # ==============================
    if page == "Home":
        st.markdown("<h1>🏠 Home</h1>", unsafe_allow_html=True)
        st.markdown("### Dataset Overview")
        st.dataframe(filtered_df.head(10))
        st.markdown(f"**Shape:** {filtered_df.shape}")
        st.markdown(f"**Columns:** {filtered_df.columns.tolist()}")
        st.markdown("**Missing Values:**")
        st.write(filtered_df.isnull().sum())
        st.markdown("**Statistics:**")
        st.write(filtered_df.describe())

    # ==============================
    # Page 2: Basic Visualizations
    # ==============================
    elif page == "Basic Visualizations":
        st.markdown("<h1>📊 Basic Visualizations</h1>", unsafe_allow_html=True)

        st.subheader("Histograms & KDE")
        for col in numeric_cols:
            fig = px.histogram(filtered_df, x=col, nbins=20, marginal="box", color_discrete_sequence=["#4CAF50"])
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Bar / Count Plots")
        for col in categorical_cols:
            fig = px.histogram(filtered_df, x=col, color=col, text_auto=True)
            st.plotly_chart(fig, use_container_width=True)

    # ==============================
    # Page 3: Advanced Visualizations
    # ==============================
    elif page == "Advanced Visualizations":
        st.markdown("<h1>📈 Advanced Visualizations</h1>", unsafe_allow_html=True)

        st.subheader("Violin Plots")
        for col in numeric_cols:
            fig = px.violin(filtered_df, y=col, color_discrete_sequence=["#FF5733"])
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Scatter Plots")
        for i in range(len(numeric_cols)):
            for j in range(i+1, len(numeric_cols)):
                fig = px.scatter(filtered_df, x=numeric_cols[i], y=numeric_cols[j], color="Continent")
                st.plotly_chart(fig, use_container_width=True)

        st.subheader("Correlation Heatmap")
        corr = filtered_df[numeric_cols].corr()
        fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale="RdBu_r")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Pie Charts")
        for col in categorical_cols:
            fig = px.pie(filtered_df, names=col, title=f"Pie Chart: {col}")
            st.plotly_chart(fig, use_container_width=True)

    # ==============================
    # Page 4: Feature Analysis
    # ==============================
    elif page == "Feature Analysis":
        st.markdown("<h1>🧩 Feature Analysis</h1>", unsafe_allow_html=True)

        df_encoded = filtered_df.copy()
        for col in categorical_cols:
            df_encoded[col] = LabelEncoder().fit_transform(df_encoded[col])

        X = df_encoded.drop(columns=['GDP Growth (% Annual)'])
        y = df_encoded['GDP Growth (% Annual)']

        rf = RandomForestRegressor(n_estimators=200, random_state=42)
        rf.fit(X, y)
        importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)

        st.subheader("Top Features")
        st.bar_chart(importances)

        st.subheader("Correlation with Target")
        corr_target = df_encoded.corr()['GDP Growth (% Annual)'].sort_values(ascending=False)
        st.bar_chart(corr_target)

    # ==============================
    # Page 5: About
    # ==============================
    elif page == "About":
        st.markdown("<h1>ℹ️ About This Project</h1>", unsafe_allow_html=True)
        st.markdown("""
        **Project Title:** How Education Drives Economic Growth  
        **Dataset:** how-education-drives-economic-growth.csv  
        **Description:** Interactive Streamlit dashboard to explore literacy, GDP, physician density and economic growth.  
        **Features:**  
        - 40+ interactive plots using Plotly  
        - Filters by Continent and GDP Category  
        - Feature importance & correlation analysis  
        - Styled Markdown/HTML headers and CSS customization  
        **Author:** Your Name  
        **Date:** 2025
        """)
