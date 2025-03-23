'''log_to_json.py - 로그 파일을 읽어 리스트 및 JSON 형식으로 변환하는 스크립트'''

import json
from typing import List, Dict

def read_log_file(file_path: str) -> List[str]:
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

def parse_log_data(log_lines: List[str]) -> List[List[str]]:
    '''로그 데이터를 콤마 기준으로 분리하여 리스트로 변환.'''
    return [line.strip().split(',', maxsplit=2) for line in log_lines if line.strip()]

def convert_to_dict(log_list: List[List[str]]) -> Dict[str, Dict[str, str]]:
    '''리스트 데이터를 사전(Dictionary)으로 변환.'''
    return {entry[0]: {"level": entry[1], "message": entry[2]} for entry in log_list}

def save_to_json(data: Dict[str, Dict[str, str]], output_file: str) -> None:
    '''변환된 데이터를 JSON 파일로 저장.'''
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"JSON 데이터가 '{output_file}' 파일로 저장되었습니다.")
    except Exception as error:
        print(f"Error: JSON 저장 중 예외 발생 - {error}")

def main() -> None:
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
