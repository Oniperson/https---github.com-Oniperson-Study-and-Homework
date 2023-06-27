s = "abcdbwxyz"
longest_string = ""
current_string = ""
s += " "  
for i in range(1,len(s)):
    if s[i-1] <= s[i]:
        current_string += s[i-1]
    elif len(longest_string) <= len(current_string):
            current_string += s[i-1]
            longest_string = current_string
            current_string = ""
    else:
         current_string = ""
print (longest_string)