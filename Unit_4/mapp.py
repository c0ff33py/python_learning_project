def fact(n):
    return 1 if n < 2 else n*fact(n-1)


results = map(fact, range(6))
print(results)

for i in results:
    print(i)
