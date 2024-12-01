import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	listA = []
	listB = []
	for line in lines:
		listPair = line.split("   ")
		listA.append(int(listPair[0]))
		listB.append(int(listPair[1]))
	listA.sort()
	listB.sort()
	zipList = zip(listA,listB)
	totalDistance = 0
	for pair in zipList:
		totalDistance += abs(pair[0]-pair[1])
	return totalDistance
