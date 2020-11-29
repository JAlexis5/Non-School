import pyautogui, time
from win10toast import ToastNotifier


print("How many times do you want to spam?")

while True:
    timesSpam = int(input())
    if timesSpam > 0:
        break
    else:
        print("Please enter a valid value.")

print("Instructions:\nIn 5 seconds, the spambot will begin.\nIt will type out the contents of spamtext.txt and send it repeatedly.\nTo stop this process, press Ctrl+Shift+S. This works regardless of where you are.\nHave fun spamming!")
time.sleep(5)


while True:
    textToSpam = open("spamtext.txt", "r")
    pyautogui.typewrite(textToSpam.read())
    pyautogui.press("enter")
    timesSpam = timesSpam - 1
    if timesSpam == 0:
        toaster = ToastNotifier()
        toaster.show_toast("spambot.py", "spambot.py has finished spamming.", threaded=True,
                   icon_path=None, duration=3)
        break
