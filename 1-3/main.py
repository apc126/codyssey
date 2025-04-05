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

def save_to_binary(data, file_path):
    '''리스트 데이터를 이진 파일로 저장'''
    try:
        with open(file_path, 'wb') as file:
            for item in data:
                line = ','.join(item) + '\n'
                file.write(line.encode('utf-8'))
        print(f"이진 데이터가 '{file_path}' 파일로 저장되었습니다.")
    except Exception as error:
        print(f"Error: 이진 저장 중 예외 발생 - {error}")

def read_binary_file(file_path):
    '''이진 파일을 읽어 내용 출력'''
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            print("이진 파일 내용:")
            print(content.decode('utf-8'))
    except Exception as error:
        print(f"Error: 이진 파일 읽기 중 예외 발생 - {error}")

def main():
    '''주요 작업 흐름'''
    csv_file = 'Mars_Base_Inventory_List.csv'
    danger_file = 'Mars_Base_Inventory_danger.csv'
    binary_file = 'Mars_Base_Inventory_List.bin'

    inventory_list = read_csv(csv_file)

    if inventory_list:
        header = inventory_list[0]
        data = inventory_list[1:]

        sorted_inventory = sort_inventory_by_flammability(data)
        high_flammability = filter_high_flammability(sorted_inventory)

        print("인화성 지수가 0.7 이상인 물질 목록:")
        for item in high_flammability:
            print(item)

        save_to_csv([header] + high_flammability, danger_file)
        save_to_binary([header] + sorted_inventory, binary_file)
        read_binary_file(binary_file)
    else:
        print('파일을 읽을 수 없었습니다.')

if __name__ == '__main__':
    main()

# 텍스트 파일 vs 이진 파일
# 텍스트 파일은 사람이 읽을 수 있는 문자 형식으로 데이터를 저장한다.
# 장점: 사람이 쉽게 읽고 편집할 수 있다. 대부분의 도구와 호환된다.
# 단점: 파일 크기가 크고, 구조화된 데이터를 표현하기 어렵다.

# 이진 파일은 기계가 이해할 수 있는 형식으로 데이터를 저장한다.
# 장점: 저장 공간이 적고, 읽기/쓰기 속도가 빠르며, 복잡한 데이터 표현에 유리하다.
# 단점: 사람이 읽기 어렵고, 플랫폼 간 호환성이 떨어질 수 있다.