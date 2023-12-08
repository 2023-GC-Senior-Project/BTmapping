# 1 = 인재, 2 = 지우, 3 = 정곤, 4 = 지성, 5 = 태경
# 13 = 지성, 14 = 정곤, 16 = 인재, 19 = 지성, 22, 24, 25 = 지성

## 인재 = 1, 16
## 지우 = 2
## 정곤 = 3, 14
## 지성 = 4, 13, 19, 22, 24, 25
## 태경 = 5
### 16, 2, 14, 25, 5

# objectId  deviceName 
#        1           1
#        2           2
#        3           3
#        4           4
#        5           5
#        13          4
#        14          3
#        16          1
#        19          4
#        22          4
#        25          4

#초기 가정 : 인원을 알고 있다고 가정
#그냥 transMOT.txt에서 ojectId별로 정렬 후, 그 순서대로 인원만큼 블루투스 와 매핑
## 그러면 초기 5명은 1,2,3,4,5에 매핑될것임.
#그 이후 부터 checkBT.txt에 있는 기록을 기준으로 확인하여 판단
## 판단 기준 : rssi가 나갔으면 그냥 나간거지만, rssi는 안에 있는데 id가 사라지면 특수 상황으로 가정.
## 특수상황에서는 이후에 새 id가 탐지되며 다른 인원들 rssi에 큰 변화가 없는 경우
## 기존의 id와 매핑
## 사실 bbox를 통해 검증을 해야하지만 우선적으로 진행하자.....
## 새 id가 탐지되며 rssi가 변화가 있는 경우는 그대로 매핑

import csv
# 데이터를 저장할 딕셔너리 초기화
mapping = {}
max_last_times = {}

# MOTbetween.txt 파일 읽기
with open(r'BTmapping/MOTbetween.txt', mode='r') as mot_file:
    mot_reader = csv.DictReader(mot_file, delimiter=',')
    for row in mot_reader:
        object_id = int(row['objectId'])
        time = row['time']
        value = row['value']
        
        # value가 'first'인 경우 매핑
        if value == 'first':
            # 이미 매핑된 objectId가 아니라면
            if object_id not in mapping:
                mapping[object_id] = {'first': time, 'deviceName': None}
        else:
            mapping[object_id]['last'] = time

# transBT_modified.txt 파일 읽기
with open(r'BTmapping/transBT_modified.txt', mode='r') as trans_file:
    for line in trans_file:
        fields = line.strip().split(',')
        time = fields[0]
        device_name = fields[1]
        mac = fields[2]
        rssi = fields[3]
        value = fields[4]
        
        # value가 'in'이고, 해당 시간의 objectId가 매핑되지 않았다면
        if value == 'in' and time in [mapping[obj]['first'] for obj in mapping if mapping[obj]['deviceName'] is None]:
            for object_id in mapping:
                if mapping[object_id]['first'] == time and mapping[object_id]['deviceName'] is None:
                    mapping[object_id]['deviceName'] = device_name
                    max_last_times[device_name] = mapping[object_id]['last']
                    break

# Iterate through the mapping dictionary again and update deviceName for objects with None
for obj, data in mapping.items():
    device_name = data['deviceName']
    first_time = data['first']
    last_time = data['last']
    
    # Check if deviceName is None, and the object's first time is smaller than the maximum last time
    if device_name is None:
        filter_max = [key for key, value in max_last_times.items() if value < first_time]
        # Update deviceName with the deviceName of the object with the largest last time
        data['deviceName'] = max(filter_max)
        max_last_times[data['deviceName']] =  last_time = data['last']

final_mapping = {}     
# 결과 출력
for obj in mapping:
    print(f"ObjectId {obj}: DeviceName {mapping[obj]['deviceName']}")
    final_mapping[obj] = mapping[obj]['deviceName']

# 딕셔너리를 텍스트 파일에 저장
with open(r'BTmapping/mapping.txt', 'w') as txt_file:
    for key, value in final_mapping.items():
        txt_file.write(f"{key},{value}\n")