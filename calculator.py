def binary_calculator(bin1, bin2, operator):
    
    # Checks if there's only 0s and 1s
    for l in bin1:
        for k in bin2:
            if l != "0" and l != "1":
                return "Error"
            if k != "0" and k != "1":
                return "Error"
    
    # Convert binary to 8 digits if less than 8 already
    if len(bin1) < 8:
        for i in range(8 - len(bin1)):
            bin1 = "0" + bin1
    if len(bin2) < 8:
        for j in range(8 - len(bin2)):
            bin2 = "0" + bin2

    # Converting binary to decimal
    bin1powers = []
    bin2powers = []
    # This loops through the binary string, and when there is a 1, it takes that index, and subtracts it from 7 to get the value to put to the power of 2, then adds it to the appropriate list
    # For example, if the second index is 1, then 7 - 2 = 5, so 2^5 = 32
    for index, value in enumerate(bin1):
        if value == "1":
            bin1powers.append(7 - index)
    for index, value in enumerate(bin2):
        if value == "1":
            bin2powers.append(7 - index)
    
    # Turn bin1 and bin2 into decimal
    bin1decimal = 0
    for i in bin1powers:
        bin1decimal += 2**i
    bin2decimal = 0
    for j in bin2powers:
        bin2decimal += 2**j

    # Performs the operation, as well as checking for overflow and NaN
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