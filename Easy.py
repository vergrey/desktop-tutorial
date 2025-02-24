print('Please input programm number')
print('1. Radius of the  round;  2. Found x in ax + b = 0;  3. To Farengeit;  4. Middle number; 5. Priority example')
c = int(input())
match c:
    case 1:
        print('Hello! Input radius')
        r = int(input())
        S  = float(3.14159 * r ** 2)
        print(S)
    case 2:
        print('Hello! Input a')
        a = int(input())
        print('input b')
        b = int(input())
        x = float((-b) / a)
        print(x)
    case 3:
        print('Hello! Input celsia')
        a = int(input())
        x = float(9/5 * a + 32)
        print(x)
    case 4:
        print('Hello! Input 3 numbers')
        a = int(input())
        b = int(input())
        c = int(input())
        x = float((a+b+c)/3)
        print(x)
    case 5:
        print('Priotity example')
        print(5 + 2 * 3 - 4 / 2)
        print((3 + 5) * (2 + 4) / 2)
        print(-3 * 6/2 * 4)
        print(5 + 4 * 5 ** 2 + 7)