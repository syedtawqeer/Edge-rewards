import pyautogui
import time
import random
import string
import subprocess
import os

def open_application(application_command):
    # Launch the application using subprocess
    subprocess.Popen(application_command, shell=True)

def type_random_string_with_delay(interval, length, repetitions):
    for _ in range(repetitions):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        for char in random_string:
            pyautogui.typewrite(char)
            time.sleep(0.1)  # Slight delay between each character for realism
        pyautogui.press('enter')
        time.sleep(interval)

# Open Microsoft Edge
open_application('microsoft-edge')

# Give some time for Edge to open
time.sleep(2)

# Type random 10-character strings with a delay of 6 seconds between each input
interval = 6  # Adjust the delay based on your needs
length = 3
repetitions = 33
type_random_string_with_delay(interval, length, repetitions)

# Close Microsoft Edge
os.system("pkill microsoft-edge")
