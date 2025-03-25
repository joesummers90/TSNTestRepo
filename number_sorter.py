my_numbers = [8, 3, 6, 5, 3, 7, 3, 5, 4, 1]
changed = True
while changed == True:
    counter = 0
    changed = False
    while counter < len(my_numbers) - 1:
        if my_numbers[counter] > my_numbers[counter + 1]:
            smaller_number = my_numbers.pop(counter + 1)
            my_numbers.insert(counter, smaller_number)
            changed = True
            counter += 1
        else: 
            counter += 1
print(my_numbers)