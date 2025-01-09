def binary_calculator(bin1, bin2, operator):
    
    # Checks if there's only 0s and 1s
    if all(char in '01' for char in bin1):
        pass
    else:
        return "Error"
    
    if all(char in '01' for char in bin2):
        pass
    else:
        return "Error"
    
    # Convert binary to 8 digits if less than 8 already
    if len(bin1) < 8:
        bin1 = bin1.zfill(8)
        
    if len(bin2) < 8:
        bin2 = bin2.zfill(8)

    # Checks if the binary is larger than 8 digits
    if len(bin1) > 8:
        return "Error"
    
    if len(bin2) > 8:
        return "Error"

    # Converting binary to decimal
    bin1decimal = 0
    bin2decimal = 0

    # Iterates through the binary string, and if the value is 1, then add 2 to the power of the index to the decimal value
    for index, (value1, value2) in enumerate(zip(bin1, bin2)):
        if value1 == "1":
            bin1decimal += 2 ** (7 - index)

        if value2 == "1":
            bin2decimal += 2 ** (7 - index)

    # Performs operations, Overflow and NaN checks
    if operator == "+":
        result = bin1decimal + bin2decimal
    elif operator == "-":
        result = bin1decimal - bin2decimal
    elif operator == "*":
        result = bin1decimal * bin2decimal
    elif operator == "/":
        if bin2decimal == 0:
            return "NaN"
        else:
            result = bin1decimal // bin2decimal
    if result > 255 or result < 0:
        return "Overflow"

    # Convert decimal to binary by iterating through the list of powers of 2, and if the result is divisible by the power of 2, then add a 1, otherwise add a 0
    ls = [128,64,32,16,8,4,2,1]
    finalResult = ""
    for num in ls:
        if result % num == result:
            finalResult += "0"
        elif result % num == 0 or result % num < num:
            finalResult += "1"
            result = result % num
        
    return finalResult

# Print statement for users who want to use the calculator :)
# print(binary_calculator("xxxxxxxx", "xxxxxxxx", "x"))