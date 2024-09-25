import streamlit as st 
import anthropic 
from PIL import Image
import os
import base64
st.set_page_config(page_title="Claude API Chatbot", page_icon=":tada:", layout="wide")
st.markdown("""
<style>
.stButton>button {
color: #ffffff;
background-color: #4CAF50;
border-color: white;
}
.stButton>button:hover {
color: #ffffff;
background-color: green;
border-color: white;
}
</style>""",unsafe_allow_html=True)
st.html("""<h1 style="text-align:left; color: #4CAF50;">Rakha Claude Anthropic API</h1>""")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.write(file_details)
    if uploaded_file.type.startswith("image"):
        image = Image.open(uploaded_file)

        st.image(image, caption= 'Uploaded Image.', use_column_width=True)
st.html("""<h7 style="text-align:left; color:#0F75BC;">Enter your prompt here:</h7>""")

prompt = st.text_area("", height=250)

if st.button("Generate Response"):
    if not prompt:
        st.error("Prompt is required")
    else:
        client = anthropic.Anthropic(api_key="sk-ant-api03-U-TIINSgIqvl4IVRAxm8HsP-bTtWJKXnhL48wWgN3NWUSNhX_mayCShV8sYuHh0kU-NXU5YbIZVEy9QcP1N30A-3pEMkgAA")
        messages = []

    if uploaded_file:
       file_bytes=uploaded_file.getvalue()
       base64_file= base64.b64encode(file_bytes).decode('utf-8')

    if uploaded_file.type.startswith('image'):
        content_type = "image"
    else:
        content_type = "file"
    messages.append({
        "role": "user",
        "content": [
            {
                "type": content_type,
                "source": {
                "type": "base64",
                "media type": uploaded_file.type,
                "data": base64_file
                          }
            }
        ]
    })

    
    messages.append({
         "role": "user",
         "content": prompt

    })

    response = client.messages.create( model="claude-3-5-sonnnet-20240620",

    messages=messages,

    max_tokens=4000

)

    st.write(response.content[0].text)




