import time


def read_temp():
    with open("/sys/devices/virtual/thermal/thermal_zone0/temp", "r") as file:
        temp_raw = file.read()
    temp = int(temp_raw)/1000
    return temp


def set_speed(spd):
    with open("/sys/devices/pwm-fan/target_pwm", "w") as file:
        file.write(f"{spd}")


UPDATE_INTERVAL = 5
while True:
    print('read temp: ', read_temp())
    set_speed(100)          # 0 ~ 255
    time.sleep(UPDATE_INTERVAL)
