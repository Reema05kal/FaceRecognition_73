import cv2

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

# Load face detection model
cascadePath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

# Names list
names = ['Unknown', 'Reema','Thensin','Shana']

# Start webcam
cam = cv2.VideoCapture(0)

print("Starting face recognition...")

while True:

    ret, img = cam.read()
    if not ret:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30,30),
    )

    for (x,y,w,h) in faces:

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        confidence_percent = round(100 - confidence)

        if confidence < 60:
            name = names[id]
            status = "Identity Verified"
            color = (0,255,0)
        else:
            name = "Unknown"
            status = "Identity Not Recognized"
            color = (0,0,255)

        # Draw face box
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)

        # Labels
        label1 = "Detected Face: " + name
        label2 = "Confidence Score: " + str(confidence_percent) + "%"
        label3 = "Status: " + status

        # Show text
        cv2.putText(img,label1,(x,y-40),font,0.6,(255,255,255),2)
        cv2.putText(img,label2,(x,y-20),font,0.6,(255,255,0),2)
        cv2.putText(img,label3,(x,y+h+20),font,0.6,(255,255,255),2)

    cv2.imshow('Real-Time Face Recognition System',img)

    # Press ESC to exit
    if cv2.waitKey(10) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()