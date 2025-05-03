import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔓")
st.title("🔓Password Strength Checker")
st.markdown("""
## Welcome to the Ulimate Password strength checker!👋
use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            we will give you helpful tips to create a **strong password**🔓""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append()
    if re.search('[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters.")
    
    if re.search('\d', password):
        score += 1
    else:
         feedback.append("❌Password should contain at least one digit.")

    if re.search('[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character(!@#$%&*).")
    
    if score == 4:
        feedback.append("✅Your password is strong")
    elif score == 3:
        feedback.append("✅Your password is strength in medium. It could be stronger.")
    else:
        feedback.append("🔴Your password is sweak. Please make it sronger.")

    if feedback:
        st.markdown("## Improvement suggestions")
        for tip in feedback:
            st.write(tip)
else: 
    st.info("Please enter your password to get started.")