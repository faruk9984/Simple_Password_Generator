# Password Generator using Python

import string
import random


if __name__ == '__main__':
    s1=string.ascii_letters
    print("letters:",s1)
    s2=string.ascii_lowercase
    print("lower:",s2)
    s3=string.ascii_uppercase
    print("upper:",s3)
    s4=string.digits
    print("digit:",s4)
    s5=string.punctuation
    print("pun:",s5)

    plen=int(input('enter password length:'))
    s=[]
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))

    #print(s)
    #random.shuffle(s)
    #print(s)
    #print('your password is:',"".join(s[0:plen]))
    print('your password is:',"".join(random.sample(s,plen)))





