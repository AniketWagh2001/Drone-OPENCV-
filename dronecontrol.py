import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('OUTPUT.avi', fourcc, 20.0, (640, 480))
font = cv2.FONT_HERSHEY_SIMPLEX
while cap.isOpened():
    _, img = cap.read()

    #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    out.write(img)

    screencenter = (640//2, 480//2)

    cv2.circle(img, screencenter, 5, (0, 255, 0), 1)


    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        rectagleCenterPont = ((x + x + w) // 2, (y + y + h) // 2)
        cv2.circle(img, rectagleCenterPont, 5, (0, 0, 255), 1)
        x1 = (x + x + w) // 2
        y1 = (y + y + h) // 2
        x2 = 640//2
        y2 = 480//2

        dist = pow((((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1))), (1/2))
        text = 'Vector: ' + str(dist)
        cv2.putText(img, text, (10, 50), font, 1, (255, 255, 0), 2)
        #print(dist)S
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
