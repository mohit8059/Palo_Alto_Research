import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("🛡️ Employee Analytics Dashboard - Palo Alto Networks")

# Data Loading
try:
    df = pd.read_csv('Palo_Alto_Analyzed.csv')
except FileNotFoundError:
    st.error("Error: 'Palo_Alto_Analyzed.csv' file nahi mili.")
    st.stop()

# 1. Top Metrics (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", len(df))
col2.metric("Avg Engagement", round(df['Engagement_Index'].mean(), 2))
col3.metric("High Risk Employees", len(df[df['Burnout_Risk_Score']==2]))

st.markdown("---")

# 2. Sidebar Filters
st.sidebar.header("Filters")
dept_filter = st.sidebar.multiselect("Select Department", df['Department'].unique(), default=df['Department'].unique())
filtered_df = df[df['Department'].isin(dept_filter)]

# 3. Visualization and Data Table (Using clear column definitions)
c1, c2 = st.columns(2)

with c1:
    st.subheader("📊 Burnout Risk by Dept")
    fig, ax = plt.subplots(figsize=(6, 4))
    # Count plot using available columns
    sns.countplot(x='Department', hue='Burnout_Risk_Score', data=filtered_df, palette='viridis', ax=ax)
    st.pyplot(fig)

with c2:
    st.subheader("⚠️ Priority Intervention List")
    # Using columns that we confirmed exist
    high_risk = filtered_df[filtered_df['Burnout_Risk_Score'] == 2]
    
    if not high_risk.empty:
        st.dataframe(high_risk[['Department', 'OverTime', 'WorkLifeBalance', 'Engagement_Index']], use_container_width=True)
    else:
        st.write("✅ Koi High Risk employee nahi mila!")

# 4. Intelligence Box
if not high_risk.empty:
    st.info(f"💡 Suggestion: {high_risk['Department'].mode()[0]} department mein High Risk employees sabse zyada hain. Immediate check-in required.")