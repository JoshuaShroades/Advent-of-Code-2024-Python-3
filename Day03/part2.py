import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	total = 0
	enabled = True
	data = ""
	for line in lines:
		data += line
	slicer = data.find("mul(")
	slicedLine = data[slicer:]
	while(slicer != -1):
		if(enabled):
			mul = slicedLine[len("mul("):slicedLine.find(")")]
			mulPair = mul.split(",")
			if(len(mulPair) == 2 and mulPair[0].isnumeric() and mulPair[1].isnumeric()):
				total += int(mulPair[0]) * int(mulPair[1])
			slicer = slicedLine.find("mul(",1)
			disable = slicedLine.find("don't()",1)
			if(slicer < disable or disable == -1):
				slicedLine = slicedLine[slicer:]
			else:
				enabled = False
				slicedLine = slicedLine[disable:]
		else:
			slicer = slicedLine.find("do()",1)
			slicedLine = slicedLine[slicer:]
			enabled = True
	return total
