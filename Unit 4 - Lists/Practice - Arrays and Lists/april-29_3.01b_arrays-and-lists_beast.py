###Programming Challenge - Beast###
number_list = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    number_list.append(num)


remove_num = float(input("The number you wish to remove from the list: "))
number_list.remove(remove_num)


print("The current data in the list:", number_list)
print("The length of the list:", len(number_list))
print("The total value of the list:", sum(number_list))
