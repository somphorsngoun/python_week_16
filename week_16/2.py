def binaryToDecimal(binaryNumber):
    value = 0
    String = str(binaryNumber)
    number = len(String)
    for index in range(len(String)):
        value = value+ int(String[index])*2**(number-1)
        number = number -1
    return value
binary = int(input())
print(binaryToDecimal(binary))