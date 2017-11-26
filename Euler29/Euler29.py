num_range = [2,100]

sequence = []

for i in range(num_range[0],num_range[1]+1):
	for j in range(num_range[0],num_range[1]+1):
		term = i**j
		if not term in sequence:
			sequence.append(term)

sequence = sorted(sequence)
print(len(sequence))
