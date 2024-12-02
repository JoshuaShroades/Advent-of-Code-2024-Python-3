import os

fileDirectory = os.path.dirname(os.path.realpath(__file__))
inputFilePath = os.path.join(fileDirectory, "input.txt")

with open(inputFilePath) as inputFile:
	lines = [line[:-1] for line in inputFile]

def main():
	safeCount = 0
	for line in lines:
		values = [int(value) for value in line.split()]
		if(isValid(values)):
			safeCount += 1
		else:
			for i in range(len(values)):
				dampenedLine = values[:i] + values[i+1:]
				if(isValid(dampenedLine)):
					safeCount += 1
					break
	return safeCount

def isValid(values:list[int]) -> bool:
	if(values[0] > values[1]):
		increasing = False
	elif(values[0] < values[1]):
		increasing = True
	safeLine = True
	for i in range(len(values)-1):
		if(abs(values[i]-values[i+1]) in range(1,4)):
			if(not((increasing and values[i] < values[i+1]) or (not increasing and values[i] > values[i+1]))):
				safeLine = False
				break
		else:
			safeLine = False
			break
	return safeLine
