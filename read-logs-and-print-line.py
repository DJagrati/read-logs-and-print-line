import os
import re

#Constants
ASSIGNMENT_DIR = os.path.dirname(os.path.abspath(__file__)) + "\Assignment2\\"
LOGS_DIR = ASSIGNMENT_DIR + "\Logs\\"

#Method to Open File in read Mode and return it's instance
def openFileInReadMode(folder, fileName: str):
    return open(folder + fileName, 'r', encoding="utf8")

#Method to Open File in read Mode and return it's instance
def closeFile(fileName):
    fileName.close()

#Method to find the index of line where particular KEyword is first found.
def findForLineNumber(file, keyword):
    for line in file:
        if keyword in line:
            break

#Find the name of log file according to the given pattern
def findPatternAfterGivenKeyword(file, keyword, pattern):
    findForLineNumber(file, keyword)
    reg = re.compile(pattern)
    matches = []
    for line in file:
        matches += reg.findall(line)
        if(len(matches) == 1):
            break
    return matches[0]

#Returns the required Line.
def printLineNextToGivenKeyword(file, keyword):
    findForLineNumber(file, keyword)
    return file.readline()
    
#MAIN BODY OF THE CODE:
# Operations performed on Start Assignment File    
file_startAssignment = openFileInReadMode(ASSIGNMENT_DIR, "start_assignment.log")
fileInLogFolder = findPatternAfterGivenKeyword(file_startAssignment, "beginning of assignment", "required_pattern_\d\d")
closeFile(file_startAssignment)

# Operations performed on Logs File found above
#_NOTE: I am printing the line above as part of my solution. This String can be stored and used for different pusposes. 
file_cmpltAssignment = openFileInReadMode(LOGS_DIR, fileInLogFolder)
print(printLineNextToGivenKeyword(file_cmpltAssignment, "assignment_completed"))
closeFile(file_cmpltAssignment)


