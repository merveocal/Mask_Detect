import cv2 as cv

video = cv.VideoCapture(0)
cv.namedWindow("kamera", cv.WINDOW_NORMAL)
org = (30,30)
fontFace = cv.FONT_HERSHEY_SIMPLEX
fontScale = 1.0
weared_mask = "Thank you"
not_weared_mask = "Please wearing a mask"
face_detect = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
mouth_detect = cv.CascadeClassifier("haarcascade_mcs_mouth.xml")

while True:
    ret, frame = video.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = face_detect.detectMultiScale(gray,
                                         scaleFactor=1.3, 
                                         minNeighbors=5, #kaç kez doğrulama yapacak
                                         minSize=(15,15))
    if(len(faces) == 0):
        cv.putText(frame, "No face found", org, fontFace, fontScale, (255,0,0),3)
    else:
        for (x,y,w,h) in faces:
            cv.rectangle(frame, (x,y), (x+w, y+h),(125,12,255),3 )
            
            roi_gray = gray[y:y+h,x:x+w] # yüz üzerinde ağız arayacak, resimden bir bölgeyi kesme işlemi yapacak
            
            mouth = mouth_detect.detectMultiScale(roi_gray, 1.4,15) 
            i = 0
            if(len(mouth) == 0):
                cv.putText(frame, weared_mask ,org, fontFace, fontScale,(0,255,0),3, cv.LINE_AA)
            else:
                cv.putText(frame, not_weared_mask, org, fontFace, fontScale, (0,0,255),3, cv.LINE_AA)
                for mx, my, mw, mh in mouth:
                    if i == 0:
                        i += 1
                        cv.rectangle(frame, (mx+x,my+y), (mx+x+mw, my+y+mh), (0,0,255),3)
                    else:
                        pass

    cv.imshow("kamera", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        print("Görüntü sonlandırıldı")
        break

video.release()
cv.destroyAllWindows()