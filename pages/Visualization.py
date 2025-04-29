import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from utils import load_model, get_model_info
import os
from pathlib import Path
import numpy as np
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from scipy import stats
import joblib
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df, categorical_features=None):
    """Handle data preprocessing including categorical encoding and type conversion"""
    if categorical_features is None:
        categorical_features = []
    
    # Convert string booleans to actual booleans
    for col in df.select_dtypes(include='object').columns:
        if df[col].str.lower().isin(['true','false']).any():
            df[col] = df[col].str.lower() == 'true'
    
    # Encode categorical features
    label_encoders = {}
    for col in categorical_features:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
    
    # Convert all numeric columns
    for col in df.columns:
        if col not in categorical_features:
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            except:
                pass
    
    return df, label_encoders

def show():
    st.title("Model Visualization & Monitoring")

    # Get available models and datasets
    models_dir = Path("models")
    datasets_dir = Path("datasets")

    if not models_dir.exists() or not any(models_dir.glob("*.pkl")):
        st.warning("No trained models found. Please train a model first.")
        return

    if not datasets_dir.exists() or not any(datasets_dir.glob("*.csv")):
        st.warning("No datasets available. Please upload a dataset first.")
        return

    # Sidebar for model and dataset selection
    with st.sidebar:
        st.subheader("Select Model & Dataset")
        model_files = [f for f in models_dir.glob("*.pkl")]
        selected_model = st.selectbox(
            "Select Model",
            options=[f.name for f in model_files],
            format_func=lambda x: x.replace(".pkl", "").replace("_", " ").title()
        )

        dataset_files = [f for f in datasets_dir.glob("*.csv")]
        selected_dataset = st.selectbox(
            "Select Dataset",
            options=[f.name for f in dataset_files],
            format_func=lambda x: x.replace(".csv", "").title()
        )

    if selected_model and selected_dataset:
        try:
            # Load model and dataset
            model_data = joblib.load(models_dir / selected_model)
            model = model_data['model']
            feature_names = model_data['feature_names']
            target_column = model_data['target_column']
            categorical_features = model_data.get('categorical_features', [])

            df = pd.read_csv(datasets_dir / selected_dataset)
            
            # Preprocess data
            df_processed, _ = preprocess_data(df.copy(), categorical_features)

            # Get model information
            model_info = get_model_info(models_dir / selected_model)

            # Main content
            st.subheader("Model Information")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Model Type:", model_info["type"])
                st.write("Parameters:", model_info["parameters"])
            with col2:
                st.write("Dataset Shape:", df_processed.shape)
                st.write("Features:", len(df_processed.columns))

            # Feature Importance
            if model_info["feature_importance"] is not None:
                st.subheader("Feature Importance")
                importance_df = pd.DataFrame({
                    'Feature': feature_names,
                    'Importance': model_info["feature_importance"]
                }).sort_values('Importance', ascending=False)

                fig = px.bar(importance_df, x='Importance', y='Feature', orientation='h')
                st.plotly_chart(fig)

            # SHAP Values
            st.subheader("SHAP Values")
            try:
                X = df_processed[feature_names]
                explainer = shap.Explainer(model, X)
                shap_values = explainer(X)

                # Summary plot
                fig, ax = plt.subplots(figsize=(10, 6))
                shap.summary_plot(shap_values, X, show=False)
                st.pyplot(fig)

                # Bar plot
                fig, ax = plt.subplots(figsize=(10, 6))
                shap.summary_plot(shap_values, X, plot_type="bar", show=False)
                st.pyplot(fig)
            except Exception as e:
                st.warning(f"Could not compute SHAP values: {str(e)}")

            # Correlation Matrix
            st.subheader("Feature Correlation Matrix")
            try:
                corr_matrix = df_processed[feature_names + [target_column]].corr()
                fig = px.imshow(corr_matrix, 
                              color_continuous_scale="RdBu",
                              zmin=-1, 
                              zmax=1)
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Could not generate correlation matrix: {str(e)}")
                st.error("Please check your data types and missing values.")

            # Model Performance Metrics
            st.subheader("Model Performance Metrics")
            try:
                X = df_processed[feature_names]
                y_true = df_processed[target_column]
                y_pred = model.predict(X)

                # Classification Report
                report = classification_report(y_true, y_pred)
                st.text(report)

                # Confusion Matrix
                cm = confusion_matrix(y_true, y_pred)
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(cm, annot=True, fmt='d', ax=ax)
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Could not compute performance metrics: {str(e)}")

        except Exception as e:
            st.error(f"Error processing model and data: {str(e)}")
            st.markdown("""
            *Common Solutions:*
            1. Check for incompatible data types in your dataset
            2. Ensure all required features are present
            3. Verify there are no unexpected string values in numeric columns
            """)