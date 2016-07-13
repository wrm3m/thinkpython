

i = 0
again = ""

def repeatPr ( again, i):
    r = 0
    while r == 0:
        print('Do you whant to play again? Y/N')
        again = input()
        if again == 'Y':
            i = 0
            r = 1
        elif again == 'N':
            i = 1
            r = 1
        else:
            r = 0

while i==0:
    print('Hello what is your name?')
    yName = input()
    print('Hello '+ yName + ', what is your age?')
    yAge = input()    
    if int(yAge)>=110:
        print('bruh thats not possible')
        repeatPr(again, i)
    else:
        print('Oh so you are ' + yAge + ' years old huh..')
        print('Do you know that this means that you turn '+ str(int(yAge)+1)+ ' next year?')
        repeatPr(again, i)

print("Press enter to Quit")	
halt = input()


