import streamlit as st

st.set_page_config(page_title="6 Months Together!", page_icon="⚛️", layout="centered")

st.title("⚡ CS + Metallurgy: 6 Months")
st.subheader("Happy Anniversary!")

st.markdown("""
```text
   ===========================================================
   [COMP SCI] <-------------------> [METALLURGY]
   ===========================================================
          ______                  ______
        /  ____  \              /  ____  \
       |  /    \  |            |  /    \  |
       |  | FE  | | <========> |  | CODE| |
       |  \____/  |            |  \____/  |
        \______/                \______/
   ===========================================================
  
   
   st.write("---")
    st.header("💌 Decrypted Message")
    message = (
    "They say metallurgy is all about finding the right balance of elements "
    "to build something strong, durable, and resilient. Combining my world of "
    "materials with your world of algorithms and computer science makes us "
    "the ultimate system. \n\n"
    
   "Thank you for an incredible six months. Here is to many more updates, "
    "successful builds, and shared milestones ahead!"
    )
    st.write(message)
else:
    st.warning("Access granted anyway because I love you! ❤️")
    st.balloons()
    fallback_message = (
    "Happy 6 Months! Combining metallurgy and computer science makes us "
    "the ultimate system. Here is to many more updates and shared milestones ahead!"
    )
    st.write(fallback_message)
