
import io

import qrcode
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔳",
    layout="centered"
)

st.title("🔳 QR Code Generator")
st.write("Generate QR codes easily using Python and Streamlit.")

st.divider()

# User input
data = st.text_input(
    "Enter URL or Text",
    placeholder="https://github.com"
)

# Generate button
if st.button("Generate QR Code", type="primary"):
    if not data.strip():
        st.warning("Please enter a URL or text!")
    else:
        # Create QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        # Convert image to PNG bytes
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        image_bytes = buffer.getvalue()

        st.success("QR Code generated successfully!")

        # Display QR Code
        st.image(image_bytes, caption="Your QR Code", width=250)

        # Download button
        st.download_button(
            label="Download QR Code",
            data=image_bytes,
            file_name="qrcode.png",
            mime="image/png"
        )
