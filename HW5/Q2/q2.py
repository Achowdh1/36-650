def clean(s):
    if not isinstance(s, str): return "Invalid input"
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    res = ""
    for char in s:
        if char not in punctuations:
            res += char
    return res

s = "Hello in 36-650, & other MSP courses."
print(clean(s))