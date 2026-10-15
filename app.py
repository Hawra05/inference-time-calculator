import streamlit as st
import math
import pandas as pd

st.title("Inference Time Calculator")
st.write("how many copies of an AI model until at least one fixes the bug?")

p_success = st.number_input(
    "Chance that ONE copy, on its own, fixes the bug", 
    min_value=0.001, max_value=0.999, value=0.159, format="%.3f"
)

target = st.number_input(
    "How sure you want to be that at least one copy fixes the bug", 
    min_value=0.01, max_value=0.99, value=0.95, format="%.2f"
)

# Calculate minimum copies using complement rule
if 0 < p_success < 1 and 0 < target < 1:
    n_copies = math.ceil(math.log(1 - target) / math.log(1 - p_success))
    
    st.subheader("The Answer")
    st.markdown(f"## {n_copies} copies")
    st.write(f"the smallest number so that at least one fixes the bug with probability >= {target*100:.1f}%")

st.divider()

st.subheader("The Chance of E")
slider_copies = st.slider("Number of copies", 1, 100, 1)

# P(E) = 1 - (1 - p)^n
chance = 1 - math.pow(1 - p_success, slider_copies)

st.markdown(f"## {chance * 100:.2f}%")
st.write(f"chance that at least one of {slider_copies} copies fixes the bug")

st.latex(rf"P(E) = 1 - (1 - {p_success})^{{{slider_copies}}} = {chance:.4f}")

st.divider()

st.subheader("The Graph")
st.write("Chance that at least one copy fixes the bug, by number of copies")

chart_data = pd.DataFrame({
    'copies': range(1, 101),
    'chance': [1 - math.pow(1 - p_success, i) for i in range(1, 101)]
})

st.line_chart(chart_data, x='copies', y='chance', height=300)