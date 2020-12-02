import smtplib, ssl
import requests, re, pandas as pd, time, webbrowser, sys

class GetWorkout:
    """Provides personalized workout schedules a plan.
    
    Attributes:
        user: 
    """
    
    def __init__(self,name):
        """Initializes a GetWorkout attribute 
        Side Effects:
            Reads contents of the specified data file 
            Populate workout plans.  
        """
        self.name = name
        self.trainer = random.choice(['Jomer', 'Seungjoon', 'Lucy', 'Jonghyeong'])
        self.stored_data = dict()
    
    def User_Info (self):
        """ Prompts user for height (inches), weight (pounds), age, gender, and email.
        Args: 
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
        height = input('Enter your height in inches: ')
        weight = input('Enter your weight in pounds: ')
        age = input('Enter your age: ')
        gender = input('Enter your gender [M/F]: ')
        email = input('Enter your e-mail address: ')
        self.stored_data.update({'name': self.name, 'height': height, 'weight' : weight, 'age': age, 'gender': gender, 'email' : email})
        
    def BMI_Calculator (self,height, weight):
        """ Calculates BMI index using formula: BMI= 703*weight(lbs)/[height(in)]^2
        Args:
            height(int): height of the user in inches
            weight (int): weight of user in pounds
        Side Effects:
            Analyze BMI index into category 
        Returns:
            BMI index and whether the value is considered underweight, normal weight, overweight, or obese. 
        """
        BMI = (703 * 175) / (68 ** 2)
        if BMI < 18.5:
            print (f'Your BMI is: {BMI}. You are underweight')
        elif BMI > 18.5 and BMI < 24.9:
            print(f'Your BMI is: {BMI}. Congrats! You are healthy')
        elif BMI > 25:
            print (f'Your BMI is: {BMI}. You are overweight')
        self.stored_data.update({'BMI': BMI})

    
    def Calories_Calculator (height, weight, age, gender):
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
            
        self.stored_data.append({'BMR': BMR})
    
    def User_History(self,workout,history):
        """ Keeps a running log of workouts already assigned to ensure no repeats. 
        Args:
            workout(str): a string that will contain workout plans for the user.
            history(str): a string that will retreive the history of workouts.
        Returns:
            Results workouts that have been done and remaining workouts the user will do.
        """
        user_hist_dict = dict()
        workout = Workout_Plan
        user_hist_dict.append(workout) #This dictionary is storing workouts assigned to the user. 
        
    def Workout_Plan(self, filename):
        """Sorts keys of the GetWorkout attribute according to user's 
        preference and creates a tailored workout plan.
        
        Args:
            filename(str): contains a list of workout plans 
        
        Returns:
            returns workout plan based on the user's preference.
        """
        workoutplan = dict()
        with open(filename, 'r') as work_out:
		    work_out = work_out.read()
		    self.stored_data[] = 

            if exercise not in user_hist_dict:
                workoutplan.append(exercise)
        
    def Video_Tutorial(self,workout):
        """ provides video_tutorial based on the specific exercise of workout given by the methods.
        Args:
            workout(str): a string that will contain workout plans for the user.
        Side effects: 
            Link youtube link video 
        Returns:
            exercise(dictionary): Default value will be an empty dictionary and will add workout as a key and url(web address) as a value.
        """
        exercises_dict = dict()
        exercises_dict['Shoulder Press'] = 'https://www.youtube.com/watch?v=Fek7QcFOgl8'
        webbrowser.open_new(exercises_dict['Shoulder Press'])
        
    def Notification(self):
        """ Sends an email to the user containing recommended workout plan and user history information.
       
            Side Effects:
                Sends notification to the user's eamil.
            Returns:
                A confirmation receipt.
        """
        port = 465  
        smtp_server = "smtp.gmail.com"
        sender_email = "fitnesstrackerINST326@gmail.com"  #I created this email just for this purpose
        receiver_email = f'{self.stored_data['email']}'  
        password = '12345!@#$%'
        message = f"""\
        Subject: Hi {self.name}

        Attached you can find your workout plan along with a copy of your user history information.
        
        This message is sent from Python."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            
        print ('Message has been successfully sent!')
        
def parse_args(arglist):
    """ parse command-line arguments."""
    parser= ArgumentParser()
	parser.add_argument(“”, help = “ ”)
    parser.add_argument(“”, help = “ ”)
    Return parser.parse_args(arglist)	
        
def main(filename):
    """ provide a space to store our arguments and execute desired plan.
    Args:
        filename(str): contains the path to a .txt file containing a list of pre-made workout plans
        workout(str): a string that will contain workout plans for the user. 
    """