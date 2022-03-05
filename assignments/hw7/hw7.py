"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    linenumber = 0
    for line in infile:
        splitlines = line.split(' ')
        for word in splitlines:
            linenumber = linenumber+1
            outfile.write(str(linenumber)+" " + word+"\n")
    infile.close()
    outfile.close()



def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w')
    for line in infile:
        listworker = line.split(' ')
        weeklypayment = (float(listworker[2])+1.65) * float(listworker[3])
        weeklypayment = '${:.2f}'.format(weeklypayment)
        outfile.write(str(listworker[0])+' '+str(listworker[1]) + " " + weeklypayment + '\n')
    infile.close()
    outfile.close()

def calc_check_sum(isbn):
    pass
    "ask about these in class "

def send_message(file_name, friend_name):
    pass

def encode():
    message = input("Enter a message to be encoded")
    key = eval(input("Enter a key to encode the message with"))
    codedmessage = ''
    for letter in message:
        c = ord(letter) + key
        codedmessage = codedmessage + chr(c)
    print(codedmessage)


def send_safe_message(file_name, friend_name, key):
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
