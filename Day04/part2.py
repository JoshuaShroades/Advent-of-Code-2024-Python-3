import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	total = 0
	for y in range(1, len(lines)-1):
		line = lines[y]
		for x in range(1, len(line)-1):
			char = line[x]
			if(char == "A"):
				tl = lines[y-1][x-1]
				tr = lines[y-1][x+1]
				bl = lines[y+1][x-1]
				br = lines[y+1][x+1]
				if(tl == "M" and br == "S" or tl == "S" and br == "M"):
					if(tr == "M" and bl == "S" or tr == "S" and bl == "M"):
						total += 1
	return total
