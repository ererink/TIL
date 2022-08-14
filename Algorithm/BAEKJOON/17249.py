# 태보태보 총난타

taebo = input()
left_hook = ''
right_hook = ''

for i in range(len(taebo)):
    left_hook += taebo[i].split('(^0^)')
    taebo.replace(taebo[i], '')
    