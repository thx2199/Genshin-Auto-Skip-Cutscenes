import time
import random
import keyboard
import pyautogui

# 获取当前鼠标位置
def get_mouse_position():
    return pyautogui.position()

# 检查鼠标是否在屏幕右侧20%的区域内
def is_mouse_in_right_area():
    screen_width, screen_height = pyautogui.size()
    right_x = screen_width * 0.8  # 屏幕右侧20%区域的起始x坐标
    mouse_x, mouse_y = get_mouse_position()
    if right_x <= mouse_x <= screen_width:
        return True
    return False

def simulate_f_key(wait_time):
    while True:
        if is_mouse_in_right_area():
            keyboard.send('f')
        time.sleep(wait_time)

def main():
    while True:
        # 随机间隔时间 0.4 ~ 0.8s
        wait_time = random.randint(40, 80) / 100
        simulate_f_key(wait_time)

if __name__ == "__main__":
    main()