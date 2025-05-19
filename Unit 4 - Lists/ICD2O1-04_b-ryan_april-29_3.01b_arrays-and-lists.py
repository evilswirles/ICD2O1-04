###Programming Challenge: Rookie###
#numbers = ["1","2","3","4","5","6","7","8","9"]
#letters = ["A","B","C","D","E","F"]

#print(numbers)
#print(letters)


###Programming Challenge: Pro###
#week_day = ["Monday","Tuesday","Wednesday","Thursday","Friday"] #just the weekday
#week_day.append("Saturday") #adds Saturday onto the end of Friday
#week_day.append("Sunday") #adds Sunday onto the end of Friday

#print(week_day) #prints out the weekday, including the appended Saturday & Sunday


###Programming Challenge: Beast###
number_list = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    number_list.append(num)


remove_num = float(input("The number you wish to remove from the list: "))
number_list.remove(remove_num)


print("The current data in the list:", number_list)
print("The length of the list:", len(number_list))
print("The total value of the list:", sum(number_list))
