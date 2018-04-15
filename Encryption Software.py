#ENCRYPT MESSAGE
def encrypt(message, offsetFactor):
    #Arguments are the plain text and the offset factor
    plain=message.readline()
    print("Original text:",plain)
    #Reads the line from the file and prints it
    cipher=[]
    #Initialises cipher text array
    for c in range(0,len(plain)):
        if plain[c]!=" ":
            char=ord(plain[c])+offsetFactor
            #For the length of the text, if char isn't space, encrypt letter
            if char>126:
                char-=94
                #If it is above the ASCII range, minus 94
            cipher.append(char)
            #Adds the char to the cipher text array
        else:
            cipher.append(ord(plain[c]))
            #Adds the space to the cipher array
    cipherText=chr(cipher[0])
    #Adds the 1st letter of the cipher text to the string
    for c in range(1,len(cipher)):
        cipherText=cipherText+chr(cipher[c])
    #Adds the rest of the chars of the cipher text to the string
    return cipherText
    #Returns the cipher text string to the function
def offset(chars):
    s1=sum(chars)
    #Adds all chars' ASCII numbers together
    s2=s1/8
    #Divides result by 8
    s3=round(s2)
    #Rounds result
    offsetFactor=s3-32
    print("Offset Factor:", offsetFactor)
    return offsetFactor
    #Sets the offset factor as the result -32 before printing and returning it
def EncryptMessage():
    fileValid=False
    while fileValid==False:
        fileName=input("Please enter the name of your file\n") #sample.txt
        if os.path.isfile(fileName):
            fileValid=True
            file=open(fileName, "r")
            #Opens the file to be encrypted if it exists
        else:
            print("This file does not exist")
    c=0
    chars=[0,1,2,3,4,5,6,7]
    nChars=[0,1,2,3,4,5,6,7]
    #Initialises the above arrays
    for c in chars:
        nChars[c]=random.randint(33,126)
        #Generates a random number within the ASCII range
        chars[c]=chr(nChars[c])
        #Converts the random number to a character before storing in the array
        c+=1
    key="'"
    for c in range(0,8):
        key+=chars[c]
    key+="'"
    print("\nKeep this key safe for decryption:", key)
    #Sets the key to the array and prints it as a string
    offsetFactor=offset(nChars)
    #Carries out the offset factor calculation
    cipherText=encrypt(file, offsetFactor)
    #Begins encryption process
    print("Encryption Complete:", cipherText,"\n")
    outputFileName=input("Please enter the name of the output file\n")
    outputFile=open(outputFileName, "w")
    outputFile.write(cipherText)
    print("File written")
    #Announces completion before writing to a file the user inputs

#DECRYPT MESSAGE
def decrypt(message, offsetFactor):
    #Arguments are the cipher text and the offset factor
    cipher=message.readline()
    print("Encrypted text:",cipher)
    #Reads the line from the file and prints it
    plain=[]
    #Initialises plain text array
    for c in range(0,len(cipher)):
        if cipher[c]!=" ":
            char=ord(cipher[c])-offsetFactor
            #For the length of the text, if char isn't space, decrypt letter
            if char<32:
                char+=94
                #If it is below the ASCII range, plus 94
            plain.append(char)
            #Adds the char to the plain text array
        else:
            plain.append(ord(cipher[c]))
            #Adds the space to the plain text array
    plainText=chr(plain[0])
    #Adds the 1st letter of the plain text to the string
    for c in range(1,len(plain)):
        plainText=plainText+chr(plain[c])
    #Adds the rest of the chars of the plain text to the string
    return plainText
    #Returns the plain text string to the function
