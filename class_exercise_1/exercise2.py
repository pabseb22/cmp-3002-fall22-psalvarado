
input = input("Enter a number: ")
n = int (input)
sum = 0
operations = 0
for num in range(0, n+1, 1):
    sum = sum+num
    operations = operations + 1

print("SUM is equal to: ", sum , " And the number of operations was: ", operations)