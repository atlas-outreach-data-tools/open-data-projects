import streamlit as st
import pandas as pd
import json

# Set page configuration to wide layout
st.set_page_config(page_title="ATLAS Open Data Contributions", layout="wide")

# Detect the theme from the URL query parameters
theme = st.query_params.get("theme", "light")  # Default to 'light'

# Apply theme styling
if theme == "dark":
    st.markdown(
        """
        <style>
        body {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #ffffff;
        }
        .stMarkdown {
            color: #ffffff;
        }
        img {
            pointer-events: none; /* Prevent image expansion */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        img {
            pointer-events: none; /* Prevent image expansion */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# CSS for tighter spacing between markdown elements
st.markdown(
    """
    <style>
    .stMarkdown p {
        margin: 0px; /* Remove extra margin */
        line-height: 1.5; /* Adjust line height for closer spacing */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Removes anchor from titles
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

# Load the project data from the JSON file
with open("projects.json", "r") as f:
    projects = json.load(f)

# Convert the project data to a DataFrame
df = pd.DataFrame(projects)

# Tag selection for filtering
all_tags = sorted(set(tag for tags in df["programming"] for tag in tags))
selected_tags = st.multiselect("Filter by programming language:", options=all_tags)

# Filter projects based on selected tags
if selected_tags:
    filtered_contributions = df[df["programming"].apply(lambda x: any(tag in x for tag in selected_tags))]
else:
    filtered_contributions = df

# Define the number of columns per row
num_columns = 5  # Adjust the number of columns as needed

# Organize by alphabetical order
filtered_contributions = filtered_contributions.sort_values(by="name")

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
                # Display project card with image, name, responsible, email, language, difficulty, tags, and link
                st.image(project["image"], use_container_width=True)
                st.markdown(f"<h3>{project['name']}</h3>", unsafe_allow_html=True)
                st.markdown(f"**Responsible:** {project['responsible']}")
                st.markdown(f"**Language:** {project['language']}")
                st.markdown(f"**Programming language:** {', '.join(project['programming'])}")
                st.markdown(f"**Difficulty:** {project['difficulty']}")
                st.markdown(f"**Length:** {project['length']}")
                st.markdown(f"[View Source]({project['link']})", unsafe_allow_html=True)
                st.markdown("---")