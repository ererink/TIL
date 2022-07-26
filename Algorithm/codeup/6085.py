
w, h, b = map(int, input().split())

print(round(w * h * b / 8 / 1024 / 1024, 2), "MB")