import fileinput
import random

list1 = []
list2 = []
i = 0
for line in fileinput.input():
	if i == 0:
		list1.append(line[:-1])
		i = i + 1
	elif i == 1:
		list2.append(line[:-1])
		i = i + 1
	else:
		i = 0

while True:
	if len(list1) == 0:
		break
	ri = random.randint(0,len(list1)-1)
	print list1[ri]
	list1.pop(ri)
	ui = raw_input()
	if ui == "q":
		break

	if len(list1)%5 == 0:
		print list2[ri] + "\n\n=====================\n" + str(len(list1)) + " questions remaining\n=====================\n"
	
	else:
		print list2[ri] + "\n\n"	

	list2.pop(ri)
