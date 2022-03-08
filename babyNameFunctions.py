def readBabyNamesFile(year):
  file = open("yob" + year + ".txt", 'r')
  names = []
  for line in file:
    line = line.strip()
    name = line.split(',')
    names.append(name)
  file.close()
  return names

def findBabyName(name, year):
	count = 0
	babies = readBabyNamesFile(year)
	for lists in babies:
		if lists[0] == name:
			count += int(lists[2])
	statement = "There were " + str(count) + " babies named " + name + " in " + year
	return statement

def numBabiesInRange(year, beg, end):
  babies = readBabyNamesFile(year)
  while True:
    if babies[0][0] == beg:
      break
    else:
      babies.pop(0)
  while True:
    if babies[len(babies)-1][0] == end:
      break
    else:
      babies.pop(len(babies)-1)
  count = 0
  for baby in babies:
    count += int(baby[2])
    statement = "There were " + str(count) + " babies born between " + beg + " and " + end
  return statement

def listInRange(year, min, max):
  babies = readBabyNamesFile(year)
  newList = []
  for baby in babies:
    if int(baby[2]) < int(max) and int(baby[2]) > int(min):
      newList.append(baby[0])
  return newList

def separateGender(year):
	fn = readBabyNamesFile(year)
	males = open("yob" + str(year) + "M.txt", 'w')
	females = open("yob" + str(year) + "F.txt", 'w')
	for each in fn:
		if each[1] == "M":
			print(each[0], file=males)
		if each[1] == "F":
			print(each[0], file=females)
	males.close()
	females.close()
	return "Done"
				
def createRangeFile(year, beg, end):
	filename = 'yob' + str(year) + '.txt'
	file_out = 'yob' + str(year) + 'R' + '.txt'
	in_file = open(filename, 'r')
	out_file = open(file_out, 'w')
	for line in in_file:
		str_line = line.strip()
		entry_list = line.split(',')
		name = entry_list[0]
		if name[0] == beg and name[-1] == end:
			print(entry_list[0], file = out_file)
	in_file.close()
	out_file.close()
	return "Done"