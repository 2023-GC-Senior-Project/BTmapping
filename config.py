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

######
# 1.BTtoTXT.py : BT.txt -> transBT.txt

# 2.newMOTtoTXT.py : 2023_09_23_09_02_19.txt -> transMOT.txt

# 3.MOTbetween.py : transMOT.txt -> MOTbetween.txt
#   3.1 viewMOT.py : view MOTbetween with graph
#   3.2 transBT_modify.py : transBT.txt -> transBT_modified.txt

# 4.mapping.py :  MOTbetween + transBT_modified-> mapping.txt
