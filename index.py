# Create a Empty List

My_list = []
print('List : ', My_list)

# Create an Append

My_list = [10]
My_list.append(20)
My_list.append(30)
My_list.append(40)
print(My_list)

# Insert the value 15 at the second position in the list

My_list = [10, 20, 30, 40]
My_list.insert(1, 15)
print(My_list)

# Extend My_list with another list [50, 60, 70]
My_list = {10, 20, 30, 40}
print('Initial set:', My_list)
My_list.add(50)
My_list.add(60)
My_list.add(70)
print(My_list)

# Remove the last element from My_list
My_list = [10, 20, 30, 40]
discharged = My_list.pop(3)
print(f"Discharged: {discharged} → Remaining: {My_list}")

# sort My_list in ascending order
My_list = [70, 40, 10, 50, 20, 60, 30]
My_list.sort()
print(My_list)


# Find and print the index of the value 30 in My_list
My_list = [70, 40, 10, 50, 20, 60, 30]
for index, value in enumerate(My_list): 
    if value == 30:
        print(index)
