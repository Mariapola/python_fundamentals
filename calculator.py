import re
print("welcome to amaka calculator isonu")

calculated = 0
run = True


def calculate():
    global calculated
    global run
    solve = input("Enter arithmetic here:")
    if solve == "quit":
        run = False
    else:
        solve = re.sub("[a-zA-Z:;'\",!@#$%^&.`~" "]", "", solve)
        calculated = eval(solve)
        print(calculated)


while run:
    calculate()