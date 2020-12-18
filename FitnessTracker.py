import smtplib, ssl, random, csv
from argparse import ArgumentParser
from datetime import date
from tkinter import *
import requests, re, pandas as pd, time, webbrowser, sys
 
class GetWorkout:
    """ Program to generate a daily 7- day workout plan"""
    def __init__(self,name,height,weight,age,gender,email): 
        """Initializes a GetWorkout attribute
	    Attributes:
		    name: name attribute is initialized for the user information.
		    user_information: An empty dictionary attribute for storing user information.
 
        """
        self.name = name
        self.user_information = dict()
        self.workoutplan_list = list()
        self.user_hist_list = list()
        self.trainer = random.choice(['Jomer', 'Seungjoon', 'Lucy', 'Jonghyeong'])
        
    def user_info (self,name,height,weight,age,gender,email): 
        """Prompts users for name, height (inches), weight (pounds), age, gender (M/F) , and email to store user's information in the empty dictionary,
            and to calculate user's BMI and BRM.

        Args:
	        name(str): name of the user
            height(int): height of the user in inches
            weight (int): weight of user in pounds
            age (int): age of the user
            gender(str): male or female in 'M'/'F'
            email(str): email address of user

        Return:
            return user's information if an accout is new, otherwise print message.
        """
        self.user_information.update({name:{'height':height,'weight':weight,'age':age,'gender':gender,'email':email}})
        return (self.user_information)
        
           
    def bmi_calculator (self,height, weight): 
        """ Calculates BMI index using formula: BMI= 703*weight(lbs)/[height(in)]^2
        Args:
            name(str): name of the user
            height(int): height of the user in inches
            weight (int): weight of user in pounds

        Returns:
            BMI index and BMI health category 
        """
        BMI = (703 * int(weight)) / (int(height) ** 2)
        self.user_information[self.name].update({'BMI': BMI})
        return BMI
       
    def calories_calculator (self,height, weight, age, gender):
        """ Calculates calories using BMR formula:
        Args:
            height(int): height of the user in inches
            weight (int): weight of user in pounds
            age (int): age of the user
            gender(str): male or female in 'M'/'F'
        
        Returns:
            Estimated number of calories needed to maintain current weight
        """
        if gender == 'M':
            BMR = 66 + (float(6.3) * int(weight)) + (float(12.9) * int(height)) - (float(6.8) * int(age))
        else:
            BMR = 655 + (float(4.3) * int(weight)) + (float(4.7) * int(height)) - (float(4.7) * int(age))
            
        self.user_information[self.name].update({'BMR': BMR})
        if self.bmi_calculator(args.height,args.weight) < 18:
            return f'You are underweight. In order to gain 1 to 2 lbs per week, you need to increase your calorie intake by 20%, from {BMR} calories to {BMR + (BMR * .20)} calories.'
        elif self.bmi_calculator(args.height,args.weight) > 18.5 and self.bmi_calculator(args.height,args.weight) < 24.9:
            return f' Congrats! You are healthy. In order to maintain this weight you need to consume {BMR} calories daily.'
        elif self.bmi_calculator(args.height,args.weight) > 24.9:
            return f'You are overweight. In order to lose 1 to 2 lbs per week, you need to reduce your daily calorie intake by 20%, from {BMR} calories to {BMR - (BMR * .20)} calories.'
        
      
    def workoutplan(self, filename):
        """Generates the workout of the day.
        
        Args:           
            filename(str): contains a list of workout plans.
        Returns:
            (list) containing workout of the day.
            
        """
        open1 = open("counter.txt", "r") 
        counter1 = int(open1.read()) 
        if counter1 > 6:
            name = open("counter.txt", "w")
            name.write(str(0))
            name.close()
            raise Exception ("You have completed the workout for the week. Congrats!")
        with open(filename) as work_out:
            workout_file = csv.reader(work_out, delimiter = ',')
            for row in workout_file:
                day = row[counter1]
                if day not in self.user_hist_list:
                    self.workoutplan_list.append(day)
                    while "" in self.workoutplan_list:
                        del self.workoutplan_list[self.workoutplan_list.index("")]
        name = open("counter.txt", "w")
        name.write(str(counter1 + 1))
        name.close()
        return ('\n'.join(self.workoutplan_list))
    
    
    def video_tutorial(self,workout):
        """ Link to youtube tutorial according to workout plan day. 
        Args:
            workout(str): a string that will contain workout plans for the user.
        Side effects:
            Launching a web browser
        Returns:
           exercise(dictionary): Default value will be an empty dictionary and will add workout as a key and url(web address) as a value.
        """
        exercises_dict = dict()
        if day1: 
            webbrowser.open_new("https://www.youtube.com/watch?v=QXmdXilQaqA")
        elif day2:
            webbrowser.open_new("https://www.youtube.com/watch?v=LZlHNVNcxF8")
        elif day3: 
            webbrowser.open_new("https://www.youtube.com/watch?v=IXTp_Ww_4zY")
        elif day4: 
            webbrowser.open_new("https://www.youtube.com/watch?v=rHlb8yfdDzo")
        elif day5: 
            webbrowser.open_new("https://www.youtube.com/watch?v=zwAkH0XFrgw")
        elif day6: 
            webbrowser.open_new("https://www.youtube.com/watch?v=AesCuT1E_hw")
        elif day7: 
            webbrowser.open_new("https://www.youtube.com/watch?v=C4a0D36_e2E")
            
    def alert_popup(self, title, message, path):
        """Generate a pop-up window for special messages."""
        root = Tk()
        root.title(title)
        w = 400     # popup window width
        h = 200     # popup window height
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        m = message
        m += '\n'
        m += path
        w = Label(root, text=m, width=120, height=10, wraplength = 300)
        w.pack()
        b = Button(root, text="Thanks Coach!", command=root.destroy, width=15)
        b.pack()
        mainloop()
        
    def notification(self, arg):
        """ Sends an email to the user containing user' stats, BMI and BMR results, and the workout of the day, .
            
        Returns: 
            (str) = containing the message sent to the user.
        """
        
        port = 465 
        smtp_server = "smtp.gmail.com"
        sender_email = "fitnessplanexperiment@gmail.com"
        receiver_email = self.user_information[self.name]['email']
        password = input("Enter your password: ")
        #password = !QW@1qw2!QW@1qw2
        message = f"""\
        Subject: Today's Workout Plan {date.today()}

        Hi {self.name},

        According to the information you provided:
        
        {self.user_info(args.name,args.height,args.weight,args.age,args.gender,args.email)}
        
        Your Body Mass Index (BMI) is: {self.bmi_calculator(args.height,args.weight)} %.
        {self.calories_calculator(args.height, args.weight, args.age, args.gender)}
        
        Your Workout of the Day (WOD) has been prepared by {self.trainer}.
        
        {self.workoutplan(args.filename)}
        
        This message is sent from Python."""
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return message
        
        self.alert_popup(f"Today's Workout Plan", f'Your Body Mass Index (BMI) is: {self.bmi_calculator(args.height,args.weight)} %', 
                         f'{self.calories_calculator(args.height, args.weight, args.age, args.gender)}')
        
      
