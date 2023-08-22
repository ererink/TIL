import math
from collections import Counter
def solution(str1, str2):
    answer = 0
    str1_ele = []; str2_ele = []
    temp = ''
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            temp += str1[i]
            temp += str1[i + 1]
            if len(temp) == 2:
                str1_ele.append(temp.lower())
                temp = '' 
            
    temp = ''        
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            temp += str2[i]
            temp += str2[i + 1]
            if len(temp) == 2:
                str2_ele.append(temp.lower())
                temp = ''  
                
    C_str1 = Counter(str1_ele)
    C_str2 = Counter(str2_ele)
    
    inter = list((C_str1 & C_str2).elements())
    union = list((C_str1 | C_str2).elements())
    
    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        answer = math.floor((len(inter) / len(union) * 65536))
        return answer