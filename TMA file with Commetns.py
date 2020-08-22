#How this program is planned to work
#I don't care about adding or recording previous interest rate and bonus interest gained
#cus it will be troublesome to deduct, too many condition
#thats why I have initialised a list to store all the selections that the user will be inputting throughout the entire code
#instead of purely adding and subtracting value for the interest rate, i just reset it back to starting interest at the start of the main() while loop
#instead all future interest rate calculation is purely based of the storeselection list

# Do refer to all the functions below main(), easier to understand the code

#put this here, cus i will be resuing it at every while loop in main()
starting_interest = 0.05

#store all the inputs and balance, how inputs are store are explained in lines 14 to 20
storeSelection = [0,0,0,0,0,0,0]

#0: available balance
#1: spending selection
#2: salary credit selection
#3: invest selection
#4: insure selection
#5: bill Payment
#6: interest rate

def main():
    
    #pull in the defined storeSelection variable for outside the main().
    global storeSelection

    #Menu stored in a dictionary, can be excluded 
    mainMenu = {}
    mainMenu[0] = "=====Main Menu===="
    mainMenu[1] = "1: Spending range"
    mainMenu[2] = "2: Salary Credit?"
    mainMenu[3] = "3: Invest?"
    mainMenu[4] = "4: Insure?"
    mainMenu[5] = "5: Bill Payment?"
    mainMenu[6] = "0: Exit Program"
    
    
    
    while True:
        
        if storeSelection[0] == 0:
            averageBalance = inputValidation(1, "Enter your estimated Bonus$aver average daily balance: S$ ")
            storeSelection[0] = averageBalance
            
        #reset previosu interest rate to default 0.05
        storeSelection[6] = starting_interest
        
        #to exclude printing main menu, just remove "mainMenu" from line 42.
        #similar to line 66 (nearest example)
        #applies to spendingMenu 
        mmselection = inputValidation(1, "Please enter a selection: ", mainMenu)
        
        
        if mmselection == 1:
            spendingMenu = {}
            spendingMenu[0] = "==Select Spending Range=="
            spendingMenu[1] = "1: Less than S$500"
            spendingMenu[2] = "2: S$500 to S$1,999"
            spendingMenu[3] = "3: S$2,000 or greated"
            
            
            spendingSelection = inputValidation(1, "Please select a range: ", spendingMenu)
            storeSelection[1] =  spendingSelection
            
            calcaulateInterestRate(storeSelection)
            
            printInterest(storeSelection)
            
            continue
        elif mmselection == 2:
            
            #first application of the inputValidation function for string inputs and also no menu in the parameter
            salary_Credit = inputValidation("Y", "Would your monthly salary credit be S$3000 ore more? (Y/N): ")
            
            #stores previous input in respective place
            storeSelection[2] = salary_Credit
            #recalculate 
            calcaulateInterestRate(storeSelection)
            printInterest(storeSelection)
            
            #'continue' allows to reloop through, explained further in line 149 within the inputValidation function
            continue
            
        elif mmselection == 3:
            #literally a repeat of lines 73 to 84 just differnt question
            investSelection = inputValidation("Y", "Would you invest in eligible products? (Y/N): ")
            storeSelection[3] = investSelection
            calcaulateInterestRate(storeSelection)
            printInterest(storeSelection)
            
            continue  
        
        elif mmselection == 4:
            #literally a repeat of lines 73 to 84 just differnt question
            insureSelection = inputValidation("Y", "Would you insure in eligible products? (Y/N): ")          
            storeSelection[4] = insureSelection
            calcaulateInterestRate(storeSelection)
            printInterest(storeSelection)
            
            continue  
        
        elif mmselection == 5:
            #literally a repeat of lines 73 to 84 just differnt question
            billSelection = inputValidation("Y", "Would you make at least 3 bill payments online? (Y/N): ")
            storeSelection[5] = billSelection
            calcaulateInterestRate(storeSelection)
            printInterest(storeSelection)
            
            continue  
        
        #allow for user to exit the program :) can be not needed, up to you. i just think its neat.
        elif mmselection == 0:
            break
        else:
            #i think this no longer do anything, cus errors are already handle by inputValidation()
            #handles error
            print("Please enter a valid option.")
            continue
        
        
        return

