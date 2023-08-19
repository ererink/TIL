def solution(cacheSize, cities):
    answer = 0
    LRU = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        # 동일한 데이터 발견
        if city in LRU:
            LRU.remove(city)
            LRU.append(city)
            answer += 1
        # 동일한 데이터 없을 경우 추가
        else:
            # 꽉 차 있을 경우
            if len(LRU) >= cacheSize:
                LRU.pop(0)
                LRU.append(city)
            else:
                LRU.append(city)

            answer += 5
    return answer