class GetWorkout:
    """Provides personalized workout schedules a plan.
    
    Attributes:
        user: 
    """
    
    def __init__(self, user):
        """Initializes a GetWorkout attribute 
        Args:
            user:
        Side Effects:
            Reads contents of the specified data file 
            Populate workout plans.  
        """
        self.user = user
        self.trainer = random.choice(['Jomer', 'Seungjoon', 'Lucy', 'Jonghyeong'])
    
    def user_info ():
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
    
    def bmi_calc ():
    """ Calculates BMI index using formula: BMI= 703*weight(lbs)/[height(in)]^2
    Args:
        height(int): height of the user in inches
        weight (int): weight of user in pounds
    Side Effects:
        Analyze BMI index into category 
    Returns:
        BMI index and whether the value is considered underweight, normal weight, overweight, or obese. 
    """
    
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
       
def parse_args(arglist):
    """ parse command-line arguments."""
        
def main(filename,workout):
    """ provide a space to store our arguments and execute desired plan.
    Args:
        filename(str): contains the path to a .txt file containing a list of pre-made workout plans
        workout(str): a string that will contain workout plans for the user. 
    """