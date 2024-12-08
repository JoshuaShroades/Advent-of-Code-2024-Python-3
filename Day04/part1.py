import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	total = 0
	SEARCH = "XMAS"
	for y in range(len(lines)):
		line = lines[y]
		for x in range(len(line)):
			char = line[x]
			if(char == SEARCH[0]):
				for b in range(max(0, y-1), min(len(lines), y+2)):
					for a in range(max(0, x-1), min(len(line), x+2)):
						if(lines[b][a] == SEARCH[1]):
							total += search((x,y), (a,b), SEARCH)
	return total

def search(pos:tuple[int], dir:tuple[int], string:str) -> int:
	vector = tuple([b-a for a,b in zip(pos,dir)])
	for i in range(len(string)):
		nextPos = [a+b*i for a,b in zip(pos,vector)]
		clampedPos = [max(0,min(len(lines[0])-1,nextPos[0])),max(0,min(len(lines)-1,nextPos[1]))]
		if(string[i] != lines[clampedPos[1]][clampedPos[0]] or nextPos != clampedPos):
			return 0
	return 1
