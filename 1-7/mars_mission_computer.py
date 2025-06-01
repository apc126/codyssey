import random  # 랜덤 값 생성을 위한 모듈
import json    # 환경 데이터를 JSON 형식으로 출력하기 위한 모듈
import time    # 주기적 실행(5초 대기)을 위한 모듈

# 더미 센서 클래스 정의
class DummySensor:
    def __init__(self):
        # 센서 측정값들을 저장할 사전 초기화
        self.env_values = {
            "mars_base_internal_temperature": None,     # 내부 온도
            "mars_base_external_temperature": None,     # 외부 온도
            "mars_base_internal_humidity": None,        # 내부 습도
            "mars_base_external_illuminance": None,     # 외부 광량
            "mars_base_internal_co2": None,             # 내부 이산화탄소 농도
            "mars_base_internal_oxygen": None           # 내부 산소 농도
        }

    # 센서 값을 무작위로 생성하여 env_values에 저장
    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18, 30), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0, 21), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50, 60), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500, 715), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 4)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4, 7), 2)

    # 현재 저장된 센서 값 반환
    def get_env(self):
        return self.env_values

# 미션 컴퓨터 클래스 정의
class MissionComputer:
    def __init__(self):
        # 미션 컴퓨터 내부의 환경 정보를 저장할 사전 초기화
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None
        }
        # DummySensor 클래스의 인스턴스를 멤버로 포함
        self.sensor = DummySensor()

    # 센서 데이터를 받아서 env_values에 저장하고 5초 간격으로 출력
    def get_sensor_data(self):
        while True:
            self.sensor.set_env()                 # 랜덤 값으로 센서 환경 설정
            self.env_values = self.sensor.get_env()  # 센서 값 받아와서 저장
            print(json.dumps(self.env_values, indent=4))  # JSON 포맷으로 보기 좋게 출력
            time.sleep(5)  # 5초 대기 후 반복

# 미션 컴퓨터 인스턴스 생성 및 실행
RunComputer = MissionComputer()
RunComputer.get_sensor_data()