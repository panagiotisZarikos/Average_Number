#Average number simple tool
import time

amount_of_num = int(input("How many numbers ? "))

sum = 0

for i in range(amount_of_num):

   numbers = float(input("Type a number "))

   sum += numbers

print("We are working on it , wait please")

time.sleep(4)

print(f"The average number is {sum / amount_of_num}")









 





