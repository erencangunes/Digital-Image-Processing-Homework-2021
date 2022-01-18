
from PIL import Image
from PIL import ImageFilter
img=Image.open("picasso.png")

resized_img = Image.Image.resize(img,(256,256))
resized_img.show()

filtered_img = Image.Image.filter(img,ImageFilter.GaussianBlur(0.8))
filtered_img.show()

Image.Image.save(resized_img,"picassoresized.png")
Image.Image.save(filtered_img,"picassoblurred.png")

