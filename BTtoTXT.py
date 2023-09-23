# 파일을 읽어오고 시간대별로 데이터를 그룹화하는 함수
def read_data_from_file(file_path):
    data_dict = {}  # 시간대별로 데이터를 그룹화한 딕셔너리
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            current_time, device_name, mac_address, rssi = parts
            rssi = int(rssi)  # rssi 값을 정수로 변환
            
            # 시간대를 키로 사용하여 데이터 그룹화
            if current_time not in data_dict:
                data_dict[current_time] = {}
            
            # deviceName을 키로 사용하여 rssi와 mac_address 갱신
            if device_name not in data_dict[current_time]:
                data_dict[current_time][device_name] = {'rssi': rssi, 'mac_address': mac_address}
            else:
                if rssi > data_dict[current_time][device_name]['rssi']:
                    data_dict[current_time][device_name]['rssi'] = rssi
                    data_dict[current_time][device_name]['mac_address'] = mac_address
    
    return data_dict

# 가장 큰 rssi와 mac_address 값을 출력 파일과 화면에 출력하는 함수
def save_max_rssi_and_mac_to_file_and_print(data_dict, output_file):
    with open(output_file, 'w') as file:
        for current_time, devices in data_dict.items():
            for device_name, data in devices.items():
                rssi = data['rssi']
                mac_address = data['mac_address']
                file.write(f"{current_time},{device_name},{mac_address},{rssi}\n")
                print(f"{current_time},{device_name},{mac_address},{rssi}")

if __name__ == "__main__":
    input_file_path = r"C:\Users\sts07\OneDrive\Desktop\Code\GuardianWatch\BT.txt"  # 입력 파일 경로를 적절하게 수정하세요.
    output_file_path = './GuardianWatch/transBT.txt' # 출력 파일 경로를 적절하게 수정하세요.
    data_dict = read_data_from_file(input_file_path)
    save_max_rssi_and_mac_to_file_and_print(data_dict, output_file_path)
