import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load student data
df = pd.read_csv("students.csv")

# Title
st.title("📊 Student Performance Dashboard")
st.write("Analyze student marks, attendance and placement data.")

# Sidebar filter
st.sidebar.header("🔍 Filter")

department = st.sidebar.selectbox(
    "Select Department",
    ["All"] + list(df["Department"].unique())
)

# Apply department filter
if department == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[df["Department"] == department].copy()

# Calculate average marks
filtered_df["Average"] = filtered_df[
    ["Python", "Java", "Maths"]
].mean(axis=1)

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👨‍🎓 Total Students",
    len(filtered_df)
)

col2.metric(
    "📚 Average Mark",
    round(filtered_df["Average"].mean(), 2)
)

col3.metric(
    "📅 Attendance",
    f"{filtered_df['Attendance'].mean():.1f}%"
)

placement_rate = (
    filtered_df["Placement"].eq("Yes").mean() * 100
)

col4.metric(
    "💼 Placement Rate",
    f"{placement_rate:.1f}%"
)

st.divider()

# -------------------------------
# Subject Performance
# -------------------------------

st.subheader("📚 Subject Performance")

subject_average = filtered_df[
    ["Python", "Java", "Maths"]
].mean()

fig1, ax1 = plt.subplots()

subject_average.plot(
    kind="bar",
    ax=ax1
)

ax1.set_ylabel("Average Marks")
ax1.set_xlabel("Subject")
ax1.set_title("Average Marks by Subject")

st.pyplot(fig1)

# -------------------------------
# Student Details
# -------------------------------

st.subheader("👨‍🎓 Student Details")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# -------------------------------
# Placement Status
# -------------------------------

st.subheader("💼 Placement Status")

placement_count = filtered_df["Placement"].value_counts()

fig2, ax2 = plt.subplots()

placement_count.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax2
)

ax2.set_ylabel("")

st.pyplot(fig2)

# -------------------------------
# Attendance Analysis
# -------------------------------


st.subheader("📈 Attendance Analysis")

fig3, ax3 = plt.subplots(figsize=(8, 4))

ax3.bar(
    filtered_df["Name"],
    filtered_df["Attendance"]
)

ax3.set_xlabel("Student")
ax3.set_ylabel("Attendance (%)")
ax3.set_title("Student Attendance")

ax3.tick_params(
    axis="x",
    rotation=45
)

plt.tight_layout()

st.pyplot(fig3, use_container_width=False)