import cv2
import mediapipe as mp
mphands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils

hand = mphands.Hands(max_num_hands=1)

video = cv2.VideoCapture(0)
while True:
    suc, img = video.read()
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = hand.process(img1)
    #print(res.multi_hand_landmarks)
    tipid = [4, 8, 12, 16, 20]
    lmlist = [] # Fingertip landmark IDs

    if res.multi_hand_landmarks:
        for handLms in res.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                cx = lm.x
                cy = lm.y
                lmlist.append([id, cx, cy])

            if len(lmlist)!=0 and len(lmlist) == 21:
                fingersList = []
                if lmlist[12][1]<lmlist[20][1]:
                    if lmlist[4][1]>lmlist[3][1]:
                        fingersList.append(0)
                    else:
                        fingersList.append(1)
                else:
                    if lmlist[4][1]<lmlist[3][1]:
                        fingersList.append(0)
                    else:
                        fingersList.append(1)
                
                for i in range(1,5):#all finger except thumb
                    if lmlist[tipid[i]][2] > lmlist[tipid[i] - 2][2]:  # If y of tip < y of lower joint
                        fingersList.append(0)
                    else:
                        fingersList.append(1)
                gesture = "Unknown"
                if fingersList == [0, 0, 0, 0, 0]:
                    gesture = "closed"
                elif fingersList == [1, 1, 1, 1, 1]:
                    gesture = "Open Palm"
                elif fingersList == [0, 1, 0, 0, 0]:
                    gesture = "Index Finger"
                elif fingersList == [0, 1, 1, 0, 0]:
                    gesture = "Peace"
                elif fingersList == [1, 1, 0, 0, 0]:
                    gesture = "Gun"
                elif fingersList == [1, 0, 0, 0, 1]:
                    gesture = "Rock"
                elif fingersList == [0, 1, 1, 1, 1]:
                    gesture = "Four"
                elif fingersList == [1, 0, 0, 0, 0]:
                    gesture = "Thumbs Up"
                elif fingersList ==[1, 1, 0, 0, 1]:
                    gesture = "I Love You"
                elif fingersList == [1, 0, 1, 1, 1]:
                    gesture = "Super"
                elif fingersList == [0, 1, 0, 0, 1]:
                    gesture = "Spider-Man "        

                print(fingersList)
                if len(fingersList)!=0:
                    fingercount=fingersList.count(1)
                print(fingercount)
                cv2.putText(img,"count "+ str(fingercount), (35, 425), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
                cv2.putText(img, gesture, (35, 400), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            mpdraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()