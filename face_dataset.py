import cv2
import os

# Load face detector
detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# Start webcam
cam = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cam.isOpened():
    print("Error: Cannot access the camera")
    exit()

face_id = input("Enter user ID: ")

print("Capturing face images. Look at the camera...")

count = 0

while True:

    ret, img = cam.read()

    # If frame not captured properly
    if not ret:
        print("Failed to grab frame from camera")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        count += 1

        # Save face image
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg",
                    gray[y:y+h,x:x+w])

        cv2.imshow('Face Capture', img)

    # Press ESC to stop
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

    # Stop after 30 images
    elif count >= 30:
        break

print("Face capture completed.")

cam.release()
cv2.destroyAllWindows()
