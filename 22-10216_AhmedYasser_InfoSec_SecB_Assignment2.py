#Name: Ahmed Yasser                                   RollNo: 22-10216
#Information Security Sec B Assignment No 2
import rsa

print("Name: Ahmed Yasser\tRollNo: 22-10216\nInformation Security Sec B Assignment No 2\n")
    
# Generate Public and Private Keys and save to file
def generate_keys():
	(pubkey , privkey) = rsa.newkeys(1024) 	                                # generating public key using rsa library built-in method newkeys
	with open('pubkey.txt' , 'wb') as fpub:	                                # opening a file and saving the public key to it
		fpub.write(pubkey.save_pkcs1('PEM'))			
	with open('privkey.txt' , 'wb') as fpriv:                               # opening a file and saving the private key to it
		fpriv.write(privkey.save_pkcs1('PEM'))

# Loading Public and Private Keys from file
def load_keys_from_file():
	with open('pubkey.txt' , 'rb') as fpub:	                                # opening the file and loading the public key from it to the variable
		pubkey = rsa.PublicKey.load_pkcs1(fpub.read())
	with open('privkey.txt' , 'rb') as fpriv:                               # opening the file and loading the private key from it to the variable
		privkey = rsa.PrivateKey.load_pkcs1(fpriv.read())
	return pubkey , privkey			                                # returning the public and private key loaded from the files

# Encrypting the Plain Text using Public Key
def encrypt(message , pubkey):
	return rsa.encrypt(message.encode('utf8') , pubkey)                     # encrypting the plain text to cipher text using RSA library built-in method 'encrypt'

# Decrypting the Cipher Text using the Provate Key to Plain Text
def decrypt(message , privkey):
	return rsa.decrypt(message , privkey)		                        # decrypting the cipher text to plain text using RSA library built-in method 'decrypt'

generate_keys()		                                                        # generating public & private key and saving to the text file
pubkey,privkey = load_keys_from_file()                                          # loading both keys from the file to the variables
a=0
while (a!=3):
    a=input("==========================================\nEnter 1 for entering text\nEnter 2 for entering txt file name\nEnter 3 for exiting the program\nEnter Choice: ")
    if (a.isnumeric()!=True):
            print("Error: Please enter a valid input!")
            continue
    if int(a)==1:
            input_text = input("Enter Text: ")      
    elif int(a)==2:
            b=input("Enter Filename: ")
            try:
                    f = open(b, "r") 				                # opening file to read
            except IOError:
                    print("Error: File name entered does not exist! Please re-enter the correct file name.")
                    continue
            input_text = f.read()			                        # read the content of file and storing it to the variable
    elif int(a)==3:
            break;
    else:
            print("Error: Please enter a valid input!")
            continue
    print("\nPublic Key:",pubkey)		                                # printing public key loaded from the file
    print("\nPrivate Key:",privkey)		                                # printing private key loaded from the file
    print("\nOriginal Text:",input_text)                                        # printing original message(plain text) to the terminal
    encrypted_text = encrypt(input_text,pubkey) 		                # encrypting plain text to the cipher text
    print("\nEncrypted Text:",encrypted_text)			                # printing cipher text encrypted using RSA
    decrypted_text = decrypt(encrypted_text,privkey)		                # decrypting cipher text to the plain text
    print("\nDecrypted Text:",decrypted_text.decode('utf8'),"\n")	        # printing plain text after decryption using RSA

print("**Thanks for using the program! Goodbye :)**")
