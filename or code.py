import qrcode
import os

def generate_qr():
    # Take URL or text input from the user
    data = input("🔗 Enter the URL or text for the QR code: ").strip()
    
    if not data:
        print("❌ Error: Input cannot be empty.")
        return

    # Prompt for filename and ensure it ends with .png
    filename = input("💾 Save as (e.g., my_code): ").strip() or "qrcode"
    if not filename.lower().endswith(".png"):
        filename += ".png"

    # Set up the QR Code generator
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image object
    # Note: make_image() requires the Pillow library to save as PNG
    img = qr.make_image(fill_color="black", back_color="white")

    # Save to the current directory
    try:
        img.save(filename)
        # Verify file existence and location
        full_path = os.path.abspath(filename)
        print(f"\n✅ Success! PNG stored at: {full_path}")
    except Exception as e:
        print(f"❌ Failed to save PNG: {e}")

if __name__ == "__main__":
    generate_qr()

