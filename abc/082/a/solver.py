from statistics import mean
import math

a, b = map(int, input().split())
print(math.ceil(mean([a, b])))

