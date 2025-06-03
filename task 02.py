from PIL import Image

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)  # XOR operation for encryption

    image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, key)  # XOR reverses itself

# Example usage
key = 42  # Encryption key
encrypt_image("input.jpg", "encrypted.jpg", key)
decrypt_image("encrypted.jpg", "decrypted.jpg", key)
