#
#   4번째 실습
#   opencv python 코딩
#   화면에 글자 출력 코드
# pillow라는 라이브러리가 필요합니다.
# datatime은 시간에 관련된 모듈
import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image # 영상에 글자를 입히는 모듈
import numpy as np # 넘파이는 필로우 사용할 때 필요해서 넣어둠

# opencv python 코딩 기본 틀
# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0) # 여기 칸에 0인지 1인지에 따라서 나오는 화면의 개수가 달라짐
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 글꼴파일을 불러옴
font = ImageFont.truetype('fonts/SCDream6.otf', 20) # 20은 글자크기임

# 무한루프
while True:
    # 현재시각을 불러와 문자열로저장
    now = datetime.datetime.now() # now라는 변수에 저장을 하는거임
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S') # 년도, 년월, 일 이런식으로 지정함
    # 그리고 시 분 초 이런식으로 작성을 함
    ret, frame = capture.read()     # 카메라로부터 현재 영상을 받아 frame에 저장, 잘 받았다면 ret가 참
    # 글자가 잘보이도록 배경을 넣어줌
    # img는 사각형을 넣을 이미지, pt1, pt2는 사각형의 시작점과 끝점, color는 색상(파랑,초록,빨강), tickness는 선굵기(-1은 내부를 채우는 것)
    cv2.rectangle(img=frame, pt1=(10, 15), pt2=(340, 35), color=(0,0,0), thickness=-1)     
    # pt1 어디서 시작할거냐, pt2 어디서 끝날거냐
    # 아래의 4줄은 글자를 영상에 더해주는 역할을 함    
    frame = Image.fromarray(frame)    # 33줄부터 37까지 글자를 입히는 과정임
    draw = ImageDraw.Draw(frame)    
    # xy는 텍스트 시작위치, text는 출력할 문자열, font는 글꼴, fill은 글자색(파랑,초록,빨강)   
    draw.text(xy=(10, 15),  text="박소이 웹캠 "+nowDatetime, font=font, fill=(255, 255, 255)) # nowDatertime을 해주면 문자열끼지 더해주는 것임
    frame = np.array(frame) #  fill=(255, 255, 255) fill은 글자의 색깔이고, 흰색을 사용하겠다는 뜻임
    cv2.imshow("text", frame)   # 현재 시간을 표시하는 글자를 써준 영상 출력
    if cv2.waitKey(1) == ord('q'):  # 키보드의 q 를 누르면 무한루프가 멈춤
            break
    # capture.release()                   # 캡처 객체를 없애줌
    
    # cv2.destroyAllWindows()             # 모든 영상 창을 닫아줌
