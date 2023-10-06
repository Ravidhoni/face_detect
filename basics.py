import cv2

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(r'C:\Users\talar_uxh3q0j\Downloads\haarcascade_frontalface_default.xml')

# Load an image or capture it from a camera
# Replace 'your_image.jpg' with the path to your image or 0 for camera capture
image = cv2.imread(r'C:\Users\talar_uxh3q0j\Downloads\WhatsApp Image 2023-06-07 at 13.51.00.jpg')
if image is not None :
    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    print("image not found !")
# Perform face detection
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with detected faces
cv2.imshow('Face Detection', image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
