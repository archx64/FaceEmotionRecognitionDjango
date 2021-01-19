import dlib
import cv2

from deepface import DeepFace

detector = dlib.get_frontal_face_detector()


def classify_emotion(image, backend):
    x = 0
    y = 0
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    faces = detector(gray, 1)
    if len(faces) != 1:
        return [image, 'Cannot detect a face']

    else:
        predictions = DeepFace.analyze(image, detector_backend=backend, enforce_detection=False, actions=['emotion'])
        print(predictions)

        for face in faces:
            x, y = face.left(), face.top()
            w, h = face.right(), face.bottom()
            cv2.rectangle(image, (x, y), (w, h), (0, 255, 255), 5)

        emotion = predictions['dominant_emotion']
        # age = str(predictions['age'])
        # gender = predictions['gender']
        # race = predictions['dominant_race']
        # text = emotion + ', ' + age + ', ' + gender + ', ' + race
        text = emotion
        cv2.putText(image, text, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 5)
        return [image, text]