def DecryptMessage():
    fileValid=False
    keyValid=False
    while fileValid==False:
        fileName=input("Please enter the name of your file\n") #output.txt
        if os.path.isfile(fileName):
            fileValid=True
            file=open(fileName, "r")
            #Opens the file to be decrypted if it exists
        else:
            print("This file does not exist")
    while keyValid==False:
        sKey=input("Please input your 8 character key")
        if len(sKey)==8:
            keyValid=True
        else:
            print("Invalid key detected")
    #Asks user to input key as string
    c=0
    key=[0,1,2,3,4,5,6,7]
    nKey=[0,1,2,3,4,5,6,7]
    #Initialises above arrays
    for c in key:
        nKey[c]=ord(sKey[c])
        #Converts string into ASCII number and stores in array
        key[c]=chr(nKey[c])
        #Converts ASCII number to character and stores in array
        c+=1
    offsetFactor=offset(nKey)
    #Carries out offset factor calculation
    plainText=decrypt(file, offsetFactor)
    #Begins decryption process
    print("\nDecryption Complete:", plainText,"\n")
    #Prints decrypted file

#ADVANCED ENCRYPTION
def aEncrypt(message, offsetFactor):
    #Arguments are the plain text and the offset factor
    plain=message.readline()
    print("Original text:",plain)
    #Reads the line from the file and prints it
    plain2=[]
    cipher=[]
    #Initialises the above arrays
    c=0
    for c in range(0,len(plain)):
        if plain[c]!=" ":
            plain2.append(plain[c])
    #Adds all characters from text file to array except spaces.
    for c in range(0, len(plain2)):
        if c%6==0:
            plain2.insert(c," ")
            #If c is a multiple of 5, inserts a space in the array at that position
    for c in range(0,len(plain2)):
        if plain2[c]!=" ":
            char=ord(plain2[c])+offsetFactor
            #Encrypt the letter for the length of the text file
            if char>126:
                char-=94
                #If it is above the ASCII range, minus 94
            cipher.append(char)
            #Adds the char to the cipher text array
        else:
            cipher.append(ord(" "))
    print(cipher)
    cipherText=""
    #Initialises the cipherText variable
    for c in range(0,len(cipher)):
        cipherText=cipherText+chr(cipher[c])
        #Adds all of the chars of the cipher text to the string
    return cipherText
    #Returns the cipher text string to the function
def AdvancedEncryption():
    fileValid=False
    while fileValid==False:
        fileName=input("Please enter the name of your file\n") #sample.txt
        if os.path.isfile(fileName):
            fileValid=True
            file=open(fileName, "r")
            #Opens the file to be encrypted if it exists
        else:
            print("This file does not exist")
    c=0
    chars=[0,1,2,3,4,5,6,7]
    nChars=[0,1,2,3,4,5,6,7]
    #Initialises the above arrays
    for c in chars:
        nChars[c]=random.randint(33,126)
        #Generates a random number within the ASCII range
        chars[c]=chr(nChars[c])
        #Converts the random number to a character before storing in the array
        c+=1
    key="'"
    for c in range(0,8):
        key+=chars[c]
    key+="'"
    print("\nKeep this key safe for decryption:", key)
    #Sets the key to the array and prints it as a string
    offsetFactor=offset(nChars)
    #Carries out the offset factor calculation
    cipherText=aEncrypt(file, offsetFactor)
    #Begins encryption process
    print("Encryption Complete:", cipherText,"\n")
    outputFileName=input("Please enter the name of the output file\n")
    outputFile=open(outputFileName, "w")
    outputFile.write(cipherText)
    print("File written")
    #Announces completion before writing to a file the user inputs

#MAIN MENU
import time
import random
import os
#Imports the random and time modules for later use.
offsetFactor=0
cipherText=""
#Initialises the above variables
def menu():
    choice=0
    while choice != 4:
        print("Abhid's Encryption Software\n")
        print("Option 1: Encrypt Message\n")
        print("Option 2: Decrypt Message\n")
        print("Option 3: Advanced Encryption\n")
        print("Option 4: Exit\n")
        #Displays the valid menu options
        choice = int(input("Please type in 1, 2, 3 or 4 to choose an option.\n"))
        #Gets the user to choose an option
        if choice == 1:
            EncryptMessage()
        elif choice == 2:
            DecryptMessage()
        elif choice == 3:
            AdvancedEncryption()
        #Redirects the user to the correct function
    print("Thank you for using this program. Goodbye.")
    time.sleep(1)
    exit()
    #Closes the program if the user chooses option 4
menu()
