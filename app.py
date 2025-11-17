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
# Interpretation (HTML-safe, reliable)
# ---------------------------------------
st.subheader("Interpretation")

html = f"""
<h3>Key Insights</h3>
<p>
With a vulnerability of <strong>{v}</strong>, and a potential loss of <strong>${L:,.0f}</strong>,<br>
the Gordon–Loeb model suggests an optimal cybersecurity investment of:<br>
<strong>${optimal_investment:,.2f}</strong>
</p>

<p>
According to the model, the optimal security budget is at most <strong>37% of the expected loss</strong> (v × L).
</p>

<p>
This model helps organizations avoid <em>overspending</em> or <em>underspending</em> on cybersecurity.
</p>
"""

st.markdown(html, unsafe_allow_html=True)




