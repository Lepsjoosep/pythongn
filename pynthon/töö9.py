def abc():
    a = float(input("Sisesta alus: "))
    b = float(input("Sisesta külg: "))
    c = float(input("Sisesta teine külg: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Error: valed mõõtmed")
    else:
        print("Mõõtmed on õiged")
        if c == b != a:
            print("See on võrdhaarne kolmnurk")
        if a == b == c:
            print("See on võrdkülgne kolmnurk")
        if a != b != c:
            print("See on erikülgne kolmnurk")
abc()