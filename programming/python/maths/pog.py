import math
a=1/math.inf
check=math.inf
p=0
answer=a
while not math.isinf(p):
    answer = a + 1/answer
    p=p+1

print(answer)