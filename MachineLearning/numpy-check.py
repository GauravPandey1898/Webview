from PIL import Image
from detectface import detect_face
from numpy import asarray

image=Image.open('face-1.jpeg')
data=asarray(image)

print(detect_face(data))