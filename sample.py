import streamlit as st

# DELTA STAR conversion function
def delta_to_star(R12, R23, R31):
    denominator = R12 + R23 + R31
    R1 = (R12 * R31) / denominator
    R2 = (R12 * R23) / denominator
    R3 = (R23 * R31) / denominator
    return R1, R2, R3

# Streamlit UI
st.title("2205A21067")
st.write("Enter the values for R12, R23, and R31 to calculate R1, R2, and R3.")

# Create two columns: one for inputs and one for output
col1, col2 = st.columns([1, 1])

# Column 1 for input fields
with col1:
    # Input fields for DELTA resistances
    R12 = st.number_input("Enter R12 (in ohms):", min_value=0.0, step=0.01)
    R23 = st.number_input("Enter R23 (in ohms):", min_value=0.0, step=0.01)
    R31 = st.number_input("Enter R31 (in ohms):", min_value=0.0, step=0.01)
    compute=st.button("compute")
    

# Column 2 for displaying results
with col2:
    # Calculate the STAR resistances when all inputs are provided
    if R12 > 0 and R23 > 0 and R31 > 0:
        R1, R2, R3 = delta_to_star(R12, R23, R31)
        st.subheader("Calculated STAR Resistances:")
        st.write(f"R1 = {R1:.2f} Ω")
        st.write(f"R2 = {R2:.2f} Ω")
        st.write(f"R3 = {R3:.2f} Ω")
    else:
        st.warning("Please enter valid resistance values for R12, R23, and R31.")