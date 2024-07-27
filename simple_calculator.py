a = int(input( "Enter 1st number: "))
b = int(input( "Enter 2nd number: "))
c = input("Enter operation: ")

match c:
    case "+":
        print(" the value of", a, "+", b, "is = ", a + b)
    case "-":
        print(" the value of", a, "-", b, "is = ", a - b)
    case "*":
        print(" the value of", a, "*", b, "is = ", a * b)
    case "/":
        (print(" the value of", a, "/", b, "is = ", a / b))
    case "%":
        (print(" the value of", a, "%", b, "is = ", a % b))

