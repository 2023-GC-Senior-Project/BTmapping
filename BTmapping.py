## Bluetooth
# currentTime yyyy-MM-dd HH:mm:ss
# deviceName Galaxy Watch5 (DH1H)
# mac_address 24:11:53:FF:38:54
# rssi -86
### deviceName, mac_address, rssi, currentTime

## MOT
# currentTime yyyy-MM-dd HH:mm:ss
# frameId 0
# objectId 1
# bboxX 648.90
# bboxY 272.70
# bboxW 118.80
# bboxH 234.45
# score 0.96
### frameId, objectId, bboxX, bboxY, bboxW, bboxH, score, currentTime

## Behavior
# currentTime yyyy-MM-dd HH:mm:ss
# frameId 0
# objectId 1
# behavior String
### frameId, objectId, behavior, currentTime

## BEV
# currentTime yyyy-MM-dd HH:mm:ss
# frameId 0
# objectId 1
# coordX 369.49
# coordY 212.90
# behavior String
### frameId, objectId, coordX, coordY, behavior, currentTime

###
## 블루투스 결과를 통해 MOT의 결과 값을 수정해야 함.
## 블루투스 rssi 값의 in: A, out: B라 가정.
## rssi값에 의해 arr에서 값 변경 (0,1,2) 0:out , 1:in , 2:in but not detect
## in out 은 무조건 rssi로 판단.
## in 이지만, MOT에서 객체가 줄어드는 경우 = 무언가에 가려져 있다 판단. arr[n]=2;
## 이후 내부에서 재 인식되는 객체는 기존의 블루투스와 연결.
###

### deviceName, mac_address, rssi, currentTime

# 1. mot 기준 탐지 객체의 수가 변화 된 경우 bluetooth 값 확인하여 id 배치 
# 인원은 총 5명이라 가정
# 

