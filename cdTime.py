# Name: J. Carter Haley
# cdTime.py

#Problem: This program aims to help your friend, Jimmy, by creating a
#program that can output the total time for each cd in his shop both
#individually and as a whole.

#Certification of Authority:
    #I certify that this lab is entirely my own work.
    

#The input that the user will provide would include: the number of cds
# the number of tracks on each cd, and the time of each track in minutes,
#and seconds. The program's outputs will include: the time on each CD,
#and the time on all CDs together.

#Pseudocode is expressed in the comments throughout the program.


#This program, with the interaction and input of the user, will
#help Jimmy catalog the CDs in his shop

def cdTime():
    #This line establishes a variable for how many tracks the user has
    #on their cd
    numCd = eval(input("How many CD's would you like to catalog?: "))
    #This line sets the total for the accumulation to zero
    total=0
    #this line prints a statement to inform the user
    print("Alright, Let's get some information about your CD(s).")
    #The following is a loop that allows the program to determine how
    #many CDs the user will need to enter 
    for cd in range(numCd):
        print("CD", cd+1)
        #This line determines how many tracks are on each CD 
        numTracks = eval(input("How many tracks are on your CD(s): "))
        minutes = 0
        seconds = 0
        print()
        #This loop uses numTracks to determine the time on all of the
        #tracks together
        for tracks in range(numTracks):
            print()
            print("Track", tracks+1)
            #minSum & secSum are variables that the loop uses to
            #determine the time on each track/cd
            minSum = 60 * eval(input("How  many minutes? :"))
            secSum = eval(input("How many seconds? :"))
            #This line sets the total accumulator equal to the number
            #of seconds on the tracks
            total += minSum + secSum
            #The next three equations determine the hours, minutes,
            #and seconds, respectively.
            hours = total // 3600
            minutes = (total- ((hours*3600)))//60
            seconds = (total- ((hours*3600+minutes*60)))
            minutes_cd = minutes+(hours*60)
            print()
            
    
        print("CD", cd+1, minutes_cd, "minutes", seconds,
              "seconds")
            #print(seconds)
        



        print()
#This line outputs the total time on all CDs entered by the user

    print("Total Time on CD(s): ", hours, "hours", minutes, "minutes",
          seconds, "seconds""\n")
       

