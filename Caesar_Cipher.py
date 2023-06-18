#  Run In Python....

# Making Encrypting Function...
class stri:
    def __init__(self,n=4):
        num =n
    def encrypting(self,message='',num=4):
        j =0
        for i in message:
            if (ord(i) >= 65 and ord(i)<= 90) or (ord(i)>=97 and ord(i)<=122) : # Taking only letters..
                if (ord(i) > (90-num) and ord(i)<= 90) or (ord(i)>(122-num) and ord(i)<=122): # Taking latter from z upto n
                    Encrypting_code = ord(i) - (26-num)  # Updating ascii code 
                    Encrypting_message = chr(Encrypting_code) # Updating letter
                else:
                    Encrypting_code = ord(i) +num
                    Encrypting_message = chr(Encrypting_code)
            else :
                Encrypting_code = ord(i)
                Encrypting_message = chr(Encrypting_code)
            # print(i, type(i))
            # print(Encrypting_code, type(Encrypting_code))
            # print(Encrypting_message, type(Encrypting_message))
            message = message[:j] + Encrypting_message + message[j+1:] # Updating String...
            j +=1
        return message
    def encrypted(self,message='',num=4):
        j =0
        for i in message:
            if (ord(i) >= 65 and ord(i)<= 90) or (ord(i)>=97 and ord(i)<=122) :
                if (ord(i) >= 65 and ord(i)< (65+num)) or (ord(i)>=97 and ord(i)<(97+num)):
                    Encrypting_code = ord(i) +(26-num)
                    Encrypting_message = chr(Encrypting_code)
                else:
                    Encrypting_code = ord(i) -num
                    Encrypting_message = chr(Encrypting_code)
            else :
                Encrypting_code = ord(i)
                Encrypting_message = chr(Encrypting_code)
            # print(i, type(i))
            # print(Encrypting_code, type(Encrypting_code))
            # print(Encrypting_message, type(Encrypting_message))
            message = message[:j] + Encrypting_message + message[j+1:]
            j +=1
        return message

a = stri()
message = input('Enter the Message for Encrypting: ')
b = a.encrypting(message,25)
print('Encrypted massege = ',b)
d = a.encrypted(b,25)
print('Original massege = ',d)
