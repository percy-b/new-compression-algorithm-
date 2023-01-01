import io
import pyqrcode
from PIL import Image

BLOCK_SIZE = 1024  # Number of bytes per block

def compress(input_file: str, output_file: str) -> None:
    # Read the input file into memory
    with open(input_file, "rb") as f:
        data = f.read()

    # Split the data into blocks
    blocks = [data[i:i+BLOCK_SIZE] for i in range(0, len(data), BLOCK_SIZE)]

    # Calculate the size of the image we need to create
    image_size = (len(blocks) * 100, 100)  # 100 pixels per block
    image = Image.new("RGB", image_size)

    # Iterate over the blocks and draw a QR code for each one on the image
    for i, block in enumerate(blocks):
        # Encode the block as a hexadecimal string
        hex_string = block.hex()

        # Generate a QR code for the hex string
        qr = pyqrcode.create(hex_string)

        # Convert the QR code to a Pillow image
        qr_image = qr.png_as_pil()

        # Calculate the position to draw the QR code on the image
        x = i * 100
        y = 0
        image.paste(qr_image, (x, y))

    # Save the image to disk
    image.save(output_file)

def decompress(input_file: str, output_file: str) -> None:
    # Load the image file into memory
    image = Image.open(input_file)

    # Calculate the size of the image
    width, height = image.size

    # Calculate the number of blocks in the image
    num_blocks = width // 100

    # Initialize an empty list to hold the recovered blocks of data
    blocks = []

    # Iterate over the blocks in the image and recover the original data
    for i in range(num_blocks):
        # Calculate the position of the QR code on the image
        x = i * 100
        y = 0

        # Crop the image to just the QR code
        qr_image = image.crop((x, y, x+100, y+100))

        # Convert the QR code image to a byte stream
        qr_bytes = io.BytesIO()
        qr_image.save(qr_bytes, format="PNG")
        qr_bytes.seek(0)

        # Decode the QR code to recover the original hex string
        qr = pyqrcode.decode(qr_bytes)
        hex_string = qr.data.decode("utf-8")

        # Convert the hex string back into binary data
        block = bytes.fromhex(hex_string)

        # Add the recovered block to the list of blocks
        blocks.append(block)

    # Concatenate the blocks to form the original data
    data = b"".join(blocks)

    # Write the recovered data to a new file
    with open(output_file, "wb") as f:
        f.write(data)

#complete the if __name__ 
