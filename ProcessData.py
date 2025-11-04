#ProcessData.py
#Name:Jadon Wiebe
#Date:11/04/2025
#Assignment:Lab 8

import random

def main():

  #Open the files we will be using
  Data = []
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')
  for line in inFile:
    info = line.split(" ")
    lastName = info[1]
    check = len(lastName)
    if check <5:
      need = 5-check
      for i in range(need):
        add = "X"
        last = lastName + add
    firstName = info[0]
    IDnum = info[3]
    user = firstName[0] + lastName + IDnum[8:]
    grade = info[5]
    major = info[6]
    grade_major = major[0:3] + " - " + grade[0:2]

    Data.append((lastName, firstName, user, grade_major))
  for line in Data:
    output = line[0] + ", " + line[1] + ", " + line[2] + ", " + line[3] + "\n"
    #check over last line
    outFile.write(output)


  #Process each line of the input file and output to the CSV file



  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
