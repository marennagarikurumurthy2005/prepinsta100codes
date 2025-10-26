import qrcode


link='https://love-letter-jcbt.vercel.app/'


# Text you want to encode


# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border
)

qr.add_data(link)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("my_qrcode.png")

# Optional: Show the QR code
img.show()