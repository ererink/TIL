def palindromeIndex(s):
   
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if s[left + 1:right + 1] == s[left + 1:right + 1][::-1]:
                return left
            elif s[left:right] == s[left:right][::-1]:
                return right
            else:
                return -1
        left += 1
        right -= 1  
    return -1  

s = 'aaab'
answer = palindromeIndex(s)
print(answer)