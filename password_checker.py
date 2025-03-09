import streamlit as st
import re
import base64

# Set page config
st.set_page_config(page_title="Password Checker", page_icon="🔐", layout="centered")

# Function to encode local image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Add background image
background_image = get_base64_of_image("images/backimage.jpg")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image}");
        background-size: cover;
        background-position: center;
    }}
    .gradient-text {{
        background: linear-gradient(90deg, #FFA500, #FF4500); /* Orange gradient */
        -webkit-background-clip: text;
        -moz-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        -moz-text-fill-color: transparent;
        color: transparent; /* Standard property */
        font-weight: bold;
    }}
    .lock-emoji {{
        color: inherit; /* Retain the original color of the emoji */
        text-align:center;
    }}
    .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white background */
        border: 1px solid #FF4500; /* Orange border */
        border-radius: 5px;
        padding: 10px;
        color: #FF4500; /* Orange text color */
    }}

    /* Style for the placeholder text */
    .stTextInput input::placeholder {{
        color: black; 
        font-weight:bold;
    }}    
    </style>
    """,
    unsafe_allow_html=True,
)
# title
st.markdown(
    '<h1><span class="lock-emoji">🔒</span> <span class="gradient-text">PassFortify: Strength Checker</span></h1>',
    unsafe_allow_html=True,
)
st.markdown("""
    ### 💥Welcome to the **Ultimate Password Strength Analyzer**!  
🔶 In today's digital world, your password is your first line of defense.  
   🔸 This tool helps you evaluate the strength of your password and provides actionable<br>🔸tips to make it **unbreakable**.  
    🔸Let's create a password that even hackers can't crack! 💪  
""",unsafe_allow_html=True)

# Create a box for the password form
with st.container():
    st.markdown("### 🔷 Enter Your Password ⤵️")
    password = st.text_input("🔸Password", type="password", placeholder="Type your password here...", key="password_input")

    feedback = []
    strength = 0

    if password:
        # Check password length
        if len(password) >= 8:
            strength += 1
        else:
            feedback.append("❌ Password should be at least 8 characters long.")

        # Check for both uppercase and lowercase letters
        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            strength += 1
        else:
            feedback.append("❌ Password should contain both uppercase and lowercase characters.")

        # Check for digits
        if re.search(r'[0-9]', password):
            strength += 1
        else:
            feedback.append("❌ Password should contain at least one digit.")

        # Check for special characters
        if re.search(r'[!@#$%&*]', password):
            strength += 1
        else:
            feedback.append("❌ Password should contain at least one special character (!@#$%&*).")

        # Determine strength level
        if strength == 4:
            st.markdown("Strength Level: ✅ **Strong Password! 🎉**", unsafe_allow_html=True)
            feedback.append("✅ Your password is strong!🔓 🎉")
            st.balloons()
        elif strength == 3:
            st.markdown("Strength Level: 🟡 **Medium Password! ⚠️**", unsafe_allow_html=True)
            feedback.append("🟡 Your password is medium strength. It could be stronger.")
        else:
            st.markdown("Strength Level: 🔴 **Weak Password! 🚨**", unsafe_allow_html=True)
            feedback.append("🔴 Your password is weak. Please make it stronger.")

        # Display feedback
        if feedback:
            st.markdown("### 📌Improvement Suggestions")
            for tip in feedback:
                if tip.startswith("✅"):
                    st.success(tip)
                elif tip.startswith("🟡"):
                    st.warning(tip)
                elif tip.startswith("🔴"):
                    st.error(tip)
                else:
                    st.info(tip)
    else:
        st.info("🔸Please enter your password to get started 🔑")

st.markdown("""
    <hr>
    <div style="text-align: center; padding: 10px; font-size: 18px; color: white;">
        © 2025 | Developed by <b style='color:#FFa500;font-size:20px;'>Sana Faisal
        <a href="https://www.linkedin.com/in/sana-faisal-developer/" target="_blank" style="color:black; text-decoration: none;">
            🔗 Connect on LinkedIn
        </a>
    </div>
""", unsafe_allow_html=True)

