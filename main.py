import day13.day13 as day
import time as t
print()

time = t.perf_counter()

solution = day.solve()
print(solution)



with open("output.txt","w") as file:
    file.write(str(solution))
    
print("Success")

runtime = t.perf_counter() - time
print(f"{1000 * runtime} ms")