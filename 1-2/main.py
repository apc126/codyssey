'''log_to_json.py - 로그 파일을 읽어 리스트 및 JSON 형식으로 변환하는 스크립트'''

import json
from typing import List, Dict

def read_log_file(file_path: str):
    '''log_to_json.py - 로그 파일을 읽어 리스트 및 JSON 형식으로 변환하는 스크립트'''

def read_log_file(file_path: str):
    '''로그 파일을 읽고 내용을 리스트로 반환.'''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
            print(''.join(content))  # 전체 로그 파일 내용 출력
            return content
    except FileNotFoundError:
        print(f"Error: 파일 '{file_path}'을 찾을 수 없습니다.")
    except PermissionError:
        print(f"Error: 파일 '{file_path}'에 대한 접근 권한이 없습니다.")
    except Exception as error:
        print(f"Error: 파일을 읽는 중 예외 발생 - {error}")
    
    return []

def parse_log_data(log_lines):
    '''로그 데이터를 콤마 기준으로 분리하여 리스트로 변환.'''
    return [line.strip().split(',', maxsplit=2) for line in log_lines if line.strip()]

def convert_to_dict(log_list):
    '''리스트 데이터를 사전(Dictionary)으로 변환.'''
    log_dict = {}
    for entry in log_list:
        log_dict[entry[0]] = {"level": entry[1], "message": entry[2]}
    return log_dict

def save_to_json(data, output_file):
    '''변환된 데이터를 JSON 파일로 저장.'''
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("{\n")
            for key, value in data.items():
                file.write(f'    "{key}": {{\n')
                file.write(f'        "level": "{value["level"]}",\n')
                file.write(f'        "message": "{value["message"]}"\n')
                file.write("    },\n")
            file.write("}\n")
        print(f"JSON 데이터가 '{output_file}' 파일로 저장되었습니다.")
    except Exception as error:
        print(f"Error: JSON 저장 중 예외 발생 - {error}")

def main():
    '''로그 파일을 처리하고 JSON으로 저장하는 메인 함수.'''
    log_file = 'mission_computer_main.log'  # 로그 파일 경로
    json_file = 'mission_computer_main.json'  # JSON 저장 경로
    
    print('로그 파일을 읽는 중...')
    log_lines = read_log_file(log_file)
    
    if log_lines:
        print('로그 데이터를 리스트로 변환 중...')
        log_list = parse_log_data(log_lines)
        print(log_list)  # 리스트 객체 출력
        
        print('시간 역순으로 정렬 중...')
        log_list.sort(reverse=True, key=lambda x: x[0])
        
        print('리스트 데이터를 사전 객체로 변환 중...')
        log_dict = convert_to_dict(log_list)
        
        print('JSON 파일로 저장 중...')
        save_to_json(log_dict, json_file)
    else:
        print('로그 파일이 비어 있거나 존재하지 않습니다.')

if __name__ == '__main__':
    main()
    
# ---------------------------------------
# 사전 객체(Dict) 설명:
# 사전 객체는 데이터를 '키-값' 쌍으로 저장하는 Python 자료형이다.
# 키를 통해 값을 빠르게 검색할 수 있고, 여러 값을 하나의 단위로 묶어서 구조화된 형태로 저장할 수 있다.
#
# JSON 파일 포맷:
# - JSON은 텍스트 기반 데이터 형식으로, '키-값' 쌍을 중괄호로 묶어서 표현한다.
# - JSON은 사람이 읽을 수 있고 다양한 프로그래밍 언어에서 쉽게 파싱 및 생성할 수 있다.
# - 중첩된 데이터 구조를 표현할 수 있으며, 주로 데이터 교환에 사용된다.
# 
# CSV 파일 포맷:
# - CSV는 각 데이터를 쉼표로 구분한 텍스트 형식으로, 주로 표 형태의 데이터를 저장하는 데 사용된다.
# - 행(row)은 각 데이터 항목을 표현하고, 열(column)은 쉼표로 구분된 데이터 항목들을 표현한다.
# - 간단하고, 사람이 읽을 수 있는 구조로 되어 있다.
# ---------------------------------------