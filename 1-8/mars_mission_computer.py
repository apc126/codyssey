import random
import json
import time
import platform
import psutil

# DummySensor 클래스는 그대로 유지
class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18, 30), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0, 21), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50, 60), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500, 715), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 4)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values


# MissionComputer 클래스 정의
class MissionComputer:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None
        }
        self.sensor = DummySensor()

    def get_sensor_data(self):
        # 센서 데이터 5초 간격으로 출력하는 메서드 (문제 7 용도)
        while True:
            self.sensor.set_env()
            self.env_values = self.sensor.get_env()
            print("[센서 데이터]")
            print(json.dumps(self.env_values, indent=4))
            time.sleep(5)

    def get_mission_computer_info(self):
        info = {
            "운영체계": platform.system(),
            "운영체계 버전": platform.version(),
            "CPU 타입": platform.processor(),
            "CPU 코어 수": psutil.cpu_count(logical=True),
            "메모리 크기 (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2)
        }
        print("[미션 컴퓨터 시스템 정보]")
        print(json.dumps(info, indent=4, ensure_ascii=False))

    def get_mission_computer_load(self):
        load = {
            "CPU 실시간 사용량 (%)": psutil.cpu_percent(interval=1),
            "메모리 실시간 사용량 (%)": psutil.virtual_memory().percent
        }
        print("[미션 컴퓨터 부하 정보]")
        print(json.dumps(load, indent=4, ensure_ascii=False))


# MissionComputer 인스턴스화 및 시스템 정보 출력
runComputer = MissionComputer()
runComputer.get_mission_computer_info()
runComputer.get_mission_computer_load()
