print("===============WELCOME TO THE BOOKFAIR=====================")
print()
print("CHOOSE YOUR GENRE")
print("1. Fiction")
print("2. Non fiction")
print()
choice= int(input("ENTER YOUR CHOICE: "))
if choice == 1:
    print("Pick your fiction type")
    print("1. Fantasy")
    print("2. Mystery")
    print()
    choice_2= int(input("ENTER YOUR CHOICE: "))
    if choice_2 == 1:
        print("HERE! Try Harry Potter")
    else:
        print("HERE! Try A Good Girls Murder Mystery ")
elif choice == 2:
    print("Pick your non fiction type")
    print("1. Autobiography")
    print("2. Self help book")
    choice_3= int(input("ENTER YOUR CHOICE: "))
    if choice_3 == 1:
        print("HERE! Try Diary of a Young Girl")
    else:
        print("HERE! Try The Power of Your Sub-consious Mind")
else:
    print("THERE ARE ONLY 2 OPTIONS!!! I guess you don't want to read.....")
    print("WE CAN'T BE FRIENDS AFTER THIS!!!!!!!!!!")
print()
print("=======================================================================")
print("YOUR BOOK IS READY!!!!!!")
print("=======================================================================")
