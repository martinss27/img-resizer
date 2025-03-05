from PIL import Image


def image_resize(size1,size2):
    image = Image.open("python-logo.jpg")

    print(f'Current size: {image.size}')

    resized_image = image.resize((size1,size2))

    resized_image.save("python-logo-resized"+ str(size1) +".jpg")

size1 = int(input("Enter Widht: "))
size2 = int(input("Enter Length: "))

image_resize(size1, size2)