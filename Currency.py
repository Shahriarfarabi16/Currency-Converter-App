import streamlit as st

st.title("Hi Homaira! Try This!")
st.title("Your Hubby Made This 😀")

# Input: Currency names
from_currency = st.text_input("Enter the First currency (e.g., USD):")
to_currency = st.text_input("Enter the Second currency (e.g., EUR):")

# Input: Conversion rate
rate = st.number_input("Enter the conversion rate from {} to {}:".format(from_currency or 'First', to_currency or 'Second'))

# Input: Amount
amount = st.number_input("Enter the amount in {}:".format(from_currency or 'First Currency'))

# Button to convert
if st.button("Convert"):
    if from_currency and to_currency and rate > 0:
        result = amount * rate
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        st.warning("Please enter valid inputs for currencies and conversion rate.")
