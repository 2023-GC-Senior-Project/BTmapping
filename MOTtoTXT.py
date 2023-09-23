# 파일을 읽어오고 줄 단위로 데이터를 처리하기 위한 함수
def read_data_from_file(file_path):
    data_dict = {}  # 시간대별로 데이터를 저장할 딕셔너리
    with open(file_path, 'r') as file:
        for line in file:
            # 각 줄을 쉼표로 분리하여 필요한 정보를 추출
            parts = line.strip().split(',')
            frame_id, object_id, bbox_x, bbox_y, bbox_w, bbox_h, score, current_time = parts[:8]
            
            # 시간대를 키로 사용하여 데이터 저장
            if current_time not in data_dict:
                data_dict[current_time] = {}
            
            # objectId를 키로 사용하여 해당 objectId의 데이터 갱신
            data_dict[current_time][object_id] = (bbox_x, bbox_y, bbox_w, bbox_h, score)
    
    return data_dict

# 가장 마지막 objectId의 데이터를 출력하는 함수
def print_last_object_data(data_dict):
    for current_time, objects in data_dict.items():
        #print("Time:", current_time)
        for object_id, object_data in objects.items():
            bbox_x, bbox_y, bbox_w, bbox_h, score = object_data
            object_id=int(object_id)
            bbox_x=float(bbox_x)
            bbox_y=float(bbox_y)
            print(f"{current_time},{object_id},{bbox_x},{bbox_y}")
        print()

# 가장 마지막 objectId의 데이터를 텍스트 파일로 저장하는 함수
def save_last_object_data_to_file(data_dict, output_file):
    with open(output_file, 'w') as file:
        for current_time, objects in data_dict.items():
            for object_id, object_data in objects.items():
                bbox_x, bbox_y, bbox_w, bbox_h, score = object_data
                file.write(f"{current_time},{object_id},{bbox_x},{bbox_y}\n")

if __name__ == "__main__":
    file_path = r"BTmapping\2023_09_23_09_02_19.txt"  # 파일 경로를 적절하게 수정하세요.
    data_dict = read_data_from_file(file_path)
    print_last_object_data(data_dict)
    save_last_object_data_to_file(data_dict, './BTmapping/transMOT.txt')
