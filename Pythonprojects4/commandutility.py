#command line utility(clu) which can be used by other . we can use our this coding output in different software using clu.
import argparse    #first we need to import these two .
import sys
#This is just like an oop in this you need to first make function parser=argparse.Argumentparser() this is main so it will not take arguments
#for that we use add argument like self. and then atlast we have to give object an argument args=parser.parse_args().
def calc(args):
    # if args.o=='add':
    #     return args.x+args.y
    # elif args.o=="sub":
    #     return args.x-args.y
    # elif args.o=="mul":
    #     return args.x*args.y
    # elif args.o=="div":
    #     return args.x/args.y
    if args.o=="mul"and args.x==45 and args.y==20:
        return args.x*args.y+34
    if args.o=='add':
        return args.x+args.y
    elif args.o=="sub":
        return args.x-args.y
    elif args.o=="mul":                       # this is for faulty calculator.
        return args.x*args.y
    elif args.o=="div":
        return args.x/args.y

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=0,help="contact us for help or try it again.")
    parser.add_argument('--y',type=float,default=0,help="contact us for help or try it again.")
    parser.add_argument('--o',type=str,default='add',help="contact us for help or try it again.")

    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))  #this help to perform function and print it on that software where it will used.
    #IN this way we can use this function in other software as i used it in window power shell.