import cv2
import mediapipe as mp

# Initialize the Mediapipe Hand solution
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open a video capture stream (you can also use a video file)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB (Mediapipe requires RGB input)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands in the frame
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            for landmark in landmarks.landmark:
                # Get pixel coordinates
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])

                # Draw a circle at the landmark position
                cv2.circle(frame, (x, y), 5, (255, 255, 0), -1)


    cv2.imshow('Hand Gesture Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
