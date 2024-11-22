import pyautogui
import keyboard
import time

# Define the three positions (mov1, mov2, mov3) as (x, y) tuples
mov1 = (1700, 925)  # Example coordinates for first click
mov2 = (1700, 740)#(1700, 750)  # Example coordinates for second click
mov3 = (1700, 700)#(300, 400)  # Example coordinates for third click

# Function to perform the mouse clicks
def automate_clicks():
    while True:
        # Perform the clicks in a loop
        pyautogui.click(mov1)
        time.sleep(0.5)  # Adjust the time between clicks if necessary
        pyautogui.click(mov2)
        time.sleep(0.5)
        pyautogui.click(mov3)
        time.sleep(0.5)

        # Check if the "C" key is pressed to stop
        if keyboard.is_pressed('c'):
            print("Stopping automation.")
            break

# Start the automation
automate_clicks()
