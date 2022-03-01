import cv2

cap = cv2.VideoCapture(0)

while(True):
    rv, frame = cap.read()
    cv2.imshow('hoge', frame)
    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
