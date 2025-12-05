import sys
arg1 = sys.argv[1]
print(f"Hello world with arg1: {arg1}")

x = 1
for i in range(1, 20):
    x = x + i * 2

print(f"The result is: {x}")
