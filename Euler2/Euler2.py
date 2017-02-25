fibonacci = [1]
current_number = 1
last_number = 1
temp = 1
while (current_number+last_number) < 4000000:
    i = 1
    temp = current_number
    current_number = current_number + last_number
    fibonacci.insert(i,current_number)
    last_number = temp
    i += 1
else:
    i = 1
    result = 0
    while i < len(fibonacci):
        if fibonacci[i] % 2:
            result = result + fibonacci[i]
        i += 1
    else:
        print(result)
