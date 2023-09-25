# 1 = 인재, 2 = 지우, 3 = 정곤, 4 = 지성, 5 = 태경
# 13 = 지성, 14 = 정곤, 16 = 인재, 19 = 지성, 22, 24, 25 = 지성

## 인재 = 1, 16
## 지우 = 2
## 정곤 = 3, 14
## 지성 = 4, 13, 19, 22, 24, 25
## 태경 = 5
### 16, 2, 14, 25, 5

#초기 가정 : 인원을 알고 있다고 가정
#그냥 transMOT.txt에서 ojectId별로 정렬 후, 그 순서대로 인원만큼 블루투스 와 매핑
## 그러면 초기 5명은 1,2,3,4,5에 매핑될것임.
#그 이후 부터 checkBT.txt에 있는 기록을 기준으로 확인하여 판단
## 판단 기준 : rssi가 나갔으면 그냥 나간거지만, rssi는 안에 있는데 id가 사라지면 특수 상황으로 가정.
## 특수상황에서는 이후에 새 id가 탐지되며 다른 인원들 rssi에 큰 변화가 없는 경우
## 기존의 id와 매핑
## 사실 bbox를 통해 검증을 해야하지만 우선적으로 진행하자.....
## 새 id가 탐지되며 rssi가 변화가 있는 경우는 그대로 매핑

import pandas as pd
import numpy as np

# 파일 경로 설정
transMOT_file = r'BTmapping/transMOT.txt'
transBT_file = r'BTmapping/transBT.txt'
MOTbetween_file = r'BTmapping/MOTbetween.txt'

# transMOT 파일 읽기
transMOT_df = pd.read_csv(transMOT_file)
# transBT 파일 읽기
transBT_df = pd.read_csv(transBT_file)
# MOTbetween 파일 읽기
MOTbetween_df = pd.read_csv(MOTbetween_file)

# 초기 objectId와 device_name 매핑
initial_mapping = {}
for i in range(5):
    first_time = transMOT_df.at[i, 'first']
    device_name = transBT_df[(transBT_df['time'] == first_time) & (transBT_df['rssi'] == transBT_df[(transBT_df['time'] == first_time)]['rssi'].max())]['device_name'].values[0]
    initial_mapping[transMOT_df.at[i, 'objectId']] = device_name

# objectId 변형 관리
next_objectId = 6

# objectId와 device_name 매핑 함수
def map_objectId(first_time, rssi):
    global next_objectId
    
    # MOTbetween 파일에서 rssi가 -90 이상인 경우 objectId 매핑
    matching_rows = MOTbetween_df[(MOTbetween_df['first'] == first_time) & (rssi >= -90)]
    
    if not matching_rows.empty:
        return matching_rows['objectId'].values[0]
    
    # MOTbetween 파일에서 rssi가 -100 이하인 경우 objectId 매핑
    matching_rows = MOTbetween_df[(MOTbetween_df['first'] == first_time) & (rssi <= -100)]
    
    if not matching_rows.empty:
        return matching_rows['objectId'].values[0]
    
    # 매칭되는 objectId가 없을 경우 새로운 objectId 생성
    new_objectId = next_objectId
    next_objectId += 1
    return new_objectId

# objectId와 device_name을 매핑하여 결과 파일에 저장
result_mapping = {}
for index, row in transMOT_df.iterrows():
    first_time = row['first']
    rssi = transBT_df[(transBT_df['time'] == first_time)]['rssi'].max()
    
    if row['objectId'] in initial_mapping:
        device_name = initial_mapping[row['objectId']]
    else:
        device_name = map_objectId(first_time, rssi)
    
    result_mapping[row['objectId']] = device_name

# 결과를 mapping.txt 파일에 저장
with open(r'BTmapping/mapping.txt', 'w') as f:
    for objectId, device_name in result_mapping.items():
        f.write(f'{objectId},{device_name}\n')
