from PIL import Image, ImageFilter
img = Image.open('./auth.png')
fil_img = img.Filter(ImageFilter.Blur)
fil_img.save("blur.png", 'png')
img.show()
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))