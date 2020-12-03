from argparse import ArgumentParser
import sys
class Testing:
    def __init__(self,height,weight,age,gender,email):
        self.stored_data = dict()
    def user_info(self,height,weight,age,gender,email):
        self.stored_data["Height"] = height
        self.stored_data["weight"] = weight
        self.stored_data["Age"] = age
        self.stored_data["gender"] = gender
        self.stored_data["email"] = email
        return (self.stored_data)
    
def parse_args(arglist):
    """ parse command-line arguments."""
    parser = ArgumentParser()
    parser.add_argument("height", help="height of the user")
    parser.add_argument("weight", help="weight of the user")
    parser.add_argument("age", help="age of the user")
    parser.add_argument("gender", help="gender of the user")
    parser.add_argument("email", help="email of the user")
    return parser.parse_args(arglist)

def main(height,weight,age,gender,email):
    g = Testing(height,weight,age,gender,email)
    a = g.user_info(height,weight,age,gender,email)
    print(a)
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.height,args.weight,args.age,args.gender,args.email)