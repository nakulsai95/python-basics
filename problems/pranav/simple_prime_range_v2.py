
prime_list = []
Uppr_limit = input("Uppr limit de ")
import time
start_time = time.time()
Uppr_limit = int(Uppr_limit)
Uppr_limit = Uppr_limit +1
R2 = range ( 2 , Uppr_limit )


for i in R2:
    if i > 1:
        for j in range(2,i):
            if i % j == 0 :
              break
        else:
            prime_list.append(i)


print(sum(prime_list))
print(time.time() - start_time)