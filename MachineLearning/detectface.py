import cv2
from PIL import Image


def detect_face(test):
	face_cascade = cv2.CascadeClassifier('dependencies/haarcascade_frontalface_default.xml')
	#image=Image.fromarray(test)
	#img = cv2.imread(image)

	gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	if len(faces)==0:
		
		return False
	else:
		
		return True
