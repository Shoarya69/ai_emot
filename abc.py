import cv2
from deepface import DeepFace
from ai_face_persona.cam import ip
cap = cv2.VideoCapture(ip())

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        print("Emotion:", emotion)

        cv2.putText(frame, emotion, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    except Exception as e:
        print("Error:", e)

    cv2.imshow("Emotion Detector", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
