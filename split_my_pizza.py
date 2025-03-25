print("---Welcome to Split My Pizza---")
def input_slices():
    correct = False
    while (correct == False):
        print("How many slices are there on the Pizza?")
        try:
            number = int(input())
            correct = True
        except ValueError:
            print("You must enter a whole number")
    return number
slices = input_slices()
def input_people():
    correct = False
    while (correct == False):
        print("How many people are sharing?")
        try:
            number = int(input())
            correct = True
        except ValueError:
            print("You must enter a whole number")
    return number
people = input_people()
slices_per_person = slices // people
slices_remaining = slices % people
print(f"This means there will be {slices_per_person} slices each")
print(f"There will be {slices_remaining} slices remaining")
def input_total():
    correct = False
    while (correct == False):
        print("How much is the pizza")
        try:
            number = float(input())
            correct = True
        except ValueError:
            print("You must enter a number to two decimal places")
    return number
pizza_total = input_total()
slice_total = pizza_total / slices
cost_per_person = slice_total * slices_per_person
print(f"Total cost per person is £{cost_per_person}")
if slices_remaining > 0:
    print(f"Slices cost £{slice_total} each if anybody wishes to have an extra slice")