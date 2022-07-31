T = int(input())
for test_case in range(1, T + 1):


    list1 = ['b', 'd', 'p', 'q']
    list2 = ['d', 'b', 'q', 'p']
    
    list1 = list2
    
    chars = input()
    result = []
    
    for i in range(len(list1)):
        result.append(chars[i])
        
    print(result[::-1])