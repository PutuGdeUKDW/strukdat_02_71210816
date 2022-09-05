import timeit
def fib_iteratif(n):
    f1 = 0
    f2 = 1
    for i in range(0, n):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f1

def fib_rekursif(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_rekursif(n-1) + fib_rekursif(n-2)

n = 100
for i in range (1,n+1):
    start_time = timeit.default_timer()
    data = fib_iteratif(i)
    end_time = timeit.default_timer()
    print('Iterasi', i, 'dengan fungsi iteratif: ', end_time - start_time, 'detik')

print("==================================")

for i in range (1,n+1):
    start_time1 = timeit.default_timer()
    data = fib_rekursif(i)
    end_time1 = timeit.default_timer()
    print('Iterasi', i, 'dengan fungsi rekursif: ', end_time1 - start_time1, 'detik')



