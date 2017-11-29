import timeit

s = """
a = {str(n) for n in range(100000)}
b = {str(n) for n in range(100000)}
a & b
"""

exec_time = timeit.timeit(stmt=s, number=1)

print(exec_time)
