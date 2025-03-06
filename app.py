import streamlit as st
from PIL import Image
import pytesseract
import os
# def image_to_text(image):
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Users\yhou\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
#     # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
#     # pytesseract.pytesseract.tesseract_cmd = r'https://github.com/ylhou9843/Streamlit_app_pic2text/blob/0c48e12f80f2f9ff0a233f32adb2001f722bbe57/tesseract.exe'
    
#     return pytesseract.image_to_string(image)

def image_to_text(image):

    # For Streamlit Cloud (Linux environment), use the following path
    if not os.path.isfile('/usr/bin/tesseract'):
        os.system('apt-get update')
        os.system('apt-get install -y tesseract-ocr')

    # Set the path to the Tesseract executable (on cloud: Linux)
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    # If running on Windows locally, you can use the path for Tesseract installation on Windows
    if os.name == 'nt':
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\yhou\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\yhou\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    # pytesseract.pytesseract.tesseract_cmd = r'\usr\bin\tesseract'
    # pytesseract.pytesseract.tesseract_cmd = r'https://github.com/ylhou9843/Streamlit_app_pic2text/blob/0c48e12f80f2f9ff0a233f32adb2001f722bbe57/tesseract.exe'

    return pytesseract.image_to_string(image)


# Main function to run the app
def main():
    # Streamlit UI

    st.set_page_config(page_title="PIC Converter", page_icon="⚡" )
    st.title("Welcome to MyCAF PIC Converter!")
    st.write("Upload an image to extract text:")

    # File uploader widget
    uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        # Open and display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Extract text from image
        text = image_to_text(image)

        # Display the extracted text
        st.subheader("Extracted Text:")
        st.write(text)

# Call main function
if __name__ == "__main__":
    main()

