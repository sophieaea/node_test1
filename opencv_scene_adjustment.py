#
#  
#   opencv python 코딩
#   영상 조정 코드
#

import cv2
import numpy as np



# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()     # 카메라로부터 영상을 받아 frame에 저장
    cv2.imshow("original", frame)   # 원본 영상 출력
    filered = color_filter(frame, 'red', 1.2)   # 원본영상에서 빨간색을 강조 즉, 1.2배만큼 빨간색을 바꿔준 것이다.
    cv2.imshow("red", filered)      # 색감을 바꾼 영상 출력
    brightness = set_brightness(frame, 20)  # 밝기를 전체적으로 20픽셀 밝게 해줌
    cv2.imshow("brightness", brightness)    # 밝기를 바꾼 영상 출력
    constrast = set_contrast(frame, 0.9)    # 대비를 0.9만큼 변경 -> contrast의 경우 1이 가장 큰 값이라서 1이하의 값을 넣어야함
    cv2.imshow("constrast", constrast)      # 대비를 바꾼 영상 출력
    big_size = set_size(frame, 2)    # 대비를 0.9만큼 변경
    cv2.imshow("big_size", big_size)      # 대비를 바꾼 영상 출력 -> 해상도가 좋아지는게 아니고, 화면 크기만 키운거라서 계단 현상이 나타남
    if cv2.waitKey(1) == ord('q'): # if cv2.waitKey(1)==ord('q): 1ms 동안 키입력을 기다리고, 입력키가 q이면 특히 무한루프 나옴 0이면 무한히 대기 중
            break

capture.release()
cv2.destroyAllWindows()