#this function works on 2 very different input, string and integers, 
#so to decide which validation
#   typeofCommand defines either a string or integer type verification, no need to strictly use "y" or 1 respectively, any string or integer will do
#   message defines the prompt that will be displayed
#   menu is already defined as a empty menu so no conflict will be raiased if you do not pass a dictionary through it.add
#       downside is, all menus need to be stored in a dictionary. 
def inputValidation(typeofCommand, message, menu = {}):
    #main point of this function is to deal with @ssholes who enter other data types when asking to enter string or integer
    #starts a loop
    while True:
        
        #if you have passed a menu dictionary, lines 119 to 121 will get triggered
        if menu != None:
            for i in menu.keys():
                print(menu[i])
            
        #checks to check to string or integer input based off 'typeofCommand'
        if isinstance(typeofCommand, str):
            #try and except loop to handle error checking
            try:
                value = str(input(message))
            # ValueError is when you enter a int when input is asking for str. 
            except ValueError:
                print("Please enter a valid option") 
                #'continue' goes to the next iteration of the loop (for 'FOR' loops) 
                # but for "WHILE" loop, it just exits the current loop and restarts from the top at line 119
                continue
            else:
                break  
        
        #same thing with the string validation but with int
        if isinstance(typeofCommand, int):
            try:
                value =  int(input(message))    
            except ValueError:
                print("Please enter a valid option")
                continue
            else:
                break
    #at the very end, if all validation passed, return the inputed value 
    return value
    

def calcaulateInterestRate(storedList):
    
    #calculates rates purely based of the storeSelection List.
    #as mentioned, the indexes are reserved for the following values
        #0: available balance
        #1: spending selection
        #2: salary credit selection
        #3: invest selection
        #4: insure selection
        #5: bill Payment
        #6: interest rate

    #FOR loop to loop through index, 1, 2, 3, 4, 5 and not 6
    #index 6 is excluded, thats how the range func work
    for i in range(1,6):
        if i == 1:
            if storedList[i] == 2:
                storedList[6] += 0.25
                continue
            elif storedList[i] == 3:
                storedList[6] += 0.75
                continue
            else:
                storedList[6] = starting_interest
                continue
        elif i == 2:
            if storedList[i] == 0:
                continue
            if storedList[i].upper() == 'Y':
                storedList[6] += 0.40
                continue
            
        elif i ==  3:
            if storedList[i] == 0:
                continue
            if storedList[i].upper() == 'Y':
                storedList[6] += 0.85
                continue
        
        elif i == 4:
            if storedList[i] == 0:
                continue
            if storedList[i].upper() == 'Y':
                storedList[6] += 0.85
                continue
        
        elif i == 5:
            if storedList[i] == 0:
                continue
            if storedList[i].upper() == 'Y':
                storedList[6] += 0.10
                continue
   

def printInterest(storeList):
    
    #print the annual interest thingy to make it nice nice.
    #no need to keep retyping, cus formating string is a pain.
    gainedInterest = calculatedInterest(storeList)
    
    print("Your estimated annual interest is S${0:.2f} @ {1:.2f}%p.a".format(gainedInterest, storeList[6]))
    print("\n")
    return
    
    

def calculatedInterest(storeList):

    
    #temporary value assigned to interest
    #i believe there will be a reference error if interest is not defined before teh if else
    #404 cus that error XD
    interest = 404
    #takes into account with balance is more than 80000
    if storeList[0] > 80000:
        #if so, calcaulate 80000's interest ammount 
        #then calcalate the extra based of starting interest of 0.05%
        temp_extra = storeList[0] - 80000
        temp_extra *= starting_interest/100
        
        bonus = 80000 * (storeList[6]/100)
        interest = bonus + temp_extra
        return interest
    else:
        interest = storeList[0] * (storeList[6]/100)
    
    return interest






#good practice to use 
#def main()
#and line 246 and 247
if __name__ == '__main__':
    main()
    
    
    
    
    
x= 4

def meh():
    x =  5
    print(x)
    
    
meh()
print(x)


    
