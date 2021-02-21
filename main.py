#Program for password generator
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
import random
if __name__ == '__main__':
    s1=string.ascii_lowercase
    S1="".join(random.sample(s1,1))
   # print(S1)
    #getting the uppercase,lowercase,digits and special characters for the password
    s2=string.ascii_uppercase
    S2 = "".join(random.sample(s2, 1))
    s3=string.digits
    S3 = "".join(random.sample(s3, 1))
    s4=string.punctuation
    S4 = "".join(random.sample(s4, 1))
    plen= input("Enter the password length min of 5 character \n")
    #print(plen)
    #the length should be alteast 5 chARAter
    if(plen.isdigit()):
        plen1=int(plen);
        if(plen1>6):
            s = []
            s.extend(s1)
            s.extend(s2)
            s.extend(s3)
            s.extend(s4)
            random.shuffle(s)
            result = []
            result.extend(S1)
            result.extend(S2)
            result.extend(S3)
            result.extend(S4)

           # print(result)
            #print(s)
            value = []
            value = random.sample(s, plen1 - 4)
            #print(value)
            result.extend(value)
           # print(result)
            print("your password is")
            print("".join(random.sample(result, plen1)))
        else:
            print("the password length should be atleast 5 characters")
    else:
        print("Invalid input! Enter a number")


