import pyautogui
import time
from datetime import datetime
import pandas as pd 
import webbrowser

def login(classlink):

    webbrowser.open(classlink)
    time.sleep(5)

    cancel_btn=pyautogui.locateCenterOnScreen('Images\cancel.png',grayscale=False,)
    pyautogui.moveTo(cancel_btn)
    pyautogui.click()

    launch_btn=pyautogui.locateOnScreen('Images\lmeet_dark.png',grayscale=False, confidence=.5)
    pyautogui.moveTo(launch_btn)
    pyautogui.click()

    launch_btn=pyautogui.locateOnScreen('Images\lmeet.png',grayscale=False, confidence=.5)
    pyautogui.moveTo(launch_btn)
    pyautogui.click()
    time.sleep(1)

    cancel_btn=pyautogui.locateCenterOnScreen('Images\cancel.png',grayscale=False,)
    pyautogui.moveTo(cancel_btn)
    pyautogui.click()

    joinw_btn= pyautogui.locateCenterOnScreen('Images\joinbrow_w.PNG')
    pyautogui.moveTo(joinw_btn)
    pyautogui.click()

    joinb_btn= pyautogui.locateCenterOnScreen('Images\joinbrow_b.PNG')
    pyautogui.moveTo(joinb_btn)
    pyautogui.click()
    time.sleep(2)

    joinw_btn= pyautogui.locateCenterOnScreen('Images\join_w.png',grayscale=False)
    pyautogui.moveTo(joinw_btn)
    pyautogui.click()

    joinb_btn= pyautogui.locateCenterOnScreen('Images\join_b.png',grayscale=False)
    pyautogui.moveTo(joinb_btn)
    pyautogui.click()
    
    audio_btn=pyautogui.locateCenterOnScreen('Images\inmeet.png',grayscale=False,)
    pyautogui.moveTo(audio_btn)
    pyautogui.click()
    time.sleep(10)

data=pd.read_csv('timing.csv')

while True:

    timern=datetime.now().strftime("%H:%M")
    if timern in str(data['time(24hrformat)']):
        row=data.loc[data['time(24hrformat)'] == timern]
        link= str(row.iloc[0,1])
        login(link)
        time.sleep(40)
        print("Signed In")

    
    

