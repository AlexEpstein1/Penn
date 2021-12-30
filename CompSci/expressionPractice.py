def main():
    x = input("What is your initial position?")
    v = input("What is your initial velocity?")
    t = input("How much time ellapsed?")
    a = input("What is your acceleration?")
    x = float(x)
    v = float(v)
    t = float(t)
    a = float(a)
    print(x + (1/2 * a * t **2) + (v * t))

main() 
