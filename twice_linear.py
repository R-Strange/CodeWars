"""Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

Example:
dbl_linear(10) should return 22

Note:
Focus attention on efficiency"""
import time
def dbl_linear_old(n):
    y = lambda x: (2 * x) + 1
    z = lambda x: (3 * x) + 1

    u = [1]
    i = 0

    while i < n+1:
        x = u[i]
        u.append(y(x))
        u.append(z(x))
        u = sorted(list(set(u)))
        i += 1

    return u[n]
start_time = time.time()

print(dbl_linear_old(9999))

print("Process finished:", time.time() - start_time)
import heapq 

def dbl_linear(n):
    u = [1]
    existing = set(u)
    
    for i in range(n):
        x = heapq.heappop(u)
        for f in [2*x + 1, 3*x + 1]:
            if f not in existing:
                existing.add(f)
                heapq.heappush(u, f)
    return heapq.heappop(u)
start_time = time.time()
print(dbl_linear(9999))
print("Process finished:", time.time() - start_time)