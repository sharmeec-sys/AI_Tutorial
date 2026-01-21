import pyautogui
import time
import webbrowser

# Step 1: Small delay so you can switch windows if needed
time.sleep(3)

# Step 2: Open Google Chrome (default browser)
webbrowser.open("https://www.google.com")

# Wait for browser to open
time.sleep(5)

# Step 3: Type search query
pyautogui.write("recent India cricket match score", interval=0.1)


# Step 4: Press Enter to search
pyautogui.press("enter")

# Wait for results to load
time.sleep(5)

# Step 5: Open the first link (Google usually selects it automatically)
pyautogui.press("enter")
