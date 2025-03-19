print('Hello Mars')

'''main.py - 로그 파일을 분석하여 사고 원인을 Markdown 형식으로 저장하는 스크립트'''

from typing import List


def read_log_file(file_path: str) -> List[str]:
    '''로그 파일을 읽고 내용을 리스트로 반환.'''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
            print(''.join(content))  # 전체 로그 파일 내용 출력
            return content
    except FileNotFoundError:
        print(f"Error: 파일 '{file_path}'을 찾을 수 없습니다.")  # 파일이 존재하지 않을 때 예외 처리
    except PermissionError:
        print(f"Error: 파일 '{file_path}'에 대한 접근 권한이 없습니다.")  # 접근 권한 문제 예외 처리
    except Exception as error:
        print(f"Error: 파일을 읽는 중 예외 발생 - {error}")  # 기타 예외 처리
    return []


def analyze_logs(log_content: List[str]) -> str:
    '''로그 내용을 분석하여 사고 원인을 반환.'''
    # 특정 키워드를 포함하는 로그 라인을 추출
    error_logs = [line for line in log_content if 'ERROR' in line or 'FAIL' in line or 'unstable' in line or 'explosion' in line or 'powered down' in line]
    
    # Markdown 형식의 보고서 생성
    report = [
        '# 로그 분석 보고서', '',
        '## 발견된 오류 로그', ''
    ]
    
    # 오류 로그를 코드 블록으로 추가
    report.append('```' + '\n'.join(error_logs) + '\n```')
    
    return '\n'.join(report) + '\n'


def save_analysis_report(report_content: str, output_file: str) -> None:
    '''Markdown 형식으로 분석 보고서를 저장.'''
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(report_content)  # 파일에 분석 결과 저장
        print(f"분석 결과가 '{output_file}' 파일로 저장되었습니다.")
    except Exception as error:
        print(f"Error: 보고서를 저장하는 중 예외 발생 - {error}")  # 예외 처리


def main() -> None:
    '''로그 파일을 읽고 분석 후 보고서를 저장하는 메인 함수.'''
    log_file = 'mission_computer_main.log'  # 로그 파일 경로
    report_file = 'log_analysis.md'  # 분석 결과 저장 파일 경로
    
    print('로그 파일을 읽는 중...')
    logs = read_log_file(log_file)
    
    if logs:
        print('로그 분석 중...')
        analysis = analyze_logs(logs)
        save_analysis_report(analysis, report_file)
    else:
        print('로그 파일이 비어 있거나 존재하지 않습니다.')


if __name__ == '__main__':
    main()
