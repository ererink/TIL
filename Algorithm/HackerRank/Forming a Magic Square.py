def formingMagicSquare(s):
    nums = []
    missing = []
    dupl = []
    
    for i in range(3):
        for j in range(3):
            nums.append(s[i][j])
    
    for i in range(1, 10):
        print(nums.count(i))
        if nums.count(i) > 1:
            dupl.append(i)
        if i not in nums:
            missing.append(i)
    
    missing = sorted(missing)
    dupl = sorted(dupl)
    print(missing)
    print(dupl)
    answer = 0
    for i in range(len(missing)):
        answer += abs(missing[i] - dupl[i])
    return answer
s = [[4, 5, 8], [2, 4, 1], [1, 9, 7]]
answer = formingMagicSquare(s)
print(answer)