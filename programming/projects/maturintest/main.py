import maturintest
import time

fac = 1
i = 1

# start
now = time.time()
while i < 10:
    fac = fac * i
    print(i, fac)
    i = i + 1
elapsed = time.time()
# end

print("Python Elapsed:", round(((elapsed - now) * 1000000), 2), "µs")
result = maturintest.facloop(1, 1)
for a in result:
    result = ' '.join(str(b) for b in a)
    print(result)
