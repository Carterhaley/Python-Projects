# Name: J. Carter Haley
# weightedAverages.py

#Problem: This program will use information provided by the user to
    #calculate the monthly payment required of a loan, the amount of
    #interest to paid over the life of the loan, and the total amount
    #paid over the life of the loan.

#Certification of Authority:
    #I certify that this lab is entirely my own work.
    
def weightedAverages():
##  The following line allows for the user to input a file name
    infileName = input("Enter the name of your grade file: ")
    
##  The next lines use the user's input to open the file in the program
    infile = open(str(infileName), "r")
    gradeFile = infile.read()
    
##  The next line splits the grade file by line
    gradeSplit= gradeFile.split("\n")
    
##  This line establishes an accumulation for the class
    total = 0
    
##  This loop uses each line of the split to calculate the averages
    for line in gradeSplit:
        averages = 0
        
##      This line splits the lines with each student's grades
        grades = line.split()

##      This loop calculates the averages by skipping the values in each
##      line by 2, and completing the equation given on the assignment
##      sheet.
        for i in range(2, len(grades),2):
            name = ""
            averages+= int(grades[i]) * int(grades[i+1])
            name += (grades[0]+ " "+ grades[1])

##      This line completes the average calc
        averages = averages/100
        total+= averages

        name += str(averages)

##      This line prints the name of the student and their average
        print(str(name), str(" ")), "${0:.1f}".format(averages)

##  These lines calculate the class average, and print it, respectively
    total = total/ (len(gradeSplit))
    print("Class Average: " + "{0:.1f}".format(total))
    

