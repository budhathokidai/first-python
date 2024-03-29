import qrcode

# Function to generate QR code with a given URL and save it as PNG image
def generate_qr_code(url, filename):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    # Create and save QR code image as PNG
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)  # Save as PNG

# Example usage:
if __name__ == "__main__":
    url = "https://sites.google.com/view/free-happy/home?authuser=1"  # Your URL here
    filename = "example_qrcode.png" 
    text = "Scan Me" # Output filename
    generate_qr_code(url, filename)
    print(f"QR code saved as {filename}")
   
