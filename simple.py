import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('frame', frame)