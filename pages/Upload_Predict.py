import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

def clean_and_preprocess(df):
    """Handle all data cleaning and preprocessing steps"""
    # Fix problematic numeric columns first
    for col in ['Age', 'Fees']:
        if col in df.columns:
            # Handle slash values (e.g., "9.7513/12")
            df[col] = df[col].astype(str).str.split('/').str[0]
            # Convert to numeric, coercing errors to NaN
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Encode categorical columns
    categorical_cols = ['Set', 'Not']  # Adjust based on your actual categorical columns
    label_encoders = {}
    for col in categorical_cols:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
    
    # Handle missing values
    numeric_cols = df.select_dtypes(include=np.number).columns
    imputer = SimpleImputer(strategy='median')
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    
    return df, label_encoders

def show():
    st.title("Data Upload & Prediction")
    
    # File upload section
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            
            # Show raw data preview
            st.subheader("Raw Data Preview")
            st.dataframe(df.head())
            
            # Clean and preprocess
            with st.spinner("Cleaning and preprocessing data..."):
                df_clean, _ = clean_and_preprocess(df.copy())
                
                # Show cleaning results
                st.subheader("Cleaning Report")
                st.markdown("""
                - Fixed numeric columns with slash values
                - Encoded categorical variables
                - Handled missing values with median imputation
                """)
                
                st.subheader("Processed Data Preview")
                st.dataframe(df_clean.head())
                
                # Show missing values report
                st.subheader("Missing Values After Processing")
                st.write(pd.DataFrame({
                    'Column': df_clean.columns,
                    'Missing Values': df_clean.isna().sum()
                }))
                
                # Continue with model prediction...
                # (Add your prediction logic here)
                
        except Exception as e:
            st.error(f"Processing failed: {str(e)}")
            st.markdown("""
            **Common Solutions:**
            1. Check for special characters in numeric fields
            2. Ensure categorical columns have consistent values
            3. Verify no empty rows in your CSV
            """)

if __name__ == "__main__":
    show()