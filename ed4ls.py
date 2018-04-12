import sys
import os
import itertools
import string
from setting import logo
from argparse import ArgumentParser

class ModModification:
    def __init__(self, file=None, output=None):
        self.file = file
        self.output = output

    def RmDuplicates(self):
        list = open(self.file, "r")
        NewList = []
        
        #Creat new list
        for word in list:
            if word not in NewList:
                NewList.append(word)
            elif word in NewList:
                pass

        #Show or save new list
        if self.output == None:
            for word in NewList:
                print(word)
        elif self.output != None:
            output = open(self.output, "w")
            sys.stdout = output
            for word in NewList:
                print(word)
            output.close

    def AddWord(self, after=False, before=False, AddWord=None):
        file = [line.strip() for line in open(self.file, "r")]
        if after:
            if self.output == None:
                for word in file:
                    NewWord = word+AddWord
                    print(NewWord)
            elif self.output != None:
                output = open(self.output, "w")
                sys.stdout = output
                for word in file:
                    NewWord = word+AddWord
                    print(NewWord)
                output.close
        elif before:
            if self.output == None:
                for word in file:
                    NewWord = AddWord+word
                    print(NewWord)
            elif self.output != None:
                output = open(self.output, "w")
                sys.stdout = output
                for word in file:
                    NewWord = AddWord+word
                    print(NewWord)
                output.close            
        elif after == False and before == False:
            exit("the -a option comes with a -aA=add after or -aB=add before")

    def RemoveBlankLines(self):
        with open(self.file, "r") as file:
            lines = file.read().splitlines()
            NewList = [lin for lin in lines if lin.strip()]
            if self.output == None:
                for line in itertools.product(NewList):
                    try:
                        output = ''.join(line)
                    except AttributeError:
                        output = string.join(line, '')
                    print(output)
            elif self.output != None:
                output = open(self.output, "w")
                sys.stdout = output
                for line in itertools.product(NewList):
                    try:
                        out = ''.join(line)
                    except AttributeError:
                        out = string.join(line, '')
                    print(out)
                    output.close

    def Sorter(self):
       list = open(self.file, "r")
       sort = sorted(list)
       if self.output == None:
           for line in itertools.product(sort):
                try:
                    out = ''.join(line)
                except AttributeError:
                    out = string.join(line, '')
                print(out)
       elif self.output != None:
           output = open(self.output, "w")
           sys.stdout = output
           for line in itertools.product(sort):
                try:
                    out = ''.join(line)
                except AttributeError:
                    out = string.join(line, '')
                print(out)
                output.close

def print_examples(display=False):
    if display:
        example = ("\n#Examples:\n")
        example += ("For delete duplicates from the file\n")
        example += ("python ed4ls.py -rD -w wordlist.txt\n")
        example += ("#------------------------------#\n")
        example += ("For add aword to each word in the wordlist\n")
        example += ("after : python ed4ls.py -a @gmail.com -aA -w wordlist.txt\n")
        example += ("befor : python ed4ls.py -a laser@ -aB -w wordlist.txt\n")
        example += ("#------------------------------#\n")
        example += ("For remove blank lines from file\n")
        example += ("python ed4ls.py -rL -w wordlist.txt\n")
        example += ("#------------------------------#\n")
        example += ("For sort alphabetical characters\n")
        example += ("python ed4ls.py -s -w wordlist.txt\n")
        example += ("#------------------------------#\n")
        example += ("For save the output to a file\n")
        example += ("python ed4ls.py -s -w wordlist.txt -o test.txt\n")
        print(example)
def main():
    #cmd
    parser = ArgumentParser(prog="ed4ls.py", add_help=True, usage=("python ed4ls.py [options]"))
    parser.add_argument("-hh", dest="helpadv", action="store_true",
                    help="Display help and examples message and exit")
    parser.add_argument("-rD", dest="rmduplicates", action="store_true",
                        help="Delete duplicates from the file")
    parser.add_argument("-a", dest="addword",
                        help="Add aword to each word in the wordlist after=-aA or brfore=-aB -a <word>")
    parser.add_argument("-aA", dest="addafter", action="store_true",
                        help="Add a word after each word in the file")
    parser.add_argument("-aB", dest="addbefore", action="store_true",
                        help="Add a word before each word in the file")
    parser.add_argument("-w", dest="wordlist",
                        help="The file you want to modify")
    parser.add_argument("-o", dest="output",
                        help="Save the output to a file")
    parser.add_argument("-rL", dest="removeblanklines", action="store_true",
                        help="remove blank lines from file")
    parser.add_argument("-s", dest="sort", action="store_true",
                        help="Sort alphabetical characters")
    args = parser.parse_args()

    #print logo
    logo()
    
    #display help
    if args.helpadv:
        parser.print_help()
        print_examples(display=True)
        exit(0)
    elif args.helpadv == False:
        pass
    
    #check the existence of the files
    if args.wordlist == None:
        exit("You must add a wordlis -w <file>")
    elif args.wordlist != None:
        if os.path.exists(args.wordlist) == True:
            pass
        elif os.path.exists(args.wordlist) == False:
            exit("\nFile does not exit")

    #choose if mod with output or without output 
    if args.output == None:
        mod = ModModification(file=args.wordlist)
    elif args.output != None:
        mod = ModModification(file=args.wordlist,
                     output=args.output)
    #run function        
    if args.rmduplicates:
        mod.RmDuplicates()
    elif args.removeblanklines:
        mod.RemoveBlankLines()
    elif args.sort:
        mod.Sorter()
    elif args.addword != None:
        if args.addafter:
            mod.AddWord(after=True,
                        AddWord=args.addword)
        elif args.addbefore:
            mod.AddWord(before=True,
                        AddWord=args.addword)
        elif args.addafter == False and args.addbefore == False:
            exit("the -a option comes with a -aA=add after or -aB=add before")
    elif args.helpadv:
        parser.print_help()
        print_examples(display=True)        
    else:
        parser.print_help()
        print_examples(display=True)
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit("\n\nuser aborted")
