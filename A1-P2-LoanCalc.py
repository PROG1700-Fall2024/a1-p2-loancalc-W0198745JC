#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 
 "Student Name: Jenille Cheney"
"Program Name: Loan Calculator"
"Description: Program 2 Assignment 1"
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
# this is the Weekly loan calculator
    print("Weekly Loan Calculator")
    print("")
    print("")
# input the amount of loan (variable)
    loanAmount=input("Enter the amount of loan: ")
#input the interest rate (%)(variable)
    interestRate= input("Enter the interest rate (%): ")
#input the number of years (variable)
    NumYears=input("Enter the number of years: ")
# the calculations 
#i = interest rate (variable) / 5200
    weeklyInterest= float(interestRate)/5200  #bugged with int changed casting to float
# weekly payment = i/1 - (1+i)**(-52*years) * loan amount  (This took me AGES to figure out the ** for power of in code)
    WeeklyPayment= weeklyInterest/(1 - (1+ weeklyInterest) ** (-52*int(NumYears))) * int(loanAmount)
#so many parenthesis it was a challenge to figure out appropriate placement.
#your weekly payment will be ${0:.2f}
    print("")
    print("")
    print("Your weekly payment will be ${0:.2f}".format(WeeklyPayment))






    # YOUR CODE ENDS HERE

main()