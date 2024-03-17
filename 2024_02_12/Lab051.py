# Match case this is similar to switch
# No need to use break

num = int(input("Enter number : "))

match num:
    case 1:
        print("Entered 1")
    case 2:
        print("Entered 2")
    case 3:
        print("Entered 3")
    case 4:
        print("Entered 4")
    case 5:
        print("Entered 5")
    case 6:
        print("Entered 6")
    case _:
        print("No idea")