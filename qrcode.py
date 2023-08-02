import os
import qrcode

def create_qr_code(link, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    input_file = "link.txt" #ubah link nya tod
    output_folder = "gambar" #ubah nama folder nya tod

    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file, "r") as file:
        links = file.readlines()

    for i, link in enumerate(links):
        link = link.strip()  
        filename = os.path.join(output_folder, f"qrcode_{i + 1}.png")
        create_qr_code(link, filename)
        print(f"QR code {filename} has been created for link: {link}")

if __name__ == "__main__":
    main()
