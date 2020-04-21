import tkinter as tk
from tkinter import *


win = tk.Tk()
win.title(" Drone's Function")
win.geometry('640x420')

def face():
    import cv2

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('OUTPUT.avi', fourcc, 20.0, (640, 480))
    font = cv2.FONT_HERSHEY_SIMPLEX
    while cap.isOpened():
        _, img = cap.read()

        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        out.write(img)

        screencenter = (640 // 2, 480 // 2)

        cv2.circle(img, screencenter, 5, (0, 255, 0), 1)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            rectagleCenterPont = ((x + x + w) // 2, (y + y + h) // 2)
            cv2.circle(img, rectagleCenterPont, 5, (0, 0, 255), 1)
            x1 = (x + x + w) // 2
            y1 = (y + y + h) // 2
            x2 = 640 // 2
            y2 = 480 // 2
            z = (x + w * y + h) // 100
            dist = pow((((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))), (1 / 2))
            text = 'Vector: ' + str(dist)
            cv2.putText(img, text, (10, 25), font, 0.5, (255, 255, 0), 1)
            coordinates = 'X coordinates: ' + str(x1) + ' Y coordinates: ' + str(y1)
            zcoord = 'Z coordinate: ' + str(z)
            cv2.putText(img, coordinates, (10, 50), font, 0.5, (255, 255, 0), 1)
            cv2.putText(img, zcoord, (10, 75), font, 0.5, (255, 255, 0), 1)
            if (x1 <= 310):
                cmd1 = 'MOVE RIGHT:'
                cv2.putText(img, cmd1, (10, 90), font, 0.5, (0, 0, 255), 1)
            elif (x1 >= 330):
                cmd2 = 'MOVE LEFT: '
                cv2.putText(img, cmd2, (10, 90), font, 0.5, (0, 0, 255), 1)
            else:
                cmd3 = 'X AXIS ALLIEND'
                cv2.putText(img, cmd3, (10, 90), font, 0.5, (0, 0, 255), 1)

            if (y1 <= 230):
                cmd4 = 'MOVE DOWN:'
                cv2.putText(img, cmd4, (10, 105), font, 0.5, (0, 0, 255), 1)
            elif (y1 >= 260):
                cmd5 = 'MOVE UP: '
                cv2.putText(img, cmd5, (10, 105), font, 0.5, (0, 0, 255), 1)
            else:
                cmd6 = 'Y AXIS ALLIEND'
                cv2.putText(img, cmd6, (10, 105), font, 0.5, (0, 0, 255), 1)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

def motion():
    import cv2
    import numpy as np

    cap = cv2.VideoCapture(0)

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)

            # if cv2.contourArea(contour)< 700:
            # continue
            # cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.putText(frame1, 'Status: {}'.format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        ret, frame = cap.read()

        cv2.imshow("feed", frame1)
        frame1 = frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(40) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()


iface = PhotoImage(file="FaceTracklogo.png")
face = tk.Button(win, image=iface, command= face)
face.grid(row=0, column=0)

imotion = PhotoImage(file="motiontrackerlogo.png")
motion = tk.Button(win, image=imotion, command=motion)
motion.grid(row=0, column=1)

win.mainloop()