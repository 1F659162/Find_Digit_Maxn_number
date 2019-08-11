# 6206021620159
# Kaittrakul Jaroenpong IT 1RA
# Python Chapter 5 Example 1

print(">> Program Find Maximum Digit <<")
while True :
    number = int(input("Enter number (0-Exit) : "))
    num = number
    if num != 0 :
        Max = 0
        while number != 0 :
            if Max < number %10 :
                Max = number % 10
            number = number // 10
        print(f"Maximum Digit of integer : {num} = {Max}")    
    else :
        break
print("Exit Program")
