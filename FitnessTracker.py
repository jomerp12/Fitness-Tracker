import smtplib, ssl
<<<<<<< HEAD
<<<<<<< HEAD
import csv

=======
from argparse import ArgumentParser
import sys
>>>>>>> 9264444770a6afed3271d029ca6ed241a7cb666e
=======
from argparse import ArgumentParser
import sys
>>>>>>> 9264444770a6afed3271d029ca6ed241a7cb666e
class GetWorkout:
    """Provides personalized workout schedules a plan.
    
    Attributes:
        user: 
    """
    
    def __init__(self,name,height,weight,age,gender,email):
        """Initializes a GetWorkout attribute 
        Side Effects:
            Reads contents of the specified data file 
            Populate workout plans.  
        """
        self.name = name
        self.user_information = dict()
        
    def user_info (self,name,height,weight,age,gender,email):
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
        counter = 0
        while counter <3: #I ran this counter just to make sure that duplicate names were not being stored in the same dictionary. Although there are people with the same name we will have
                          # to work around this somehow. This way, we can store the workout plan and bmi results under that user's key.
            self.name = name
            if name != self.user_information:
                self.user_information.update({name:{'height':height,'weight':weight,'age':age,'gender':gender,'email':email}})
                return (self.user_information)
            else:
                print('you already have an account on us')
            counter+=1

    
    def bmi_calc (self,height, weight):
        """ Calculates BMI index using formula: BMI= 703*weight(lbs)/[height(in)]^2
        Args:
            height(int): height of the user in inches
            weight (int): weight of user in pounds
        Side Effects:
            Analyze BMI index into category 
        Returns:
            BMI index and whether the value is considered underweight, normal weight, overweight, or obese. 
        """
        BMI = (703 * weight) / (height ** 2)
        if BMI < 18.5:
            print (f'Your BMI is: {BMI}. You are underweight')
        elif BMI > 18.5 and BMI < 24.9:
            print(f'Your BMI is: {BMI}. Congrats! You are healthy')
        elif BMI > 25:
            print (f'Your BMI is: {BMI}. You are overweight')
        userInfo.update({name: {'BMI': BMI}}) #This is meant to add onto the user's history dictionary created above on the user_info function

    
    def calorie_calc ():
<<<<<<< HEAD
<<<<<<< HEAD
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
        bmr_men = 66+ (6.3 * weight) + (12.9 * height) - (6.8 * age)
        bmr_women = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
        
        if age = M:
            return bmr_men
            userInfo.update({name: {'BMR': bmr_men}})

        elif age = W:
            return bmr_women
            userInfo.update({name: {'BMR': bmr_woemn}})
        
=======
=======
>>>>>>> 9264444770a6afed3271d029ca6ed241a7cb666e
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
    
<<<<<<< HEAD
>>>>>>> 9264444770a6afed3271d029ca6ed241a7cb666e
=======
>>>>>>> 9264444770a6afed3271d029ca6ed241a7cb666e
    def workoutplan(self, filename):
        """Get a workout plan from a file and check the user history for any past
            workout to ensure no repeats.
        
        Args:
            filename(str): contains a list of workout plans 
        
        Returns:
            returns workout plan based on the user's preference.
        """
        
        with open('workoutplan.csv') as fn:
            wp = csv.reader(fn, delimiter=',')
            history = []
            plan = []
            for row in wp:
                day = row[0]
                plan.append(day)
                history.append(day)
                
        
    def video_tutorial(self,workout):
        """ provides video_tutorial based on the specific exercise of workout given by the methods.
        Args:
            workout(str): a string that will contain workout plans for the user.
        Side effects: 
            Link youtube link video 
        Returns:
            exercise(dictionary): Default value will be an empty dictionary and will add workout as a key and url(web address) as a value.
        """
    def user_history(self,workout,history):
        """ Keeps a running log of workouts already assigned to ensure no repeats. 
        Args:
            workout(str): a string that will contain workout plans for the user.
            history(str): a string that will retreive the history of workouts.
        Returns:
            Results workouts that have been done and remaining workouts the user will do.
        """
        for x in plan:
            if plan.count(x) > 1:
                return True
        return False

        result = user_history(plan)
        if result:
            print('You have already done with this workout plan')
        else:
            print('You are good to do the next day workout plan')

    def notification(self):
        """ Sends an email to the user containing recommended workout plan and user history information.
       
            Side Effects:
                Sends notification to the user's eamil.
            Returns:
                A confirmation receipt.
        """
        port = 465  
        smtp_server = "smtp.gmail.com"
        sender_email = "fitnesstrackerINST326@gmail.com"  
        receiver_email = f'{user_email}'  
        password = '12345!@#$%'
        message = """\
        Subject: Hi there


        This message is sent from Python."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            
        print ('Message has been successfully sent!')
        
def parse_args(arglist):
    """ parse command-line arguments."""
    parser = ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("height", help="height of the user")
    parser.add_argument("weight", help="weight of the user")
    parser.add_argument("age", help="age of the user")
    parser.add_argument("gender", help="gender of the user")
    parser.add_argument("email", help="email of the user")
    return parser.parse_args(arglist)
    
def main(name,height,weight,age,gender,email):
    """ provide a space to store our arguments and execute desired plan.
    Args:
        filename(str): contains the path to a .txt file containing a list of pre-made workout plans
        workout(str): a string that will contain workout plans for the user. 
    """
    g = GetWorkout(name,height,weight,age,gender,email)
    a = g.user_info(name,height,weight,age,gender,email)
    print(a)
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name,args.height,args.weight,args.age,args.gender,args.email)