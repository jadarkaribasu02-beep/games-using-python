#finding largest number without uusing max functinon

k = list(map(int,input('enter numbers').split()))

largest = k[0]

for num in k:
    if num > largest:
        largest = num

print('largest is :',largest)