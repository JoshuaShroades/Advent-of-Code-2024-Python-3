import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	total = 0
	for line in lines:
		slicer = line.find("mul(")
		slicedLine = line[slicer:]
		while(slicer != -1):
			mul = slicedLine[len("mul("):slicedLine.find(")")]
			mulPair = mul.split(",")
			if(len(mulPair) == 2 and mulPair[0].isnumeric() and mulPair[1].isnumeric()):
				total += int(mulPair[0]) * int(mulPair[1])
			slicer = slicedLine.find("mul(",1)
			slicedLine = slicedLine[slicer:]
	return total
