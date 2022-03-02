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
	deez = readBabyNamesFile(year)
	for lists in deez:
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