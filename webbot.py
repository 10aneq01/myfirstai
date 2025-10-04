import streamlit as st

from google import genai
chitti =genai.Client(api_key="AIzaSyDLit1WmoKcR4KdLCz9yk6-hF5L9PrWz_Q")
st.title("my own chatbot")
question = st.text_input("ask antything")

if st.button("send"):
    response = chitti.models.generate_content
    (
        model == "gemini-2.5-flash",
        contents == question
        )
    st.write(response.text)
    


