
h, b, c, s = map(int, input().split())

print(round(h * b * c * s / 8 / 1024 / 1024, 1), "MB")