import os
import re

# dir2dict(path,extension) generates a dictionary with directories as keys and lists of restframe.fits files as values  

def dir2dict(path,extension):
    directories = [x[0] for x in os.walk(path)] # creates a list of the directories in path
    fitfiles = {} # dictionary of _restframe.fits files {'directory':['_.fit','_.fit',...]}
    for dirs in directories:
        filenames = os.listdir(dirs) # lists all the files in each directory
        filelist = [] # list of files in dirs with the _restframe.fits ending
        for files in filenames:
            match = re.search('\._(.+)',files) # remove the "._" before some file names (I don't know why that's there)
            if match:
                files = match.group(1)
            if files.endswith(extension):
                filelist.append(files)    
        fitfiles[dirs] = filelist # matching a list of _.fits files (value) to each directory name (key)
    return fitfiles

# maxphase(fitfiles) generates a list of files at maximum phase

def maxphase(fitfiles):

    phasemaxfiles = []
    for dirs in fitfiles: # for each directory in the fitfiles dictionary
        for entry in fitfiles[dirs]: # i.e. for each _.fits file in each directory...
            match = re.search(r'_[PM](\d+)_',entry) # find the pattern indicating phase
            if match:
                phase = match.group(1)
            if int(phase) < 1000: # if the phase is maximal, add the file path to a list
                filepath = dirs + '/' + entry
                if filepath not in phasemaxfiles:
                    phasemaxfiles.append(filepath)
    phasemaxfiles.sort()    
    return phasemaxfiles

# writefile(phasemaxfiles,filename) writes the list to a text file. If the filenmame is taken, writefile prints the result instead.

def writefile(phasemaxfiles,path,filename):
    
    if not os.path.isfile(filename):
        outf = open(filename, 'w')
        outf.write('\n'.join(phasemaxfiles))
        outf.close()
    else:
        print 'File name already taken.'
        print '------------------------'
        print '\n'.join(phasemaxfiles)
    
def main():
    
    path = 'training/'
    extension = 'restframe.fits'
    filename = 'SNmaxphase.txt'
    
    fitfiles = dir2dict(path,extension)
    phasemaxfiles = maxphase(fitfiles)
    writefile(phasemaxfiles,path,filename)
    
if __name__ == '__main__':
  main() 