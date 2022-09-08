score = 0

for _ in range(10):
    copy_score = score
    score += int(input())
    if score >= 100:
        break


    
if score > 100:
    under_ = 100 - copy_score
    over_ = score - 100
    if under_ > over_:
        print(score)
    elif under_ < over_:
        print(copy_score)
    else:
        print(score)
    
else: 
    print(score)
