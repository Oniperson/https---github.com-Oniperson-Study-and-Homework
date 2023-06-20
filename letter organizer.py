s = "abcd"
mystery = ""
mysterytwo = ""

for i in range(1,len(s)):
    if s[i] >= s[i-1]:
        mysterytwo += s[i]
    else:
        mysterytwo = mystery
        mysterytwo = ""
print (mystery)