def solution(s):
    answer = []
    sliced_s = s[2:-2].split('},{')
    sliced_s.sort(key=lambda x : len(x))
    
    for i in sliced_s:
        if ',' in i:
            temp = i.split(',')
            for t in temp:
                if int(t) not in answer:
                    answer.append(int(t)) 
        else:
             answer.append(int(i))           

    return answer