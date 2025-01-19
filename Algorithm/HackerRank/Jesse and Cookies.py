import heapq

def cookies(k, A):
    heapq.heapify(A)
    cnt = 0
    
    while A[0] < k:
        if len(A) < 2:
            return -1
            
        min_cookie1 = heapq.heappop(A)
        min_cookie2 = heapq.heappop(A)
        
        new_cookie = min_cookie1 + 2 * min_cookie2 
        heapq.heappush(A, new_cookie)
        cnt += 1
        
    return cnt