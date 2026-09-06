import streamlit as st

st.set_page_config(page_title="6 Months Together!", page_icon="⚛️", layout="centered")

st.title("⚡ CS + Metallurgy: 6 Months")
st.subheader("Happy Anniversary!")

st.code(
    "===========================================================\n"
    "[COMP SCI] <-------------------> [METALLURGY]\n"
    "===========================================================\n"
    "       ______                  ______\n"
    "     /  ____  \\              /  ____  \\\n"
    "    |  /    \\  |            |  /    \\  |\n"
    "    |  | FE  | | <========> |  | CODE| |\n"
    "    |  \\____/  |            |  \\____/  |\n"
    "     \\______/                \\______/\n"
    "===========================================================",
    language="text"
)

st.write("---")
st.header("🔒 System Security Check")

q1 = st.radio("1. What is the strength of our bond?", ["Low carbon steel", "Unbreakable crystal lattice", "Null pointer"])
q2 = st.radio("2. How long have we been running this process?", ["6 days", "6 months", "Infinite loop"])

if st.button("Unlock Anniversary Message"):
    if q1 == "Unbreakable crystal lattice" and q2 == "6 months":
        st.success("ACCESS GRANTED! System status: Perfect Match.")
        st.balloons()
        
        st.write("---")
        st.header("💌 Decrypted Message")
        message = (
            "They say metallurgy is all about finding the right balance of elements "
            "to build something strong, durable, and resilient. Combining my world of "
            "materials with your world of algorithms and computer science makes us "
            "the ultimate system.\n\n"
            "Thank you for an incredible six months. Here's to many more updates, "
            "successful builds, and shared milestones ahead!"
        )
        st.write(message)
    else:
        st.warning("Access granted anyway because I love you! ❤️")
        st.balloons()
        fallback_message = (
            "Happy 6 Months! Combining metallurgy and computer science makes us "
            "the ultimate system. Here's to many more updates and shared milestones ahead!"
        )
        st.write(fallback_message)
