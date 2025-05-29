import streamlit as st
import pandas as pd
import plotly.express as px

st.title("STEM Activity Engagement Dashboard")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Data", df.head())

    # Select columns to plot
    x_col = st.selectbox("Select X-axis", df.columns)
    y_col = st.selectbox("Select Y-axis", df.columns)
    chart_type = st.selectbox("Chart Type", ["Line", "Bar"])

    if st.button("Generate Plot"):
        if chart_type == "Line":
            fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} over {x_col}")
        else:
            fig = px.bar(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}")
        st.plotly_chart(fig)
else:
    st.info("Please upload a CSV file to begin.")
