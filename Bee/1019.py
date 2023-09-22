temp = int(input())

h = temp // 3600
m = (temp % 3600) // 60
s = (temp % 3600) % 60

print(f"{h}:{m}:{s}")
