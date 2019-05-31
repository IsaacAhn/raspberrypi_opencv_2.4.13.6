import cv2
import numpy as np

#video_file = "video_1.mp4"
video = cv2.imread('firetest.jpg', cv2.IMREAD_COLOR)

while True:
#	(grabbed, frame) = video.read()
#	if not grabbed:
#		break

	cv2.imshow('input', video)
	blur = cv2.GaussianBlur(video, (21, 21), 0)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

	lower = [18, 50, 50]
	upper = [35, 255, 255]
	lower = np.array(lower, dtype="uint8")
	upper = np.array(upper, dtype="uint8")
	mask = cv2.inRange(hsv, lower, upper)

	output = cv2.bitwise_and(video, hsv, mask=mask)
	no_red = cv2.countNonZero(mask)
	cv2.imshow("output", output)
	#print("output: ", frame)
	if int(no_red) > 20000:
		print('Fire Detected')
	#print(int(no_red))
       #print("output: ".format(mask))
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
video.release()
