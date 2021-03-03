import string

numbers_dict = {x: i+1 for i, x in enumerate(string.ascii_uppercase)}


with open("p022_names.txt", "r") as file:
    data = file.read()
    result = 0
    for i, name in enumerate(sorted(data.split(","))):
        name_sum = sum([numbers_dict[x] for x in name.strip("\"")])
        result += name_sum * (1+i)

print(result)
