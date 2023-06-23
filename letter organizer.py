s = "abcdpoopsdfasjfkjlhmvfabcdefgajlajhaz"
mystery = ""
mysterytwo = ""

for i in range(1,len(s)):
    if s[i-1] <= s[i]:
        mysterytwo += s[i-1]
    elif len(mystery) <= len(mysterytwo):
            mysterytwo += s[i-1]
            mystery = mysterytwo
            mysterytwo = ""
    else:
         mysterytwo = ""
print (mystery)