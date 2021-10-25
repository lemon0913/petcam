#   opencv python 코딩
#   얼굴을 인식한 상태에만 자동으로 촬영
#

import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os
import datetime
import requests as req
import time
# opencv python 코딩 기본 틀
# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(1) #카메라 선택
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

is_record = False                           # 녹화상태는 처음엔 거짓으로 설정
on_record = False
cnt_record = 10      # 영상 녹화 시간 관련 변수
max_cnt_record =100  # 최소 촬영시간

fourcc = cv2.VideoWriter_fourcc(*'H264')    # 영상을 기록할 코덱 설정
font = ImageFont.truetype('fonts/SCDream6.otf', 20) # 글꼴파일을 불러옴

# haar cascade 검출기 객체 선언
#face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml') #사람얼굴
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalcatface.xml') #고양이얼굴

video_url= 'http://192.168.0.6:8000/api/video/'
username ='hong'
file_name =''    #비디오명
file_path = '' #비디오경로
#nowDatetime_path =''
# 무한루프
while True:
    # 현재시각을 불러와 문자열로저장
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    nowDatetime_path = now.strftime('%Y-%m-%d %H_%M_%S') # 파일이름으로는 :를 못쓰기 때문에 따로 만들어줌
    ret, frame = capture.read()     # 카메라로부터 현재 영상을 받아 frame에 저장, 잘 받았다면 ret가 참
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 영상을 흑백으로 바꿔줌
    
    # 글자가 잘보이도록 배경을 넣어줌
    # img는 사각형을 넣을 이미지, pt1, pt2는 사각형의 시작점과 끝점, color는 색상(파랑,초록,빨강), tickness는 선굵기(-1은 내부를 채우는 것)
    cv2.rectangle(img=frame, pt1=(10, 15), pt2=(340, 35), color=(0,0,0), thickness=-1)     
    frame = Image.fromarray(frame)    
    draw = ImageDraw.Draw(frame)    
    # xy는 텍스트 시작위치, text는 출력할 문자열, font는 글꼴, fill은 글자색(파랑,초록,빨강)   
    draw.text(xy=(10, 15),  text="PETCAM "+nowDatetime, font=font, fill=(255, 255, 255))
    frame = np.array(frame)
    
    # scaleFactor를 1에 가깝게 해주면 정확도가 상승하나 시간이 오래걸림
    # minNeighbors를 높여주면 검출률이 상승하나 오탐지율도 상승
    faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.5, minNeighbors=3, minSize=(20,20))
    # print(faces)
    
    # 찾은 얼굴이 있으면
    if len(faces) :
        is_record = True    # 녹화 준비
        if on_record == False:
            video = cv2.VideoWriter("media/video/PETCAM " + nowDatetime_path + ".mp4", fourcc, 15, (frame.shape[1], frame.shape[0]))
            video_path="media/video/PETCAM " + nowDatetime_path + ".mp4"
            file_name = "PETCAM "+nowDatetime_path+".mp4"
            file_path = os.path.join('./media/video', file_name) 

        cnt_record = max_cnt_record
        
    if is_record == True:   # 녹화중이면
        print('녹화 중')
        video.write(frame)    # 현재 프레임 저장
        cnt_record -= 1     # 녹화시간 1 감소
        on_record = True    # 녹화중 여부를 참으로
        cv2.circle(img=frame, center=(620, 15), radius=5, color=(0,0,255), thickness=-1)


        # cv2.circle => 녹화중이라는 것을 보여주기 위해 보여주는 화면에는 빨간색 점을 표시해줌
    if cnt_record == 0:     # 녹화시간이 다 되면
        print('______________________________')
        print('녹화 완료')
        is_record = False   # 녹화관련 변수들을 거짓으로
        on_record = False
        video.release()
        #capture.release()
        # video_path="media/video/PETCAM " + nowDatetime_path + ".mp4"
        # file_name = "PETCAM "+nowDatetime_path+".mp4"
        # file_path = os.path.join('./media/video', file_name) 
        data = {
                'username': username,
                'size': os.path.getsize(file_path),
                'filename': file_name,
                'content_type': 'video/mp4'
        }
        #time.sleep(5)
        jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InBhcmsiLCJleHAiOjE2MzU0OTM2OTMsImVtYWlsIjoiZXdmYUBhZmV3ZmEuYWVmYWYiLCJvcmlnX2lhdCI6MTYzNDg4ODg5M30.g3lBOfnDrTsIe7I0Ustl2eYUmZHmPEcXKN6izHFN6a8'
        headers = {
            'Authorization' : f'jwt {jwt}'
        }
        res= req.post(video_url, data=data, headers=headers, files={'video_file': open(file_path, 'br')})
        cnt_record = 10
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.text)
    
    # 얼굴 영역을 영상에 사각형으로 표시
    if len(faces) :
        for  x, y, w, h in faces :
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,255,255), 2, cv2.LINE_4)
    cv2.imshow("PETCAM", frame)   # frame(카메라 영상)을 original 이라는 창에 띄워줌 
    if cv2.waitKey(1) == ord('q'):  # 키보드의 q 를 누르면 무한루프가 멈춤
            break

capture.release()                   # 캡처 객체를 없애줌
cv2.destroyAllWindows()             # 모든 영상 창을 닫아줌