def parse_args(arglist): # only user_info arguments are constructed. Other arguments will later be constructed with more codes in main.
    """ parse command-line arguments.
    Args:
        arglist (list of str): list of command-line arguments.
 
    Returns:
        namespace: the parsed arguments
    """

    parser = ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("height", help="height of the user in inches")
    parser.add_argument("weight", help="weight of the user in pounds")
    parser.add_argument("age", help="age of the user")
    parser.add_argument("gender", help="gender of the user in 'M'/'F'")
    parser.add_argument("email", help="email of the user")
    parser.add_argument("filename", help="csv file")
    return parser.parse_args(arglist)
  
def main(name,height,weight,age,gender,email): # This main function currently takes the class and launches the user_info method using the user arguments and print out. In the future, there will be more applications using different methods.
    """ provide a space to store our arguments and execute desired plans.
   
    Args:
       name(str): name of the user
       height(int): height of the user in inches
       weight (int): weight of user in pounds
       age (int): age of the user
       gender(str): male or female in 'M'/'F'
       email(str): email address of user

    """
    g = GetWorkout(name,height,weight,age,gender,email)
    a = g.user_info(name,height,weight,age,gender,email)
    r = g.calories_calculator(height, weight, age, gender)
    b = g.bmi_calculator(height, weight)
    #h = g.user_history(GetWorkout)
    n = g.notification(a)
    print(n)

if __name__ == "__main__": # partially completed (only user_info method is currently running in main function)
    args = parse_args(sys.argv[1:])
    main(args.name,args.height,args.weight,args.age,args.gender,args.email)

    # Sample running code
    # python FitnessTracker.py Jong 70 175 20 M aengida@gmail.com workoutplan.csv
    # python3 FitnessTracker.py Jong 70 175 20 M aengida@gmail.com workoutplan.csv
    # password = !QW@1qw2!QW@1qw2
