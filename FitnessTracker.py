class GetWorkout:
    """Provides personalized workout schedules and diet plans.
    
    Attributes:
    
    
    """
    
    def __init__(self, filename):
        """Initializes a GetWorkout attribute and reads contents of the 
        specified data file and populate workout plans.  
        
        Args:
            filename(str): contains the path to a .txt file containing 
            a list of pre-made workout plans

        """
        
    def workoutplan(self, workout):
        """Sorts keys of the GetWorkout attribute according to user's 
        preference and creates a tailored workout plan.
        
        Args:
            workout(str): a string that will contain workout plans for the user.
        """
        
    def dietplan(self, Diet):
        """Sorts keys of the GetWorkout attribute according to user's 
        preference and creates a tailored diet plan.
        
        Args:
            Diet(str): a string that will contain diet plan for the user.
        """
        
    def video_tutorial(self,workout,Diet):
        """ provides video_tutorial based on the specific exercise of workout/diet plan given by the methods.
        Args:
            workout(str): a string that will contain workout plans for the user.
            Diet(str): a string that will contain diet plan for the user.
        Returns:
            exercise(dictionary): Defauilt value will be an empty dictionary and will add workout/diet plan as a key and url(web address) as a value.
        """
        
def parse_args(arglist):
    """ parse command-line arguments."""
        
def main(filename,workout,Diet):
    """ provide a space to store our arguments and execute desired plan.
    Args:
        filename(str): contains the path to a .txt file containing a list of pre-made workout plans
        workout(str): a string that will contain workout plans for the user.
        Diet(str): a string that will contain diet plan for the user. 
    """