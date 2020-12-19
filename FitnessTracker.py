import smtplib
import ssl
import random
import csv
import time
import webbrowser
import sys
import requests
import re
import pandas as pd
from argparse import ArgumentParser
from datetime import date
from tkinter import *


class GetWorkout:
    """ Program to generate a daily 7- day workout plan"""

    def __init__(self, name, height, weight, age, gender, email):
        """Initializes a GetWorkout attribute
        Attributes:
            name: name attribute is initialized for the user information.
            user_information: An empty dictionary attribute for storing user
                information.

        """
        self.name = name
        self.user_information = dict()
        self.workoutplan_list = list()
        self.user_hist_list = list()
        self.trainer = random.choice(
            ['Jomer', 'Seungjoon', 'Lucy', 'Jonghyeong'])

    def user_info(self, name, height, weight, age, gender, email):
        """Prompts users for name, height (inches), weight (pounds), age, 
        gender (M/F) , and email to store user's information in a dictionary 
        and to calculate user's BMI and BMR.

        Args:
            name(str): name of the user
            height(int): height of the user in inches
            weight (int): weight of user in pounds
            age (int): age of the user
            gender(str): male or female in 'M'/'F'
            email(str): email address of user

        Return:
            (dict): return user's personal information.
        """
        self.user_information.update(
            {name: {'height': height, 'weight': weight, 'age': age,
                    'gender': gender, 'email': email}})
        return (self.user_information)

    def bmi_calculator(self, height, weight):
        """ Calculates Body Mass Index (BMI) and updates to user's dictionary.
        Args:
            height (int): height of the user in inches.
            weight (int): weight of user in pounds.

        Returns:
            (float): BMI percentage.
        """

        BMI = (703 * int(weight)) / (int(height) ** 2)
        return BMI

    def calories_calculator(self, height, weight, age, gender):
        """ Calculates calories intake using the Basal Metabolic Rate (BMR) 
        formula:

        Args:
            height(int): height of the user in inches
            weight (int): weight of user in pounds
            age (int): age of the user
            gender(str): male or female in 'M'/'F'

        Returns:
            (str): Health category and estimated number of calories needed in 
            order to gain, maintain or lose weight.

        """
        if gender == 'M':
            BMR = 66 + (float(6.3) * int(weight)) + (float(12.9)
                                                     * int(height)) - (float(6.8) * int(age))
        else:
            BMR = 655 + (float(4.3) * int(weight)) + (float(4.7)
                                                      * int(height)) - (float(4.7) * int(age))

        self.user_information[self.name].update({'BMR': BMR})
        if self.bmi_calculator(height, weight) < 18:
            return f'You are underweight. In order to gain 1 to 2 lbs per week,'\
            f'you need to increase your calorie intake by 20%, from {BMR}'\
            f'calories to {int(BMR + (BMR * .20))} calories.'
        elif self.bmi_calculator(height, weight) > 18.5 and\
                self.bmi_calculator(height, weight) < 24.9:
            return f'Congrats! You are healthy. In order to maintain this weight'\
            f'you need to consume {int(BMR)} calories daily.'
        elif self.bmi_calculator(height, weight) > 24.9:
            return f'You are overweight. In order to lose 1 to 2 lbs per week, '\
            f'you need to reduce your daily calorie intake by 20%, from {int(BMR)}'\
            f' calories to {int(BMR - (BMR * .20))} calories.'

    def workoutplan(self, filename):
        """Generates the workout of the day by reading through a file.

        Args:           
            filename(str): contains a list of workout plans.

        Side Effect:
            Adds (1) to the counter.txt everytime the program is executed.

        Returns:
            (list): containing workout of the day.

        """
        open1 = open("counter.txt", "r")
        counter1 = int(open1.read())
        if counter1 > 6:
            name = open("counter.txt", "w")
            name.write(str(0))
            name.close()
            raise Exception(
                "You have completed the workout for the week. Congrats!")
        with open(filename) as work_out:
            workout_file = csv.reader(work_out, delimiter=',')
            for row in workout_file:
                day = row[counter1]
                if day not in self.user_hist_list:
                    self.workoutplan_list.append(day)
                    while "" in self.workoutplan_list:
                        del self.workoutplan_list[self.workoutplan_list.index(
                            "")]
        name = open("counter.txt", "w")
        name.write(str(counter1 + 1))
        name.close()
        return ('\n'.join(self.workoutplan_list))

    def video_tutorial(self, filename):
        """ Contains links to YouTube tutorial videos according to workout plan 
        day. 

        Args:
            filename(str): file that contains workout of the day for the user.

        Side effects:
            Launches a web browser.
        """
        open1 = open("counter.txt", "r")
        counter1 = int(open1.read())
        if counter1 == 0:
            webbrowser.open_new("https://www.youtube.com/watch?v=QXmdXilQaqA")
        elif counter1 == 1:
            webbrowser.open_new("https://www.youtube.com/watch?v=LZlHNVNcxF8")
        elif counter1 == 2:
            webbrowser.open_new("https://www.youtube.com/watch?v=IXTp_Ww_4zY")
        elif counter1 == 3:
            webbrowser.open_new("https://www.youtube.com/watch?v=rHlb8yfdDzo")
        elif counter1 == 4:
            webbrowser.open_new("https://www.youtube.com/watch?v=zwAkH0XFrgw")
        elif counter1 == 5:
            webbrowser.open_new("https://www.youtube.com/watch?v=AesCuT1E_hw")
        else:
            webbrowser.open_new("https://www.youtube.com/watch?v=C4a0D36_e2E")
        open1.close()

    def alert_popup(self, title, message, path):
        """Generates a pop-up window with a message.

        Args:
            title(str): title of the message box.
            message(str): primary message.
            path(str): seconday message.

        Side Effect:
            Calls the video_tutorial method once the user clicks on the button 
            provided in the message box.

        """
        root = Tk()
        root.title(title)
        w = 400
        h = 200
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        m = message
        m += '\n'
        m += path
        w = Label(root, text=m, width=120, height=10, wraplength=300)
        w.pack()
        b = Button(root, text=f"Workout video of the day!", command=lambda:
                   self.video_tutorial(
                       args.filename), width=20)
        b.pack()
        mainloop()

    def notification(self, arg):
        """ Sends an email to the user containing their Body Mass Index 
        percentage and recommended Calories Intake to either gain, maintain 
        or lose weight. 

        Returns: 
            (str) = containing the message sent to the user.
        """

        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "fitnessplanexperiment@gmail.com"
        receiver_email = self.user_information[self.name]['email']
        password = input("Enter your password: ")
        # password = !QW@1qw2!QW@1qw2
        message = f"""\
        Subject: Today's Workout Plan {date.today()}

        Hi {self.name},

        According to the information you provided:
        
        {self.user_info(args.name,args.height,args.weight,args.age,args.gender,
        args.email)}
        
        Your Body Mass Index (BMI) is: {self.bmi_calculator(args.height, args.weight)} %.
        {self.calories_calculator(args.height, args.weight, args.age, args.gender)}
        
        Your Workout of the Day (WOD) has been prepared by {self.trainer}.
        
        {self.workoutplan(args.filename)}
        
        This message is sent from Python."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print(message)
        time.sleep(5)
        self.alert_popup(f"Today's Workout Plan", f'Your Body Mass Index (BMI) is: '
                         f'{self.bmi_calculator(args.height,args.weight)} %',
                         f'{self.calories_calculator(args.height, args.weight, args.age, args.gender)}')


def parse_args(arglist):
    """ parse command-line arguments.
    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments
    """

    parser = ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("height", type=int,
                        help="height of the user in inches")
    parser.add_argument("weight", type=int,
                        help="weight of the user in pounds")
    parser.add_argument("age", type=int, help="age of the user")
    parser.add_argument("gender", help="gender of the user in 'M'/'F'")
    parser.add_argument("email", help="email of the user")
    parser.add_argument("filename", help="csv file")
    return parser.parse_args(arglist)


def main(name, height, weight, age, gender, email):
    """ provide a space to store our arguments and execute desired plans.

    Args:
       name(str): name of the user
       height(int): height of the user in inches
       weight (int): weight of user in pounds
       age (int): age of the user
       gender(str): male or female in 'M'/'F'
       email(str): email address of user

    """
    g = GetWorkout(name, height, weight, age, gender, email)
    a = g.user_info(name, height, weight, age, gender, email)
    r = g.calories_calculator(height, weight, age, gender)
    b = g.bmi_calculator(height, weight)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name, args.height, args.weight,
         args.age, args.gender, args.email)

    # Sample running code
    # python FitnessTracker.py Jong 70 175 20 M aengida@gmail.com workoutplan.csv
    # python3 FitnessTracker.py Jong 70 175 20 M aengida@gmail.com workoutplan.csv
    # password = !QW@1qw2!QW@1qw2
