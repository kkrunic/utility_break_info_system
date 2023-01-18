original_list = ["1", "2,3,4,5"]
new_list = []
for substring in original_list:
    numbers = substring.split(",")
    new_list.extend(numbers)
print(new_list)