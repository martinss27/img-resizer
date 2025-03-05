from PIL import Image
import os


def image_resize(width, height, input_path):
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return

    try:
        image = Image.open(input_path)
        print(f"Current size: {image.size}")

        resized_image = image.resize((width, height))

        file_name, ext = os.path.splitext(os.path.basename(input_path))
        output_path = f"{file_name}-resized-{width}x{height}{ext}"

        resized_image.save(output_path)
        print(f"Resized image saved ass '{output_path}'")

    except Exception as e:
        print(f"Error processing image: {e}")