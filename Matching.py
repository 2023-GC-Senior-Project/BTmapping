# MOT 파일에서 데이터를 읽어오는 함수
def read_mot_data(file_path):
    mot_data = {}  # objectId를 키로 사용하여 MOT 데이터를 저장할 딕셔너리
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            current_time, object_id, *rest = parts
            mot_data[object_id] = (current_time, *rest)  # objectId를 키로 사용하여 MOT 데이터 저장
    return mot_data

# BT 파일에서 데이터를 읽어오는 함수
def read_bt_data(file_path):
    bt_data = {}  # 시간대를 키로 사용하여 BT 데이터를 저장할 딕셔너리
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            current_time, device_name, mac_address, rssi = parts
            rssi = int(rssi)
            
            # 시간대를 키로 사용하여 BT 데이터 저장
            if current_time not in bt_data:
                bt_data[current_time] = {}
            
            # objectId와 rssi 값을 저장
            bt_data[current_time][mac_address] = {'device_name': device_name, 'rssi': rssi}
    return bt_data

# MOT 데이터와 BT 데이터를 조합하여 출력하고 저장하는 함수
def combine_and_print_data(trans_mot_data, trans_bt_data, output_file):
    with open(output_file, 'w') as file:
        for object_id, mot_data in trans_mot_data.items():
            current_time, *mot_rest = mot_data
            
            if current_time in trans_bt_data:
                bt_devices = trans_bt_data[current_time]
                matched_device_name = None
                max_rssi = -float('inf')
                
                for mac_address, bt_device_data in bt_devices.items():
                    rssi = bt_device_data['rssi']
                    device_name = bt_device_data['device_name']
                    
                    if rssi > max_rssi:
                        max_rssi = rssi
                        matched_device_name = device_name
                
                if matched_device_name:
                    output_line = f"Time: {current_time}, Object ID: {object_id}, Device Name: {matched_device_name}, RSSI: {max_rssi}"
                    print(output_line)
                    file.write(output_line + "\n")

if __name__ == "__main__":
    trans_mot_file_path = "./GuardianWatch/transMOT.txt"  # transMOT 파일 경로를 적절하게 수정하세요.
    trans_bt_file_path = "./GuardianWatch/transBT.txt"    # transBT 파일 경로를 적절하게 수정하세요.
    output_file_path = "./GuardianWatch/output.txt"       # 출력 파일 경로를 적절하게 수정하세요.
    
    trans_mot_data = read_mot_data(trans_mot_file_path)
    trans_bt_data = read_bt_data(trans_bt_file_path)
    
    combine_and_print_data(trans_mot_data, trans_bt_data, output_file_path)
