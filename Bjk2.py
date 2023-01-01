from PIL import Image

def compress(input_file: str, output_file: str) -> None:
    # Read the input file into memory as a bytestring
    with open(input_file, "rb") as f:
        data = f.read()

    # Compress the bytestring into a JPEG image
    image = Image.frombytes("RGB", (1, 1), data)
    image = image.resize((100, 100))  # Increase the size of the image to improve compression
    image.save(output_file, "JPEG", quality=95)

def decompress(input_file: str, output_file: str) -> None:
    # Load the image file into memory
    image = Image.open(input_file)

    # Decode the image and recover the original bytestring
    data = image.tobytes()

    # Write the recovered bytestring to a new file
    with open(output_file, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    # Compress the file
    compress("input.txt", "output.jpg")

    # Decompress the file
    decompress("output.jpg", "recovered.txt")
