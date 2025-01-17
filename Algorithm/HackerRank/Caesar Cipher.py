
def caesarCipher(s, k):
    answer = ''
    k = k % 26  

    for i in s:
        if 'A' <= i <= 'Z':
            new_ascii = ord(i) + k
            if new_ascii > 90:  
                new_ascii = (new_ascii - 90) + 64
            answer += chr(new_ascii)
        elif 'a' <= i <= 'z': 
            new_ascii = ord(i) + k
            if new_ascii > 122:  
                new_ascii = (new_ascii - 122) + 96
            answer += chr(new_ascii)
        else: 
            answer += i

    return answer

s= 'www.abc.xy'
k = 87
answer = caesarCipher(s, k)
print(answer)