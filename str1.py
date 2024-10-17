message = 'The guys working at low level are paid highest in Embedded Domain'

print(len(message))     #prints length of the message
print(message)          #prints the message

#------------------------------------------------------------
#String Slicing
print(message[:12])     #prints the message uptill 11th character
print(message[12:])     #prints the message from 12th character until the string ends.
print(message[:])       #prints the whole string 
print(message[4: 47])   #prints the string from 4th character upto 46th character
print(message[43])      #prints the chracter at 43rd position

#-------------------------------------------------------------
#other functionalities
print(message.lower())
print(message.upper())
print(message.count('low'))
print(message.count('e'))
print(message.find('h'))
print(message.find('highest'))
print(message.find('best'))

#-------------------------------------------------------------
#Replace and Concatenate
message = message.replace('Domain', 'Systems Domain')
print(message)

new_msg = 'and are very hard working.'
message = message + ' ' + new_msg
print(message)

intro = "Fact:"
#Instead of doing this 
#message = intro + ' ' + message + ' ' + new_msg
#We can do:

message = '{} {} Welcome!'. format(intro, message)
print(message)

#we can also use fstring
message = f'The one true {message} Just appending:-)'
print(message)

message = f'{message.lower()}'
print(message)

message = f'{message.upper()}'
print(message)

#-------------------------------------------------------------
#Show Attributes and methods for a given variable

print(dir(message))

print(dir(new_msg))

print(help(str))

#--------------------------------------------------------------