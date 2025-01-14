def hackerlandRadioTransmitters(x, k):
    x = sorted(x)
    n = len(x)
    transmitters = 0
    i = 0

    while i < n:
        transmitters += 1
        loc = x[i] + k
        
        while i < n and x[i] <= loc:
            i += 1
        
        loc = x[i - 1] + k
        while i < n and x[i] <= loc:
            i += 1

    return transmitters


x = [9, 5, 4, 2, 6, 15, 12]

k = 1
answer = hackerlandRadioTransmitters(x, k)
print(answer)