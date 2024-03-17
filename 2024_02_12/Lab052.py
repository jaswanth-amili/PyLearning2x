browser = input("Enter browser : ")

match browser.lower():
    case "chrome":
        print("Chrome is selected")
    case "edge":
        print("Edge is selected")
    case "firefox":
        print("Firefox is selected")
    case _:
        print("No browser found")