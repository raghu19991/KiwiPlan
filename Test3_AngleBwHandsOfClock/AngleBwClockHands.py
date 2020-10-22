import os
from sys import platform
start = True
def calculate_angle(hr,mins):
    # Considering 12 in hour and 60 in minute as 0(starting point) in the clock
    hr=(0 if hr==12 else hr)
    mins=(0 if mins==60 else mins)
    # Converting minute equivalent of the hour hand i.e 4 hour position will be 20 min hand position
    hrToMin= hr*5
    
    # Calculating the number of minutes between the hands
    min_diff=(hrToMin-mins if hrToMin>mins else mins-hrToMin)
    
    # Converting minutes between hands to angle as each minute is a 6 degree angle
    angle_Bw_Hands=min_diff*6
    
    # Calculating relative movement of the hour hand with respect to minute hand. i.e a 360 deg movement of Min Hand ~ 30 deg(1 hr) movement of Hr hand
    # So for every 1 degree movement of minute hand hour hand moves 30/360 degrees
    rel_mov=30/360
    
    # Actual angle is difference in angle between the hour hand and minute hand - the relative movement that hour hand had while the minute hand moved to its position
    actual_angle=angle_Bw_Hands-rel_mov*mins
    
    return actual_angle

def inputs():
    while start:
        hr=input("\nHour Hand: ")
        mins=input("Minute Hand: ")
        try:
            # Validating if input is numeric
            hr=int(hr)
            mins=int(mins)
        except (ValueError,TypeError):
            print(''' \nOnly Numbers are accepted\nPlease try again ''')
            continue
        
        # Validating if hour hands and minute hands are in acceptable ranges
        if not (0<=hr<=12 and 0<=mins<=60): 
            print('''\nHours can only be between 0-12 and Min between 0-60\nPlease try again''')
            continue
        
        true_angle=calculate_angle(hr,mins)
        print(("The exact angle between the hands of the clock is {}".format(true_angle)))
        print("")
        ans = input("Try another one?(y/n)")

        if ans.lower() in ['y','1','yes','true','yeah']:
            if platform == "linux" or platform == "darwin":
                os.system('clear')  # For Linux/OS X
            if platform == "win32":
                os.system('cls')  # For Windows
            continue
        else:
            print("GoodBye")
            exit()
    

if __name__ == "__main__":
    print("Enter the Clock Hand values")
    inputs()
    
    
