print("Day 20 of 100 Days of Python! Today we are doing a number list generator!")
print()
starting_number = int(input("Pick a starting number: "))
ending_number = int(input("Pick an ending number: "))
increment = int(input("Pick an increment: "))
for i in range(starting_number, ending_number, increment):
  print(i)