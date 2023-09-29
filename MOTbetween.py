# 입력 파일 이름과 출력 파일 이름 설정
input_file = r"BTmapping\transMOT.txt"
output_file = r"BTmapping\MOTbetween.txt"

# 입력 파일 열기
with open(input_file, "r") as f:
    lines = f.readlines()

# 출력 파일 열기
with open(output_file, "w") as f:
    # 헤더 쓰기
    f.write("objectId,time,value\n")

    # 각 줄을 파싱하고 변환하여 출력 파일에 쓰기
    for line in lines[1:]:  # 첫 번째 줄은 헤더이므로 건너뜁니다.
        parts = line.strip().split(',')
        objectId = parts[0]
        first_time = parts[1]
        last_time = parts[2]

        # objectId, 시간 및 value를 출력 파일에 쓰기
        f.write(f"{objectId},{first_time},first\n")
        f.write(f"{objectId},{last_time},last\n")


# 입력 파일 열기
with open(output_file, "r") as f:
    lines = f.readlines()

# 헤더를 제외한 데이터 정렬
sorted_lines = sorted(lines[1:], key=lambda line: line.split(',')[1])

# 출력 파일 열기
with open(output_file, "w") as f:
    # 헤더 쓰기
    f.write(lines[0])

    # 정렬된 데이터 쓰기
    for line in sorted_lines:
        f.write(line)
