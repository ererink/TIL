# 유학금지

prohibit = 'CAMBRIDGE'
s = input()
new_s = ''

for i in range(len(s)):
        if s[i] in prohibit:
            continue
        new_s += s[i]

print(new_s)