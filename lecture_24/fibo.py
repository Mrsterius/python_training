def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)

# print(fibo(3))

def fiboDP(n, memory):
    if n < 2:
        return n

    if memory.get(n):
        return memory.get(n)

    total = fiboDP(n-1, memory) + fiboDP(n-2, memory)
    memory[n] = total
    return total

print(fiboDP(50, {}))