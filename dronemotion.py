import cv2

cap = cv2.VideoCapture(0)

ret, frmae1= cap.read()
ret, frmae2= cap.read()


while cap.isOpened():
    diff = cv2.absdiff(frmae1, frmae2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
