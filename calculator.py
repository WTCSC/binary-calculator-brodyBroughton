def binary_to_decimal(bin_str):
    decimal_value = 0
    for index, value in enumerate(bin_str):
        if value == "1":
            decimal_value += 2 ** ((len(bin_str) - 1) - index)
    return decimal_value

def binary_calculator(bin1, bin2, operator):
    # If there's only 0s and 1s in the strings, then it's valid, otherwise return error
    if not all(char in '01' for char in (bin1 + bin2)):
        return "Error"

    # Converting binary to decimal
    bin1decimal = binary_to_decimal(bin1)
    bin2decimal = binary_to_decimal(bin2)

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
    ls = [128, 64, 32, 16, 8, 4, 2, 1]
    final_result = ""
    for num in ls:
        if result % num == result:
            final_result += "0"
        elif result % num == 0 or result % num < num:
            final_result += "1"
            result = result % num
        
    return final_result

# Print statement for users who want to use the calculator :)
# print(binary_calculator("binary number 1", "binary number 2", "operation"))