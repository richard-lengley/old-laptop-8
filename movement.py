import pyautogui as pag

def press_tab(n):
    for i in range(n):
        time.sleep(0.2)
        pag.hotkey("tab")
        time.sleep(0.2)

def press_up_arrow(n):
    for i in range(n):
        time.sleep(0.2)
        pag.hotkey("up")
        time.sleep(0.2)
