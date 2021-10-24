def isPalindrome(s):
    if len(s) == 1 or (len(s) == 2 and s[1] == s[0]):
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])


print(isPalindrome('kayak'))
print(isPalindrome('hello'))