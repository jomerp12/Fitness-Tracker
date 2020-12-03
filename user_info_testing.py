from argparse import ArgumentParser
import sys
class Testing:
    def __init__(self,name,height,weight,age,gender,email):
        self.name = name
        self.stored_data = dict()
    def user_info(self,name,height,weight,age,gender,email):
        counter = 0
        while counter <3:
            self.name = name
            if name != self.stored_data:
                self.stored_data.update({name:{'height':height,'weight':weight,'age':age,'gender':gender,'email':email}})
                return (self.stored_data)
            else:
                print('you already have an account on us')
            counter+=1
    
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
    g = Testing(name,height,weight,age,gender,email)
    a = g.user_info(name,height,weight,age,gender,email)
    print(a)
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name,args.height,args.weight,args.age,args.gender,args.email)