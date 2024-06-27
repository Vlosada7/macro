import pyautogui
import time


def move_mouse_and_press_key():
    while True:
        # Move o mouse para uma posição ligeiramente diferente
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 10, y + 10, duration=0.5)

        # Pressiona a tecla "Enter"
        pyautogui.press('enter')

        # Aguarda 5 segundos antes de repetir
        time.sleep(5)


if __name__ == "__main__":
    move_mouse_and_press_key()
