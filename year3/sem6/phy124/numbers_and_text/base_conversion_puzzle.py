def convert_to_base15(n):
    digits = "0123456789ABCDE"
    ans = ""
    while n > 0:
        remainder = n % 15  # remainder is from 0 to 14 (inclusively)
        n = n // 15
        ans = digits[remainder] + ans

    return ans


number = 65533378
print(convert_to_base15(number))
