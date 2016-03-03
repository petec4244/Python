#A handy python script for untaring a file passed in as an arg

import tarfile, sys

def utar(fname):
    if(fname.endswith("tar.gz")):
        tar = tarfile.open(fname)
        tar.extractall()
        tar.close()
        print "Extracted in Current Directory"
	else if (fname.endswith("tar")):
		tar = tarfile.open(fname)
		tar.extractall()
		tar.close()
    else:
        print "Not a Tar.gz file : '%s '" % sys.argv[0]
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: '%s filename'" % sys.argv[0]
        sys.exit(0)
    utar(sys.argv[1])
