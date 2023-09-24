import pandas as pd

# CSV 파일을 DataFrame으로 읽기
df = pd.read_csv(r'BTmapping\transMOT.txt')

# 시간 형식을 datetime으로 변환
df['first'] = pd.to_datetime(df['first'])
df['last'] = pd.to_datetime(df['last'])

# start와 end 계산
start = df['first'].min()
end = df['last'].max()

# start와 end가 아닌 objectId 찾기
invalid_start = df[df['first'] != start]
invalid_end = df[df['last'] != end]

# 결과를 저장할 파일명 지정
output_filename = r'./BTmapping/checkBT.txt'

# 결과를 저장할 문자열 초기화
result = ""

if not invalid_start.empty:
    result += "objectId,first\n"
    result += invalid_start[['objectId', 'first']].to_csv(index=False, header=False)

if not invalid_end.empty:
    result += "objectId,last\n"
    result += invalid_end[['objectId', 'last']].to_csv(index=False, header=False)

# 빈 줄 제거
result = "\n".join([line for line in result.splitlines() if line.strip()])

# 결과를 파일로 저장
with open(output_filename, 'w') as output_file:
    output_file.write(result)
