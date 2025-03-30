# Mars_Base_Inventory_List.csv 파일을 읽어 리스트 객체로 변환하고, 
# 인화성 지수가 0.7 이상인 항목을 출력하고 CSV로 저장하는 스크립트

def read_csv(file_path):
    '''CSV 파일을 읽고 내용을 리스트로 반환'''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip().split(',') for line in lines]
    except FileNotFoundError:
        print(f"Error: 파일 '{file_path}'을 찾을 수 없습니다.")
    except PermissionError:
        print(f"Error: 파일 '{file_path}'에 대한 접근 권한이 없습니다.")
    except Exception as error:
        print(f"Error: 파일을 읽는 중 예외 발생 - {error}")
    return []

def sort_inventory_by_flammability(inventory_list):
    '''인화성 지수에 따라 화물 목록을 정렬'''
    return sorted(inventory_list, key=lambda x: float(x[4]), reverse=True)

def filter_high_flammability(inventory_list):
    '''인화성 지수가 0.7 이상인 항목을 필터링'''
    return [item for item in inventory_list if float(item[4]) >= 0.7]

def save_to_csv(data, file_path):
    '''리스트 데이터를 CSV 포맷으로 저장'''
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data:
                file.write(','.join(item) + '\n')
        print(f"CSV 데이터가 '{file_path}' 파일로 저장되었습니다.")
    except Exception as error:
        print(f"Error: CSV 저장 중 예외 발생 - {error}")

def main():
    '''주요 작업 흐름'''
    # 파일 경로 설정
    csv_file = 'Mars_Base_Inventory_List.csv'  # 입력 파일 경로
    output_file = 'Mars_Base_Inventory_danger.csv'  # 출력 CSV 파일 경로
    
    # CSV 파일을 읽고 내용을 리스트로 변환
    inventory_list = read_csv(csv_file)
    
    if inventory_list:
        # 첫 번째 항목은 헤더이므로 리스트에서 제외하고 나머지 항목만 사용
        header = inventory_list[0]
        data = inventory_list[1:]
        
        # 화물 목록을 인화성 지수에 따라 내림차순으로 정렬
        sorted_inventory = sort_inventory_by_flammability(data)
        
        # 인화성 지수가 0.7 이상인 항목만 필터링
        high_flammability = filter_high_flammability(sorted_inventory)
        
        # 결과 출력
        print("인화성 지수가 0.7 이상인 물질 목록:")
        for item in high_flammability:
            print(item)
        
        # 인화성 지수가 0.7 이상인 항목을 CSV로 저장
        save_to_csv([header] + high_flammability, output_file)
    else:
        print('파일을 읽을 수 없었습니다.')

if __name__ == '__main__':
    main()
