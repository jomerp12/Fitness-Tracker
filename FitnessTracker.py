import smtplib, ssl

class GetWorkout:
    """Provides personalized workout schedules a plan.
    
    Attributes:
        user: 
    """
    
    def __init__(self,user):
        """Initializes a GetWorkout attribute 
        Side Effects:
            Reads contents of the specified data file 
            Populate workout plans.  
        """
        self.user = user
        self.trainer = random.choice(['Jomer', 'Seungjoon', 'Lucy', 'Jonghyeong'])
    
    def user_info (self):
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
        userInfo = dict()
        height = input('Enter your height in inches: ')
        weight = input('Enter your weight in pounds: ')
        age = input('Enter your age: ')
        gender = input('Enter your gender [M/F]: ')
        email = input('Enter your e-mail address: ')

    
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
        BMI = (703 * weight) / (height ^ 2)
        if BMI < 18.5:
            return (f'Your BMI is: {BMI}. You are underweight')
        elif BMI > 18.5 and BMI < 24.9:
            return(f'Your BMI is: {BMI}. Congrats! You are healthy')
        elif BMI > 25:
            return (f'Your BMI is: {BMI}. You are overweight')

    
    def calorie_calc ():
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
        
    def workoutplan(self, filename):
        """Sorts keys of the GetWorkout attribute according to user's 
        preference and creates a tailored workout plan.
        
        Args:
            filename(str): contains a list of workout plans 
        
        Returns:
            returns workout plan based on the user's preference.
        """
        
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
        
def main(filename):
    """ provide a space to store our arguments and execute desired plan.
    Args:
        filename(str): contains the path to a .txt file containing a list of pre-made workout plans
        workout(str): a string that will contain workout plans for the user. 
    """