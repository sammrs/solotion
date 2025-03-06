list = [2, 4, 5, 6, 7, 9, 10]
x = ""
while x != "exit":
    x = input("Enter a number: ")
    
    if x == "exit":
        break

    if x.isdigit():  # بررسی اینکه ورودی عدد است
        x = int(x)  # تبدیل ورودی به عدد صحیح
        if x in list:
            print("Yes")
        else:
            print("No")
    else:
        print("Please enter a valid number or 'exit' to quit.")
