import ast
import string

alphabet = list(string.ascii_uppercase)

alphabet_dict = {}
for index, char in enumerate(alphabet):
	alphabet_dict[char] = index+1

file = open('p022_names.txt', 'r')
file_content = file.read()
file_content = '[' + file_content + ']'

file_content = ast.literal_eval(file_content)
names = [n.strip() for n in file_content]

names = sorted(names)

total_sum = 0

for index, name in enumerate(names):
	name_sum = 0
	for i, char in enumerate(name):
		name_sum += alphabet_dict[char]
	name_sum = name_sum*(index+1)
	total_sum += name_sum

print(total_sum)