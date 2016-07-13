

i = 0
again = ""

def repeatPr ( again, i):                           #function to rather stop or restart the script
    r = 0
    while r == 0:                           
        print('Do you whant to play again? Y/N')
        again = input()
        if again == 'Y':                            #check if Y or N
            i = 0                                   #restart the script
            r = 1                                   #stop the function
        elif again == 'N':
            i = 1                                   #stop the main infinite while loop aka whole script
            r = 1                                   #stop the function
        else:
            r = 0                                   #everything that is not Y or N ends in a restart of the function

while i==0:
    print('Hello what is your name?')
    yName = input()
    print('Hello '+ yName + ', what is your age?')
    yAge = input()    
    if int(yAge)>=110:                              #age check
        print('bruh thats not possible')
        repeatPr(again, i)                          #call function for the restart check
    else:
        print('Oh so you are ' + yAge + ' years old huh..')
        print('Do you know that this means that you turn '+ str(int(yAge)+1)+ ' next year?')
        repeatPr(again, i)

print("Press enter to Quit")	
halt = input()  


