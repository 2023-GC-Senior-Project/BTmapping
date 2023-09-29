import pandas as pd

input_file =r'BTmapping\transBT.txt'
output_file=r"BTmapping\transBT_modified.txt"

# 파일을 읽어 DataFrame으로 변환
data = pd.read_csv(input_file, header=None, names=['time', 'deviceName', 'mac', 'rssi'], skiprows=1)

# rssi 값을 기반으로 value 열 추가
def classify_rssi(rssi):
    rssi=int(rssi)
    if rssi >= -90:
        return 'in'
    elif rssi <= -100:
        return 'out'
    else:
        return None

data['value'] = data['rssi'].apply(classify_rssi)

# 이전 시간과 rssi 값을 기반으로 was_in과 was_out 열 추가
data['prev_value'] = data.groupby('deviceName')['value'].shift(1)
data['was_in'] = (data['value'] == 'in') & (data['prev_value'] == 'in')
data['was_out'] = (data['value'] == 'out') & (data['prev_value'] == 'out')

# was_in 값이 True이면 value 값을 'was_in'으로 저장
data.loc[data['was_in'], 'value'] = 'was_in'

# was_out 값이 True이면 value 값을 'was_out'으로 저장
data.loc[data['was_out'], 'value'] = 'was_out'


# 결과를 새로운 파일에 저장
data.to_csv(output_file, index=False, header=None, columns=['time', 'deviceName', 'mac', 'rssi', 'value'])
