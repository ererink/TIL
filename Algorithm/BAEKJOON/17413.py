s = list(input())
stack = []
check = []

for i in s:
    if i == '<':
        stack.append(i)

    elif i == ' ':
        continue

    else:
        stack.append(i)
        check.append(stack.pop())

print(stack + check)