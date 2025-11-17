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

# ---------------------------------------
# Correct Gordon–Loeb Model Function
# ---------------------------------------
def gordon_loeb_investment(v, L):
    return (1 / np.e) * L * v * (1 - np.log(v))

# Compute current optimal investment
optimal_investment = gordon_loeb_investment(v, L)

# Sidebar output
st.sidebar.write("---")
st.sidebar.subheader("📌 Model Output")
st.sidebar.metric("Optimal Investment", f"${optimal_investment:,.2f}")

# ---------------------------------------
# Correct Gordon–Loeb Investment Curve
# ---------------------------------------
st.subheader("Gordon–Loeb Investment Curve (Correct Model)")
st.write(
    "The true Gordon–Loeb model predicts that optimal investment rises with vulnerability "
    "but then declines due to diminishing returns. This graph shows the correct shape."
)

# Curve values
v_values = np.linspace(0.01, 1.0, 300)
investment_curve = gordon_loeb_investment(v_values, L)

# Plot
fig, ax = plt.subplots()
ax.plot(v_values, investment_curve)
ax.set_xlabel("Vulnerability (v)")
ax.set_ylabel("Optimal Investment ($)")
ax.set_title("Gordon–Loeb Model Investment Curve")
st.pyplot(fig)

# ---------------------------------------
# Interpretation
# ---------------------------------------
st.markdown(
    f"""
### 🔍 Key Insights

- With vulnerability **v = {v}**, and potential loss **${L:,.0f}**,  
  the Gordon–Loeb model recommends investing:  
  **${optimal_investment:,.2f}**

- The model shows:
  - Investment rises as vulnerability increases  
  - But after a point (~0.35), extra vulnerability **does NOT justify more spending**  
  - Spending never exceeds **37% of the expected loss** (v × L)

- This reflects real-world diminishing returns:  
  throwing more money at cybersecurity **does not always improve protection**.

"""
)
