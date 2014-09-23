
#This allows writing/appending a textfile.
#Input 1  what to write
#Input 2  Where to write it.

import sys
import os

def writeReport(writeline, report):
    cwd = os.getcwd()
    if os.path.isfile(report):
        print("found file" + report+ " appending")
        with open(report, 'a')as theFile: #append existing file
            theFile.write(writeline)
            print("file appended")
    else:
        print("file not found, creating "+report)
        with open(report, 'w') as theFile: #start new file
            theFile.write(writeline)
            print("file written")


def main():
    if len(sys.argv) == 3:
        writeLine = sys.argv[1]
        report = sys.argv[2]
        writeReport(writeLine, report)
if __name__ == "__main__":
    main()
