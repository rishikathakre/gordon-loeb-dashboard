import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Gordon–Loeb Model — Example from Gordon, Loeb & Zhou (2020)")
st.write(
    "This dashboard implements the *exact* formula from the example on page 6 "
    "of the Gordon–Loeb paper, using the security breach probability function "
    "s(z,v) = v / (1 + z/2). The optimal investment is z* = √(2 v L) − 2."
)

# -------------------------
# Sidebar Inputs
# -------------------------
st.sidebar.header(" Input Parameters")

v = st.sidebar.selectbox(
    "Vulnerability (v)",
    options=[0.1, 0.3, 0.5],
    index=1,
    help="The three values used in the paper’s example."
)

L = st.sidebar.number_input(
    "Potential Loss (L)",
    min_value=1_000_000.0,
    max_value=150_000_000.0,
    value=10_000_000.0,
    step=1_000_000.0,
    help="Loss values between $1M and $150M as in the paper."
)

# -------------------------
# Correct Optimal Investment (from paper)
# -------------------------
def optimal_z(v, L):
    z_star = np.sqrt(2 * v * L) - 2
    return max(z_star, 0)   # do not allow negative optimal investment

z_star = optimal_z(v, L)

st.sidebar.subheader("📌 Model Output")
st.sidebar.metric("Optimal Investment z*", f"${z_star:,.2f}")

# -------------------------
# Plot optimal z vs L for v
# -------------------------
st.subheader("Optimal Investment Curve (Matches Page 7 of the Paper)")
st.write(
    "For each v = 0.1, 0.3, 0.5 we compute z* = √(2 v L) − 2 "
    "for L ranging from $1M to $150M."
)

L_vals = np.linspace(1_000_000, 150_000_000, 300)

fig, ax = plt.subplots()

for vv in [0.1, 0.3, 0.5]:
    z_vals = np.sqrt(2 * vv * L_vals) - 2
    z_vals = np.maximum(z_vals, 0)
    ax.plot(L_vals, z_vals, label=f"v = {vv}")

ax.set_xlabel("Loss L ($)")
ax.set_ylabel("Optimal Investment z* ($)")
ax.set_title("Optimal Cybersecurity Investment (Exact Example from Paper)")
ax.legend()

st.pyplot(fig)

# -------------------------
# Interpretation
# -------------------------
st.markdown(
    f"""
### Interpretation

- Using **v = {v}** and **L = ${L:,.0f}**,  
  the model yields an optimal cybersecurity investment of:  
  **${z_star:,.2f}**

### Based on the formula:
\[
z^* = \sqrt{{2 v L}} - 2
\]

- Investment increases as loss L increases
- Higher vulnerability v rapidly increases optimal investment
- Negative values are mapped to 0 (no investment needed)
    """
)
