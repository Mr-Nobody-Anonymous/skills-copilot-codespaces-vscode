# By Kena Fayera
try:
    s_r = float(input("Enter your Score: "))
    if s_r > 100 or s_r < 0:
        print("It should be between 0 - 100 enter again")
    else:
        if s_r >= 90 and s_r <= 100:
            print("Your Grade is 4.0 You got A+")
        elif s_r >= 83:
            print("Your Grade is 4.0 You got A")
        elif s_r >= 80:
            print("Your Grade is 3.75 You got A-")
        elif s_r >= 75:
            print("Your Grade is 3.5 You got B+")
        elif s_r >= 68:
            print("Your Grade is 3.0 You got B")
        elif s_r >= 65:
            print("Your Grade is 2.75 You got B-")
        elif s_r >= 60:
            print("Your Grade is 2.5 You got C+")
        elif s_r >= 50:
            print("Your Grade is 2.0You got C")
        elif s_r >= 45:
            print("Your Grade is 1.75 You got C-")
        elif s_r >= 40:
            print("Your Grade is 1.0 You got D")
        elif s_r >= 30:
            print("Your Grade is 0 You got Fx")
        elif s_r < 30:
            print("Your Grade is 0 You got F")
        else:
            print("No Grade ")
except ValueError:
    print("Your input is not correct please enter only numbers")


