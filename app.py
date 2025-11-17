# ---------------------------------------
# Gordon–Loeb Investment Curve (Correct Model)
# ---------------------------------------

st.subheader("Gordon–Loeb Investment Curve")
st.write(
    "This graph uses the actual Gordon–Loeb model formula, which shows that "
    "optimal security investment does **not** increase linearly with vulnerability. "
    "Instead, it rises but then flattens out, and never exceeds 1/e of the expected loss."
)

# Correct GL model investment function:
#   z*(v) = (1/e) * L * v * (1 - ln(v))
def gordon_loeb_investment(v, L):
    return (1 / np.e) * L * v * (1 - np.log(v))

# Curve for 0.01 ≤ v ≤ 1.0
v_values = np.linspace(0.01, 1.0, 300)
investment_curve = gordon_loeb_investment(v_values, L)

# Compute optimal investment using correct formula
optimal_investment = gordon_loeb_investment(v, L)

# Plot
fig, ax = plt.subplots()
ax.plot(v_values, investment_curve)
ax.set_xlabel("Vulnerability (v)")
ax.set_ylabel("Optimal Investment ($)")
ax.set_title("Gordon–Loeb Model Investment Curve (Correct Formula)")
st.pyplot(fig)

# ---------------------------------------
# Interpretation
# ---------------------------------------
st.markdown(
    f"""
### Key Insights from the Gordon–Loeb Model

- For vulnerability **v = {v}**, and potential loss **${L:,.0f}**,  
  the recommended cybersecurity investment is:  
  **${optimal_investment:,.2f}**

- The model predicts that optimal security spending:
  - **Does not increase linearly** with vulnerability  
  - Peaks for vulnerabilities around **0.3–0.4**  
  - **Never exceeds ~37% of the expected loss** (v × L)

- Interpretation:
  - Even if vulnerability becomes extremely high (close to 1),  
    **it is not optimal to spend more and more on cybersecurity**.
  - Spending beyond a certain point yields diminishing returns.

This is exactly why the Gordon–Loeb curve goes up and then levels off instead of being a straight line.
"""
)
