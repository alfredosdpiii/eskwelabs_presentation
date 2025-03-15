import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set page title
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Overall", "Introduction", "Methodology", "Results", "Recommendations"])

# Ensure directories exist
data_dir = "data"
image_dir = "images"
plot_dir = "plots"

os.makedirs(data_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)
os.makedirs(plot_dir, exist_ok=True)

# Overall Section
if menu == "Overall":
    st.title("Overall Summary")

    # Display an image from images folder
    overall_img_path = os.path.join(image_dir, "overall.png")
    if os.path.exists(overall_img_path):
        st.image(overall_img_path, caption="Project Overview", use_container_width=True)
    else:
        st.warning("No overview image found. Please add an image to `images/` directory.")



# Introduction Section
elif menu == "Introduction":
    st.title("Introduction")
    st.write("How can we leverage data science to improve Adobo Bank's performance?")

# Methodology Section
elif menu == "Methodology":
    st.title("Methodology")
    
    st.header("Deep Dive: Addressing Problem #1")
    
    st.subheader("Objectives")
    st.markdown("""
    - Enable effective marketing interventions by generating customer segments from observed patterns in customer transactions
    - Propose next steps that can be adopted in the medium to long-term
    """)
    
    st.subheader("Scope and Limitations")
    st.markdown("""
    Analysis and modeling focused on CY 2021 transactions, particularly on the following dimensions:
    - Recency
    - Frequency
    - Monetary Value
    - Transaction Categories
    
    Customer profiles could not be validated in the absence of income and other demographic data
    """)
    
    st.subheader("Generating the Customer Segments")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        Process flow:
        1. Data Cleaning
        2. Exploratory Data Analysis
        3. Data Transformation
        4. RFM Scoring
        5. K-Means Clustering
        6. Post-Profiling
        """)
        
    with col2:
        st.markdown("""
        Exploratory data analysis using scatter plot showed transaction recency, frequency, and monetary value 
        were promising data elements in generating discrete clusters.
        
        Thus, RFM scores were generated and used in K-Means Clustering.
        """)
    
    st.markdown("""
    The elbow method showed an optimal k of three clusters based on the RFM scores. ✔
    
    However, further testing showed four clusters generated more unique, discrete segments.
    """)

# Results Section
elif menu == "Results":
    st.title("Results")
    
    # Display results image
    results_img_path = os.path.join(image_dir, "results.png")
    if os.path.exists(results_img_path):
        st.image(results_img_path, caption="Analysis Results", use_container_width=True)
    else:
        st.warning("Results image not found. Please add results.png to the images/ directory.")

# Recommendations Section
elif menu == "Recommendations":
    st.title("Recommendations")
    
    # Create a 2x2 grid for recommendations
    col1, col2 = st.columns(2)
    
    # Row 1
    with col1:
        rec1_img_path = os.path.join(image_dir, "recommendation1.png")
        if os.path.exists(rec1_img_path):
            st.image(rec1_img_path, use_container_width=True)
        else:
            st.warning("Recommendation 1 image not found.")
    
    with col2:
        rec2_img_path = os.path.join(image_dir, "recommendation2.png")
        if os.path.exists(rec2_img_path):
            st.image(rec2_img_path, use_container_width=True)
        else:
            st.warning("Recommendation 2 image not found.")
    
    # Row 2
    with col1:
        rec3_img_path = os.path.join(image_dir, "recommendation3.png")
        if os.path.exists(rec3_img_path):
            st.image(rec3_img_path, use_container_width=True)
        else:
            st.warning("Recommendation 3 image not found.")
    
    with col2:
        rec4_img_path = os.path.join(image_dir, "recommendation4.png")
        if os.path.exists(rec4_img_path):
            st.image(rec4_img_path, use_container_width=True)
        else:
            st.warning("Recommendation 4 image not found.")

# Footer
st.sidebar.write("Developed using Streamlit")
