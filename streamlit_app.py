import streamlit as st
import numpy as np

st.set_page_config(
  page_title="Banker's Algorithm by Nathan"
)

st.title("Banker's Algorithm App")

# Step 1: Let user define matrix size
rows = st.number_input('Number of rows:', min_value=1, max_value=10, value=3)
cols = st.number_input('Number of columns:', min_value=1, max_value=10, value=3)

# Step 2: Create an editable table
st.write("Input your matrix values:")

# Create empty matrix
matrix_input = []

for i in range(int(rows)):
    row = []
    cols_input = st.columns(int(cols))
    for j in range(int(cols)):
        value = cols_input[j].number_input(f"Row {i+1} Col {j+1}", key=f"{i}-{j}")
        row.append(value)
    matrix_input.append(row)

# Step 3: Display the final matrix
if st.button("Create Matrix"):
    matrix_np = np.array(matrix_input)
    st.write("Here is your matrix:")
    st.write(matrix_np)
