number = open("numbers.txt","w")
for i in range(4):
    num = input("Enter a number: ")
    number.write(str(num))
    number.write("\n")
number.close()


# number  = open("numbers.txt","r")
# content = number.read()
# print(content)

# number.close()

# number = open("numbers.txt","a")
# number.write("Here are your four numbers: ")
# number.close()
