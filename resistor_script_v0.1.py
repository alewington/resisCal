#python
# Version 0.1
# resistor calculator


#Colours and values for resistor calculator.
#0 zero value rule ["0",band = 0 = black,mulitplier = 0 = ignore,tolerence = 0 = ignore, temp coefficent = 0 = ignore]
#0 for no band has value for 0 zero ie 0 has meaning and can't be ignored.4
band_Types = [
    
    ["Black",0,1,0,250],
    ["Brown",1,10,1,100],
    ["Red",2,100,2,50],
    ["Orange",3,1000,0,15],
    ["Yellow",4,10000,0,25],
    ["Green",5,100000,0.5,20],
    ["Blue",6,1000000,0.25,10],
    ["violet",7,10000000,0.1,5],
    ["Grey",8,100000000,0.05,1],
    ["White",9,1000000000,0,0],
    ["Gold",0,0.1,5,0],
    ["Silver",0,0.01,10,0],
    ["No Band",0,0,20,0]
]

band_checker = [    
    ["Black",1,1,1,1,0,1],
    ["Brown",1,1,1,1,1,1],
    ["Red",1,1,1,1,1,1],
    ["Orange",1,1,1,1,0,1],
    ["Yellow",1,1,1,1,0,1],
    ["Green",1,1,1,1,1,1],
    ["Blue",1,1,1,1,1,1],
    ["violet",1,1,1,0,1,1],
    ["Grey",1,1,1,1,0,1],
    ["White",1,1,1,0,0,0],
    ["Gold",0,0,0,1,1,0],
    ["Silver",0,0,0,1,1,0],
    ["No Band",0,0,0,1,0,0]
]


#banding selcting and reset.

#rules for resistor calculator
#bands 1-6 available
#bands 1-3 are for value, 4 is multiplier, 5 is tolerence, 6 is temp coefficent
#if 6 bands are selected then band 3 is for value, if 5 bands are selected then band 3 is for multiplier and band 4 is for tolerence, if 4 bands are selected then band 2 is for value, band 3 is for multiplier and band 4 is for tolerence.
#if 6 bands: band 1 is for value, band 2 is for value, band 3 is for value, band 4 is for multiplier, band 5 is for tolerence, band 6 is for temp coefficent
#if 5 bands: band 1 is for value, band 2 is for value, band 3 is for value, band 4 is for multiplier, band 5 is for tolerence
#if 4 bands: band 1 is for value, band 2 is for value, band 3 is for value, band 4 is for multiplier, band 5 is no band option
#if 3 bands: band 1 is for value, band 2 is for value, band 3 is for multiplier, band 4 is no band option for multiplier, band 5 is no band option for tolerence?
#no other options for 2 bands or 1 band as they are not valid for resistor calculation, but could be used for other purposes such as identifying the type of resistor or the manufacturer.
 
#band values, may be removed once identified and replaced with the below options.
#as listed.
band_Select = []



#menu 
"""
def main():
    while True:
        print("Resistor Calculator")
        print("1. Select Bands")
        print("2. Find Resistor Value")
        print("3. Reset Bands")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            select_bands()
        elif choice == "2":
            find_resistor_value()
        elif choice == "3":
            reset_bands()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")
"""    
    
#select
def band_Selection():
    band_Select = int(input("select band:"))
    return band_Select

def resistor_Selection():    
    bands_No = int(input("select number of bands:"))          
    return bands_No


def list_Resistors():
    print(("-"*20)*6)
    txt = "{0:^20}|{1:^20}|{2:^20}|{3:^20}|{4:^20}|{5:^20}|{6:^20}"
    print(txt.format("Colour","1st Band","2nd Band","3rd Band","Multiplier","Tolerence","Temp Coefficent"))
    print(("-"*20)*6)
    for x in band_Types:         
        print(f"{x[0]:^20}|{x[1]:^20}|{x[1]:^20}|{x[1]:^20}|{x[2]:^20}|{x[3]:^20}|{x[4]:^20}")
    
def list_Band():
    #list bands to select from, then select bands and assign to variables for calculation, then calculate and output result.
    print("Select Band")
    
    for i in band_Types:
        print(i, i[0])


#find

#append
def append_Band(band_Choice):
    band_Select.append(int(band_Choice))
    print(band_Select)
    return band_Select
    


#pop
def pop_Band(): 
    band_Select.pop(-1)
    print("Last selected band removed.")
    print(band_Select)
    return band_Select
    


#calculate
def calculate_Resistor():
    resistor_Select = resistor_Selection()
    
    x = 0
    
    while x < resistor_Select:        
        # type number for next band or p to pop last band or c to calculate or r to reset or e to exit
        band_Choice = input("Enter your choice: ")
        res = band_Choice.isdigit()
        if res == True:
            x+=1
            append_Band(band_Choice)
            continue      
        elif band_Choice == "p":
            x-=1
            pop_Band()
        elif band_Choice == "c":
            print("")
        elif band_Choice == "r":
            band_Select.clear()
            print("Bands reset.")
            print(band_Select)
            break
        elif band_Choice == "e":
            exit()
        else:
            print("Invalid choice, please try again.")
        
calculate_Resistor()
    


#display results

#reset

