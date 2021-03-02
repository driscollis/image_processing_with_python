# eye_finder.py

import cv2
import os


def find_eyes(image_path):
    image = cv2.imread(image_path)

    # Make a copy to prevent us from modifying the original
    color_img = image.copy()

    filename = os.path.basename(image_path)

    # OpenCV works best with gray images
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    # Use OpenCV's built-in Haar classifier
    haar_classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

    faces = haar_classifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
    print("Number of faces found: {faces}".format(faces=len(faces)))

    for (x, y, width, height) in faces:
        cv2.rectangle(color_img, (x, y), (x + width, y + height), (0, 255, 0), 2)
        roi_gray = gray_img[y : y + height, x : x + width]
        roi_color = color_img[y : y + height, x : x + width]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Show the faces / eyes found
    cv2.imshow(filename, color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    find_eyes("author.jpg")
