# Name: J. Carter Haley
# Usury.py

#Problem: This program will use information provided by the user to
    #calculate the monthly payment required of a loan, the amount of
    #interest to paid over the life of the loan, and the total amount
    #paid over the life of the loan.

#Certification of Authority:
    #I certify that this lab is entirely my own work.
    

#The input that the user will provide would include: the intial amount
#of the loan (principal), the interest rate of the loan, and finally the
#amount of time over which the loan will be repaid. The program's
#outputs will include: The necessary monthly payment, the amount of
#interest that will be paid over the course of the loan, and the
#complete amount that will be paid over the course of the loan.

#Pseudocode is expressed in the comments throughout the program.


#This program, with the interaction and input of the user, will
#calculate the principal payments per month, the interest, and the total
#amount that will be paid over the period of a loan.

def monthlyPayment():
#This line will print the statement: Hello, let's determine your monthly
#principal payment, which helps the user understand why they are enter-
#ing their information into the program.
    print("Hello, let's determine your monthly principal payment.")

    #this line will print a blank line, which helps with readability
    print()

#this line establishes the variable 'principal', which will be used
#later in the program to calculate the monthly payment, interest paid,
#and the total amount paid. It is equal to the intial amount of the
#loan.
    principal = eval(input("What was the intial amount of your loan? "))

#this line established the variable 'interestRate', which will be used
#later in the equation to calculate the monthly payments.
    interestRate = eval(input("What is the loan's interest rate? "))

#this line establishes the variable 'months'which will be used later in
#the equation to calculate the monthly payments.
    months = eval(input("How many months to repay the loan? "))

#this line establishes the variable 'rate', which which will be used
#later in the equation to calculate the monthly payments.
    rate = ((interestRate) / 1200)

#this line establishes the variable 'numerator', which is an equation
#and a component of the equation used to calculate the user's monthly
#payments (payments).
    numerator = (principal * (rate * ((1+rate) ** months)))

#this line establishes the variable 'denominator', which is an equation
#and a component of the equation used to calculate the user's monthly
#payments (payments).
    denominator = (((1+rate) ** months) - 1)

#this line establishes the equation 'payments' using the variables
#established above to calculate the user's monthly payments for
#their loans
    payments = (numerator / denominator)

#this line establishes the equation 'total' using established variables
#to calculate the total amount that must be paid for the loan.
    total = (payments * months)

#this line establishes the equation 'interest', which claculates the
#amount of interest that the user pays over the course of the loan.
    interest = ((months * payments) - principal)

#this line prints the statement in quotes to make it clear to the user
#that the figure that the program outputs represents.
    print("Principal payment each month: ", "$", payments)

#this line prints a blank line to make the output look neater
    print()

#this line prints the statement in quotes to make it clear to the user
#what the figure that the program outputs represents.
    print("Total interest paid: ","$", interest)

#this line prints a blank line to make the output look neater
    print()

#this line prints the statement in quotes to make it clear to the user
#what the figure that the program outputs represents.
    print("Total amount paid: ", "$", total)

#this line prints a blank line to make the output look neater
    print()
    


