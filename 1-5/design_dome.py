import numpy as np

def load_csv_file(file_path):
    try:
        data = np.genfromtxt(file_path, delimiter=',', dtype=None, encoding='utf-8', names=True)
        return data
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
    except ValueError:
        print(f"잘못된 데이터 형식이 포함되어 있습니다: {file_path}")
    except Exception as e:
        print(f"알 수 없는 오류가 발생했습니다 ({file_path}): {e}")
    return None

def main():
    arr1 = load_csv_file('mars_base_main_parts-001.csv')
    arr2 = load_csv_file('mars_base_main_parts-002.csv')
    arr3 = load_csv_file('mars_base_main_parts-003.csv')

    if arr1 is None or arr2 is None or arr3 is None:
        print("데이터를 모두 불러오지 못해 프로그램을 종료합니다.")
        return

    try:
        # 각 배열을 리스트로 변환 후 병합
        parts_combined = np.concatenate((arr1, arr2, arr3))

        # strength 값만 추출해서 평균 계산
        strength_values = [item[1] for item in parts_combined]
        strength_array = np.array(strength_values)
        mean_strength = np.mean(strength_array)

        # 평균보다 작은 값 필터링
        filtered_parts = [item for item in parts_combined if item[1] < 50]

        # 저장을 위해 다시 배열로 변환
        output_array = np.array(filtered_parts, dtype=arr1.dtype)

        # CSV로 저장
        header = "parts,strength"
        np.savetxt('parts_to_work_on.csv', output_array, delimiter=',', fmt='%s,%d', header=header, comments='')

        print("작업이 완료되었습니다. parts_to_work_on.csv가 생성되었습니다.")
    except Exception as e:
        print(f"처리 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()