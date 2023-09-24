import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일에서 데이터를 읽어옴
df = pd.read_csv(r'BTmapping\transMOT.txt', parse_dates=['first', 'last'])

# 각 objectId에 대해 그래프 그리기
plt.figure(figsize=(12, 6))
for _, row in df.iterrows():
    objectId = row['objectId']
    first_time = row['first']
    last_time = row['last']
    plt.plot([first_time, last_time], [objectId, objectId], marker='o', label=f'objectId {objectId}')

# 그래프 설정
plt.xlabel('Time')
plt.ylabel('objectId')
plt.title('First and Last Timestamps for Each objectId')
plt.legend()

# 그래프 저장 또는 표시
#plt.savefig('timestamp_graph.png')
plt.show()
