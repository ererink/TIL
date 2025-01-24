def kangaroo(x1, v1, x2, v2):
    kang1 =x1 
    kang2 = x2 
    
    if v1 <= v2:
        return "NO"
        
    while kang1 < kang2:
        if kang1 == kang2:
            return "YES"
        
        kang1 += v1 
        kang2 += v2 
        
    if kang1 == kang2:
        return "YES"
    else:
        return "NO"