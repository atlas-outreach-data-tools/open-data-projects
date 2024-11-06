import streamlit as st
import pandas as pd
import json

# Set page configuration to wide layout
st.set_page_config(page_title="ATLAS Open Data Contributions", layout="wide")

# Load the project data from the JSON file
with open("projects.json", "r") as f:
    projects = json.load(f)

# Convert the project data to a DataFrame
df = pd.DataFrame(projects)

# Title of the app
st.title("ATLAS Open Data Contributions")

# Tag selection for filtering
all_tags = sorted(set(tag for tags in df["tags"] for tag in tags))
selected_tags = st.multiselect("Filter by tags:", options=all_tags)

# Filter projects based on selected tags
if selected_tags:
    filtered_contributions = df[df["tags"].apply(lambda x: any(tag in x for tag in selected_tags))]
else:
    filtered_contributions = df

# Define the number of columns per row
num_columns = 5  # Adjust the number of columns as needed

# Display projects in a grid layout
rows = []
for index, row in filtered_contributions.iterrows():
    rows.append(row)

# Loop over the rows in chunks according to num_columns
for i in range(0, len(rows), num_columns):
    cols = st.columns(num_columns)
    for j, col in enumerate(cols):
        if i + j < len(rows):
            project = rows[i + j]
            with col:
                # Display project card with image, title, author, and link
                st.image(project["image"], use_column_width=True)
                st.markdown(f"### {project['name']}")
                st.markdown(f"**Author:** {project['author']}")
                st.markdown(f"**Tags:** {', '.join(project['tags'])}")
                st.markdown(f"[View Source]({project['link']})", unsafe_allow_html=True)
                st.markdown("---")
