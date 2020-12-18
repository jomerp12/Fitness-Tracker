import smtplib, ssl
from argparse import ArgumentParser
import requests, re, pandas as pd, time, webbrowser, sys
 
class GetWorkout:
   """ Program to generate a daily 7- day workout plan"""
   def __init__(self,name,height,weight,age,gender,email): 
       """Initializes a GetWorkout attribute
	Attributes:
		name: name attribute is initialized for the user information.
		user_information: An empty dictionary attribute for storing user information.
       Side Effects:
           Reads contents of the specified data file
           Populate workout plans. 
       """
       self.name = name
       self.user_information = dict()
   def user_info (self,name,height,weight,age,gender,email): 
       """ Prompts users for name, height (inches), weight (pounds), age, gender (M/F) , and email. This method collects user information(name,height,weight,age,gender,email) as values and keys will be named corresponding to the values. Type of values in the dictionary will vary depending on the arguments. Some can have strings, integers or others.
       Args:
	    name(str): name of the user
           height(int): height of the user in inches
           weight (int): weight of user in pounds
           age (int): age of the user
           gender(str): male/female
           email(str): email address of user
       Side Effects:
           Stores this information into a list.
       Raise Error:
           If user does not enter an appropriate int/str
       """
       counter = 0
       while counter <3: #I ran this counter just to make sure that duplicate names were not being stored in the same dictionary. Although there are people with the same name we will have to work around this somehow. This way, we can store the workout plan and bmi results under that user's key.
           self.name = name
           if name != self.user_information:
               self.user_information.update({name:{'height':height,'weight':weight,'age':age,'gender':gender,'email':email}})
               return (self.user_information)
           else:
               print('you already have an account on us')
           counter+=1
           
   def bmi_calc (self,name,height, weight): 
       """ Calculates BMI index using formula: BMI= 703*weight(lbs)/[height(in)]^2
       Args:
           height(int): height of the user in inches
           weight (int): weight of user in pounds
       Side Effects:
           Analyze BMI index into a health category: underweight, healthy, or overweight 
       Returns:
           BMI index and BMI health category 
       """
       BMI = (703 * weight) / (height ** 2)
       if BMI < 18.5:
           print (f'Your BMI is: {BMI}. You are underweight')
       elif BMI > 18.5 and BMI < 24.9:
           print(f'Your BMI is: {BMI}. Congrats! You are healthy')
       elif BMI > 25:
           print (f'Your BMI is: {BMI}. You are overweight')
       self.user_information.update({name: {'BMI': BMI}}) #This is meant to add onto the user's history dictionary created above on the user_info function
       
   def Calories_Calculator (self,height, weight, age, gender):
       """ Calculates calories using BMR formula:
       Args:
           height(int): height of the user in inches
           weight (int): weight of user in pounds
           age (int): age of the user
           gender(str): male/female
       Side Effects:
           Male BMR formula: 66 + (6.3 x body weight in lbs.) + (12.9 x height in inches) - (6.8 x age in years)
           Female BMR formula: 655 + (4.3 x weight in lbs.) + (4.7 x height in inches) - (4.7 x age in years)
       Returns:
           Estimated number of calories needed to maintain current weight
       """
       if gender == 'M':
           BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
       else:
           BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
 
       self.user_information.update({'BMR': BMR})
      
   def workoutplan(self, filename):
        """Get a workout plan from a file and store a tailored workout plan.
        Args:
            filename(str): contains a list of workout plans
        Returns:
            returns workout plan based on the user's preference.
        """
        workoutplan_list = []
        with open(filename) as work_out:
            workout_file = csv.reader(work_out, delimiter = ',')
            for row in workout_file:
                Day = row[:]
                workoutplan_list.append(day)
            if exercise not in user_hist_list:
                workoutplan_list.append(exercise)
        return workoutplan_list
    
   def video_tutorial(self,workout):
       """ Link to youtube tutorial according to workout plan day. 
       Args:
           workout(str): a string that will contain workout plans for the user.
       Side effects:
           Link youtube link video
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
            
   def user_history(self): #Jomer Paulino
       """ Keeps a running log of workouts already assigned to ensure no repeats.
       
       Returns:
           A list containing exercises performed by the user.
       """
       user_hist_list = list()
       workout = workoutplan()
       user_hist_list.append(workout)
       return user_hist_list
   
   def notification(self): #Jomer Paulino
        """ Sends an email to the user containing recommended workout plan for the day and user history information.
        
            Returns: 
                message (str) = containing the message sent to the user.
        """
        port = 465 
        smtp_server = "smtp.gmail.com"
        sender_email = "fitnesstrackerINST326@gmail.com" #This email has been hacked. New email will be provided on the final project.
        receiver_email = f'{self.user_information[self.email]}'  
        password = input("Enter your password: ") 
        message = f"""\
        Subject: Hi {self.name}
 
 
       Attached you can find your workout plan along with a copy of your user history information.
      
       This message is sent from Python."""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
           server.login(sender_email, password)
           server.sendmail(sender_email, receiver_email, message)
           return message
      
def parse_args(arglist): # only user_info arguments are constructed. Other arguments will later be constructed with more codes in main.
   """ parse command-line arguments.
Args:
        arglist (list of str): list of command-line arguments.
 
    	Returns:
        namespace: the parsed arguments
"""
   parser = ArgumentParser()
   parser.add_argument("name")
   parser.add_argument("height", help="height of the user")
   parser.add_argument("weight", help="weight of the user")
   parser.add_argument("age", help="age of the user")
   parser.add_argument("gender", help="gender of the user")
   parser.add_argument("email", help="email of the user")
   return parser.parse_args(arglist)
  
def main(name,height,weight,age,gender,email): # This main function currently takes the class and launches the user_info method using the user arguments and print out. In the future, there will be more applications using different methods.
   """ provide a space to store our arguments and execute desired plans.
   Args:
       name(str): name of the user
       height(int): height of the user in inches
       weight (int): weight of user in pounds
       age (int): age of the user
       gender(str): male/female
       email(str): email address of user
   """
   g = GetWorkout(name,height,weight,age,gender,email)
   a = g.user_info(name,height,weight,age,gender,email)
   print(a)
   
if __name__ == "__main__": # partially completed (only user_info method is currently running in main function)
   args = parse_args(sys.argv[1:])
   main(args.name,args.height,args.weight,args.age,args.gender,args.email)
© 2020 GitHub, Inc.