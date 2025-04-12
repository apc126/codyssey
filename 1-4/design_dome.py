# 전역 변수
area = 0  # 면적 저장용 변수
weight = 0  # 무게 저장용 변수

def sphere_area(diameter=10, material='유리', thickness=1):
    """반구체 형태의 돔 면적 및 무게 계산 함수"""
    
    # 지름 -> 반지름으로 변환
    radius = diameter / 2
    
    # 원주율 (π)
    pi = 3.141592653589793
    
    # 밀도 값 설정 (g/cm³)
    material_density = {
        '유리': 2.4,
        '알루미늄': 2.7,
        '탄소강': 7.85
    }
    
    if material not in material_density:
        print("잘못된 재질입니다. 유리, 알루미늄, 탄소강 중 하나를 입력하세요.")
        return

    density = material_density[material]
    
    # 반구 면적 계산: 2πr²
    global area
    area = 2 * pi * radius**2  # 면적 = 2πr²
    
    # 부피 계산: (4/3)πr³ (구의 부피)
    volume = (4/3) * pi * radius**3
    
    # 두께를 반영한 부피 조정
    adjusted_volume = volume * thickness
    
    # 무게 계산: 밀도 * 부피, 화성 중력 반영 (지구 중력의 0.38배)
    global weight
    weight = (density * adjusted_volume) * 0.38 / 1000  # g -> kg로 변환
    
    # 소수점 3자리로 출력
    print(f"재질 =⇒ {material}, 지름 =⇒ {diameter}, 두께 =⇒ {thickness}, 면적 =⇒ {area:.3f}, 무게 =⇒ {weight:.3f} kg")

def main():
    """주요 작업 흐름"""
    # 사용자 입력 받기
    material = input("재질을 입력하세요 (유리, 알루미늄, 탄소강): ") or '유리'  # 기본값 '유리'
    diameter = input("지름을 입력하세요 (단위: m): ") or '10'  # 기본값 10m
    thickness = input("두께를 입력하세요 (단위: cm): ") or '1'  # 기본값 1cm
    
    # 지름을 cm로 변환
    try:
        diameter = float(diameter) * 100  # m -> cm로 변환
    except ValueError:
        print("지름은 숫자만 입력할 수 있습니다.")
        return
    
    # 두께 값 처리
    try:
        thickness = float(thickness)
    except ValueError:
        print("두께는 숫자만 입력할 수 있습니다.")
        return
    
    # 함수 호출
    sphere_area(diameter, material, thickness)

if __name__ == '__main__':
    main()

# 계산 과정
# 1. 반구체 면적: 면적은 반구체의 겉면만 계산되므로, 구의 표면적 공식인 4πr² 중에서 2πr²를 사용.
# 2. 부피: 구의 부피는 (4/3)πr³ 공식을 사용.
# 3. 화성 중력 반영: 지구에서의 무게를 기준으로 화성 중력은 지구 중력의 0.38배이므로 이를 반영.
# 4. 결과는 소수점 3자리까지 출력하여 결과가 너무 길지 않도록 처리.
