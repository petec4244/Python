#this script is designed to read a text file and ignore any lines that begin with #
#params:
#1. Input file
#2. Output Type?, 1 = array to 1 line, 2 = line by line, 3 = future use.

import sys

formatted = ''
		
def run(command, Type):
	#f = open(command)
	lines = [line.strip() for line in open(command)]
	linesNoC = []
	
	for line in lines:
		if not line.startswith("#"):
		   # print(line)#debug
			if not line == '':
				if Type == '1':
					linesNoC.append(line)
				if Type == '2':
					printFmt(line)
				# if Type == '1':
					# print(line)
	if not len(linesNoC) == 0:
		if not Type == '2':
			counter = 0
			for line in linesNoC:
				if counter == 0:
					formatted = line
					counter = counter + 1
				else:
					formatted = formatted+','+line
			printFmt(formatted)


def printFmt(inlines):
	print(inlines)
	
def main():
	if len(sys.argv) == 3:
		run(sys.argv[1], sys.argv[2])
	else:
		print("\n\n#######\nArguments improperly formatted!!!\n\nExpected format: filename #\n\n#= type of output, 1 = comma sep lines \n2 = line by line output")
if __name__ == "__main__":
	main()
