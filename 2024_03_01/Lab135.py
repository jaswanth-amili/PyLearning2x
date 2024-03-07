class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number : "))
        except Exception as e:
            print(e)
        try:
            b = int(input("Enter a number : "))
        except Exception as e:
            print(e)

