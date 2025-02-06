# x=int(input("Enter The Value of x : "))

# match x:
#     case 1:
#         print("The value of x is 1")
#     case 2:
#         print("The value of x is 2")
#     case 3:
#         print("The value of x is 3")
#     case 4:
#         print("The value of x is 4")

#     #default Case
#     case _ if x!=90:
#         print("The value of x is not 90")
#     case _ if x!=80:
#         print("The value of x is not 80")
#     case _ :
#         print(x)


char = input("Enter a character : ")

match char:
    case "a":
        print(f"{char} is a vowel.")

    case "e":
        print(f"{char} is a vowel.")

    case "i":
        print(f"{char} is a vowel.")

    case "o":
        print(f"{char} is a vowel.")

    case "u":
        print(f"{char} is a vowel.")
    case "A":
        print(f"{char} is a vowel.")

    case "E":
        print(f"{char} is a vowel.")

    case "I":
        print(f"{char} is a vowel.")

    case "O":
        print(f"{char} is a vowel.")

    case "U":
        print(f"{char} is a vowel.")
    case _:
        print(f"{char} is not a vowel")
