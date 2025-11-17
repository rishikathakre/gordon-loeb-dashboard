import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------
# Dashboard Title
# ---------------------------------------
st.title("Gordon–Loeb Cybersecurity Investment Model Dashboard")
st.write(
    "This dashboard visualizes the Gordon–Loeb model, which helps determine "
    "the optimal level of cybersecurity investment for a given vulnerability and loss estimate."
)

# ---------------------------------------
# Sidebar Inputs
# ---------------------------------------
st.sidebar.header(" Input Parameters")

v = st.sidebar.slider(
    "Vulnerability (v)",
    min_value=0.01,
    max_value=1.0,
    value=0.3,
    step=0.01,
    help="Probability that the asset will be compromised."
)

L = st.sidebar.number_input(
    "Potential Loss (L)",
    min_value=1000.0,
    max_value=10_000_000.0,
    value=100000.0,
    step=1000.0,
    help="Financial loss if the asset is compromised."
)

# Gordon–Loeb simplified optimal investment
optimal_investment = (1 / np.e) * v * L

st.sidebar.write("---")
st.sidebar.subheader("📌 Model Output")
st.sidebar.metric("Optimal Investment", f"${optimal_investment:,.2f}")

# ---------------------------------------
# Main Section
# ---------------------------------------

st.subheader(" Gordon–Loeb Investment Curve")
st.write("The curve shows how recommended investment changes as vulnerability varies.")

# Generate curve data
v_values = np.linspace(0.01, 1.0, 200)
investment_curve = (1 / np.e) * v_values * L

# Plot
fig, ax = plt.subplots()
ax.plot(v_values, investment_curve)
ax.set_xlabel("Vulnerability (v)")
ax.set_ylabel("Optimal Investment")
ax.set_title("Gordon–Loeb Model Curve")
st.pyplot(fig)

# ---------------------------------------
# Interpretation
# ---------------------------------------

st.subheader("Interpretation")
st.write(
    f"""
### Key Insights  
- With a vulnerability of **{v}, and a potential loss of **${L:,.0f},  
  the Gordon Loeb model suggests an optimal cybersecurity investment of:  
  **${optimal_investment:,.2f}

- According to the model, the optimal security budget is at most **37% of the expected loss** (v × L).

- This model helps organizations avoid *overspending* or *underspending* on cybersecurity.
"""
)

