import pyautogui, time
#Mouse operations
print("Place the pointer where needed right now")

time.sleep(10)
#finding mouse coordinate
x,y = pyautogui.position()
print("x=" ,x,"y=", y)
