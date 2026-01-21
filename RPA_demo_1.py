import pyautogui, time
#Mouse operations
pyautogui.click(100,100)
time.sleep(3)
pyautogui.rightClick(100,100)
time.sleep(5)
#finding mouse coordinates
# x,y = pyautogui.position()
# print("x=" ,x,"y=", y)
pyautogui.doubleClick(1366,22)
# pyautogui.scrollDown(500)    #not working

#Key board operations
time.sleep(5)
#pyautogui.click(498,839)
#time.sleep(3)
#pyautogui.typewrite("AI Tutorial")
# pyautogui.write("python .\RPA_demo_1.py")

# commenting this to avoid loop operations - pyautogui.press('enter')
# pyautogui.hotkey("ctrl","a")

#image processing
location = pyautogui.locateOnScreen("gpt.png",confidence=0.0)
print (location)
time.sleep(2)
pyautogui.click(pyautogui.center(location))
print(pyautogui.size())
ss = pyautogui.screenshot()
ss.save("demo.png")