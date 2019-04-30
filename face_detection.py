import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


vs = cv2.VideoCapture(0)


while True:

	ret, frame = vs.read()
  

	if frame is None:
		break
		
	faces = faceCascade.detectMultiScale(frame)

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
	
	
	cv2.imshow("Video", frame)
	key = cv2.waitKey(1) & 0xFF

	
	if key == ord("q"):
		break
 

cv2.destroyAllWindows()
