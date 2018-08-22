__author__ = 'stefan'

import math

one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight = "eight"
nine = "nine"
ten = "ten"
eleven = "eleven"
twelve = "twelve"
thirteen = "thirteen"
fourteen = "fourteen"
fifteen = "fifteen"
sixteen = "sixteen"
seventeen = "seventeen"
eighteen = "eighteen"
nineteen = "nineteen"
twenty = "twenty"
thirty = "thirty"
forty = "forty"
fifty = "fifty"
sixty = "sixty"
seventy = "seventy"
eighty = "eighty"
ninety = "ninety"
hundred = "hundred"
andand = "and"

def split_number(n):
    if n <=20:
        return [n]
    if n>20 and n<100:
        return [int(math.floor(n/10)), int(n-math.floor(n/10)*10)]
    if n>=100 and n<=999:
        return [int(math.floor(n/100)), int(math.floor((n-(math.floor(n/100)*100))/10)), int(n-math.floor(n/100)*100-math.floor((n-(math.floor(n/100)*100))/10)*10)]
    if n>999:
        return [1,1,1,1]

def last(arg):
    if arg==1:
        return one
    if arg==2:
        return two
    if arg==3:
        return three
    if arg==4:
        return four
    if arg==5:
        return five
    if arg==6:
        return six
    if arg==7:
        return seven
    if arg==8:
        return eight
    if arg==9:
        return nine
    if arg==10:
        return ten
    if arg==11:
        return eleven
    if arg==12:
        return twelve
    if arg==13:
        return thirteen
    if arg==14:
        return fourteen
    if arg==15:
        return fifteen
    if arg==16:
        return sixteen
    if arg==17:
        return seventeen
    if arg==18:
        return eighteen
    if arg==19:
        return nineteen
    if arg==20:
        return twenty
    if arg==0:
        return ""
def middle(arg):
    if arg==2:
        return twenty
    if arg==3:
        return thirty
    if arg==4:
        return forty
    if arg==5:
        return fifty
    if arg==6:
        return sixty
    if arg==7:
        return seventy
    if arg==8:
        return eighty
    if arg==9:
        return ninety

def first(arg):
    if arg==1:
        return one + " " + hundred
    if arg==2:
        return two + " " + hundred
    if arg==3:
        return three + " " + hundred
    if arg==4:
        return four + " " + hundred
    if arg==5:
        return five + " " + hundred
    if arg==6:
        return six + " " + hundred
    if arg==7:
        return seven+ " " + hundred
    if arg==8:
        return eight + " " + hundred
    if arg==9:
        return nine + " " + hundred

def last_two(arg):

    if len(arg)==1 and arg[0]==0:
        return ""
    if len(arg)==1:
        return last(arg[0])
    if (len(arg)==2 and arg[0]==1) or (len(arg)==2 and arg[0]==2 and arg[1]==0):
        return last(int("".join(map(str, arg))))
    if (len(arg)==2 and arg[0]==2 and arg[1]>0) or(len(arg)==2 and arg[0]>2):
        return middle(arg[0]) + " " + last(arg[1])
    if (len(arg)==2 and arg[0]==0 and arg[1]==0):
        return ""
    if (len(arg)==2 and arg[0]==0 and arg[1]!=0):
        return last_two(arg[1:])
def combine(arg):
    arg = split_number(arg)
    if len(arg)>3:
        return "za duza liczba!"
    if len(arg)==3 and (arg[1]!=0 or arg[2]!=0):
        return first(arg[0]) + " and " + last_two(arg[1:])
    if len(arg)==3 and arg[1]==0 and arg[2]==0:
        return first(arg[0])
    else:
        return last_two(arg)

def count_length(arg):
    return len(arg.replace(" ",""))

sum =0
for i in range(1000):
    if i == 0:
        continue
    sum+=count_length(combine(i))

print sum