import cv2
import numpy as np
import mediapipe as mp

# Initialize the Mediapipe Face Mesh solution
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Open a video capture stream (you can also use a webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB (Mediapipe requires RGB input)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces and get landmarks
    results = face_mesh.process(rgb_frame)
    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            # Extract center from landmarks
            center_x = np.mean([lm.x for lm in landmarks.landmark[:68]])
            center_y = np.mean([lm.y for lm in landmarks.landmark[:68]])

            # Draw a circle at the center of the face
            cv2.circle(frame, (int(center_x * frame.shape[1]), int(center_y * frame.shape[0])), 3, (0, 0, 255), -1)


            print("x = {} , y =  {} ".format(str(center_x)[:4] ,str( center_y)[:4]))


    cv2.imshow('Face Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


"""
    Final remarks , very gucci 
    diff level 1/10
    experiment with landmarks

"""