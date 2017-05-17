from Tkinter import *
import tkFileDialog
import os
import sys

"""Script to run Sed commands without changing much"""

file_opt = options = {}

def run():
    if isdirVar.get() == 1: #determine file or path
        performSed(recursepath(), 1)
    else:
        performSed(fileVar.get())

def recursepath():
    fileList = []
    for foldername, subfolders, filenames in os.walk(fileVar.get()):
        for filename in filenames:
            found = "%s/%s" %(foldername, filename)
            fileList.append(found)
    return fileList

def performSed(files, isList = 0):
    from subprocess import call, Popen, PIPE
    sedCmnd = "sed s/%s/%s/g -i " % (findVar.get(), replaceVar.get())
    if(isList == 1):
        for file in files:
            sedCmnd2 = sedCmnd + file
            if verbose.get() == 1:
                print("Performing sed on %s" % file)
            call(sedCmnd2, shell=True)
    else:
        sedCmnd = sedCmnd + files
        if verbose.get() == 1:
            print("Performing Sed on %s" % files)
        call(sedCmnd, shell=True)
    statusVar.set("Sed Complete")

def openfiledialog():
    if isdirVar.get() == 1:
        fileVar.set(tkFileDialog.askdirectory(**file_opt))
    else:
        fileVar.set(tkFileDialog.askopenfilename(**file_opt))
    statusVar.set("Opened %s" % fileVar.get())

def inputclear():
    if clrReplace.get()==1:
        replaceVar.set("")
    if clrFile.get()==1:
        fileVar.set("")
    if clrFile.get()==1:
        findVar.set("")
    statusVar.set("Cleared Requested fields")

rt = Tk()
rt.title("PySed")

#bools/checkboxes
isdirVar   = IntVar()
clrReplace = IntVar()
clrFile    = IntVar()
clrFind    = IntVar()
verbose    = IntVar()

#strings
replaceVar = StringVar()
fileVar    = StringVar()
findVar    = StringVar()
statusVar  = StringVar()

Label(rt, text="     Input File or Path     ").pack()
Entry(rt, textvariable=fileVar, width=40).pack()
Button(rt, text="Select File/Dir", command=(lambda:openfiledialog()),width=30).pack()
Checkbutton(rt, text="Open A Directory", variable=isdirVar).pack()
Label(rt, text="=============================").pack()
Label(rt, text="        Find String          ").pack()
Entry(rt, textvariable=findVar, width=40).pack()

Label(rt, text="      Replace String         ").pack()
Entry(rt, textvariable=replaceVar, width=40).pack()
Button(rt, text="Run SED", command=(lambda:run()),width=30).pack()
Label(rt, text="=============================").pack()

Label(rt, text="        Clear Field(s)        ").pack()
Checkbutton(rt, text="  Find String    ", variable=clrFind).pack()
Checkbutton(rt, text="  Replace String", variable=clrReplace).pack()
Checkbutton(rt, text="  File/Dir String", variable=clrFile).pack()
Button(rt, text="Clear Selection(s)", command=(lambda:inputclear()),width=30).pack()


Label(rt, text="=============================").pack()
Checkbutton(rt, text="Verbose Output", variable=verbose).pack()
Label(rt, text="           Status            ").pack()

Entry(rt, textvariable=statusVar, width=40).pack()
Button(rt, text="Exit", command=(lambda:sys.exit()),width=30).pack()

rt.mainloop()
