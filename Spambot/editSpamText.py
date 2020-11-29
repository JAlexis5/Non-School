import sys, time

f = open("spamtext.txt", mode="r", encoding="utf-8")
print("Contents of spamtext.txt: \n\n")
print(f.read())
print("\n1 to wipe contents, 2 to edit contents, 3 to exit\n")
f.close()

while True:
    eraseOrEdit = input()
    if eraseOrEdit == "1":  # erase
        open1 = open("spamtext.txt", mode="w", encoding="utf-8")
        open1.truncate(0)
        time.sleep(0.5)
        print('\nContents erased.')
        time.sleep(1)
        break
    elif eraseOrEdit == "2":  # edit
        open1 = open("spamtext.txt", mode="r", encoding="utf-8")
        print("\nLoading spamtext.txt...")
        time.sleep(1)
        break
    elif eraseOrEdit == "3":  # exit
        print("\nSee you next time.")
        time.sleep(1)
        sys.exit()
    else:  # when something else is entered
        print("\nPlease enter a valid value.")
        time.sleep(1)

print("\n1 to overwrite the contents, 2 to append to end, 3 to exit")
open1.close()
while True:
    overwriteOrAppend = input()
    if overwriteOrAppend == "1":  # overwrite contents
        open2 = open("spamtext.txt", mode="w", encoding="utf-8")
        print("\nLoading spamtext.txt...")
        time.sleep(1)
        break
    elif overwriteOrAppend == "2":  # append to end
        open2 = open("spamtext.txt", mode="a", encoding="utf-8")
        print("\nLoading spamtext.txt...")
        time.sleep(1)
        break
    elif overwriteOrAppend == "3":  # exit
        print("\nSee you next time.")
        time.sleep(1)
        sys.exit()
    else:  # when something else is entered
        print("\nPlease enter a valid value.")
        time.sleep(1)

while True:
    if open2.mode == "w":
        print("Insert new text:")
        toBeAdded = input()
        open2.write(toBeAdded)
        open2.close()
        break
    elif open2.mode == "a":
        print("Insert text to be added:")
        toBeAdded = input()
        toBeAddedStr = "'" + toBeAdded + "'"
        open2.write(toBeAdded)
        open2.close()
        break
    else:
        print("\nPlease enter a valid value.")

print("Would you like to view the file's contents?")
while True:
    yesNo = input()
    if yesNo.lower() == "yes" or yesNo.lower() == "ye" or yesNo.lower() == "y" or yesNo.lower() == "yup" or yesNo.lower() == "yea":
        viewfile = True
        break
    elif yesNo.lower() == "no" or yesNo.lower() == "nah" or  yesNo.lower() == "n" or yesNo.lower() == "nope":
        viewfile = False
        break

if viewfile == True:
    open3 = open("spamtext.txt", mode="r", encoding="utf-8")
    print(open3.read())
elif viewfile == False:
    print("See you next time.")
    time.sleep(1)
    sys.exit