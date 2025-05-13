import streamlit as st
from PIL import Image

st.set_page_config(page_title="Vietnamese Document Search Tool")

st.title("🇻🇳 Vietnamese Document Search Tool")

st.write("This app allows you to interact with documents in Vietnamese using AI.")

# Simulated features
option = st.selectbox("Choose a feature:", ["Chat with Document", "Generate Image", "Generate Video"])

if option == "Chat with Document":
    query = st.text_input("Ask something about your document:")
    if query:
        st.write(f"🤖 AI Response: This is a placeholder answer for '{query}'.")
elif option == "Generate Image":
    prompt = st.text_input("Enter an image prompt:")
    if prompt:
        st.image("https://placekitten.com/400/300", caption="Generated Image (placeholder)")
elif option == "Generate Video":
    st.video("https://samplelib.com/lib/preview/mp4/sample-5s.mp4")

st.markdown("**Built with Streamlit & Flask.**")
