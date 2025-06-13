import cv2
import numpy as np



person1 = cv2.imread("images/exau.jpeg")
person2 = cv2.imread("images/lui.jpeg")


gray_person1 = cv2.cvtColor(person1, cv2.COLOR_BGR2GRAY)
gray_person2 = cv2.cvtColor(person2, cv2.COLOR_BGR2GRAY)


face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face1 = face_detector.detectMultiScale(gray_person1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
face2 = face_detector.detectMultiScale(gray_person2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


video_capture = cv2.VideoCapture(0)

while True:
    
    ret, frame = video_capture.read()

    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    
    for (x, y, w, h) in faces:
       
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        
        if len(face1) > 0 and len(face2) > 0:
            if np.array_equal(gray_frame[y:y + h, x:x + w], gray_person1):
                cv2.putText(frame, "Personne 1", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)
            elif np.array_equal(gray_frame[y:y + h, x:x + w], gray_person2):
                cv2.putText(frame, "Personne 2", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)
            else:
                cv2.putText(frame, "Inconnu", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)

    
    cv2.imshow('reconnaissance faciale', frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()