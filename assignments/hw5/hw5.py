"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = input("enter a name (first last)")
    print(name[name.find(' ')+1:] + ',', name[0:name.find(' ')+1])


def company_name():
    site = input("enter a domain:")
    print(site[site.find('.')+1 :site.rfind('.')])


def initials():
    numstudents = eval(input("How many students are in the class?"))
    for student in range(1, numstudents + 1):
        print("What is the name of student", str(student) + "?")
        name = input()
        print(name[0]+ name[name.find(' ')+1])



def names():
    names = input("Enter a list of names")


def thirds():
    numsentence = eval(input("enter number of sentences"))
    sentenceaccumulator = ""
    for sentence in range(1, numsentence + 1):
        print("enter sentence", str(sentence) + ":")




def word_average():
    sentence = input("Enter a sentence")
    splitsent = sentence.split()
    averageaccum = 0
    for word in splitsent:
        averageaccum = len(word) + averageaccum
    print(averageaccum/len(splitsent))



def pig_latin():
    pass


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
