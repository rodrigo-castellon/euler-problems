#Is a 4, 5, or 6-digit number a palindrome?
def ispalindrome(palindrome):
    i = 0
    length = len(str(palindrome))
    while i < 3:
        if length == 4 and not str(palindrome)[i] == str(palindrome)[(3-i)]:
            return False
            break
        if length == 5 and not str(palindrome)[i] == str(palindrome)[(4-i)]:
           return False
           break
        if length == 6 and not str(palindrome)[i] == str(palindrome)[(5-i)]:
            return False
            break
        i += 1
    else:
        return True

def main(three_digit_one, three_digit_two, i, j):
    while i >= 0:
        if ispalindrome((three_digit_one - i)*(three_digit_two - j)):
            print(three_digit_one - i)
            print(three_digit_two - j)
            break
        i -= 1
    else:
        if j >= 0:
            main(three_digit_one,three_digit_two, 9, j-1)
        else:
            print("no palindrome in this range")
main(999,999, 99, 99)
