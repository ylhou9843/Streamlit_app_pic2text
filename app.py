import streamlit as st
from PIL import Image
import pytesseract
import os

def image_to_text(image):
    
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\yhou\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    # pytesseract.pytesseract.tesseract_cmd = r'\usr\bin\tesseract'
    # # pytesseract.pytesseract.tesseract_cmd = r'https://github.com/ylhou9843/Streamlit_app_pic2text/blob/0c48e12f80f2f9ff0a233f32adb2001f722bbe57/tesseract.exe'

    return pytesseract.image_to_string(image)



# Main function to run the app
def main():
    # Streamlit UI

    st.set_page_config(page_title="PIC Converter", page_icon="⚡" )
    st.title("Welcome to MyCAF PIC Converter!")
    st.write("Upload image to extract text:")

    # File uploader widget
    # uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    uploaded_images = st.file_uploader("Choose image(s)...", type=["png", "jpg", "jpeg"],accept_multiple_files=True)

    if uploaded_images:
        for idx, uploaded_image in enumerate(uploaded_images, start=1):
            st.markdown(f"### {uploaded_image.name}")
            
            # Open and display image
            image = Image.open(uploaded_image)
            st.image(image, caption=f"Uploaded Image {idx}", use_container_width=True)

            # Extract text
            text = image_to_text(image)

            # Display output
            st.subheader(f"Extracted Text from Image {idx}:")
            st.write(text)


# Call main function
if __name__ == "__main__":
    main()

