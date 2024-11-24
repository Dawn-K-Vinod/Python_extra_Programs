"""
Author: Dawn K Vinod
Date: 24-11-2024
Description: Python program to Encode and decode any given message.
"""
import enchant
dictionary=enchant.Dict("en_US")

def encode_msg(msg):
    shift = int(input("Enter the number in which you want to shift the message upto:"))

    #Encoding process
    encode = ""
    for ch in msg:
        if ch.isalpha():
            offset = 65 if ch.isupper() else 97  # Adjust for uppercase or lowercase
            encode += chr((ord(ch) - offset + shift) % 26 + offset)
        else:
            encode += ch  # non-alphabet characters remains unchanged
    return encode

def decode_msg(msg):
    delimiter = input("Enter the delimiter which is used in the msg that you want to decode\n"
                      "(it can be space or comma or slash etc..) :")
    for shift in range(1, 27):

        #Decoding process
        decode = ""
        for ch in msg:
            if ch.isalpha():
                offset = 65 if ch.isupper() else 97  # Adjust for uppercase or lowercase
                decode += chr((ord(ch) - offset - shift) % 26 + offset)
            else:
                decode += ch  # non-alphabet characters remains unchanged

        #Checking if the decoded msg is meaningful, for each shift
        count = 0
        words = decode.split(delimiter)
        for word in words:
            if word.isalpha():
                if dictionary.check(word):
                    count += 1
            else:
                suggestion = dictionary.suggest(word)
                for j in suggestion:
                    if j in word:
                        count += 1

        #Display decoded msg, if more than half the words in the msg is meaningful
        if count >= len(words) // 2:
            print(f"\nDecoded msg: {decode}\n")
            break
        elif count > 0:
            print(f"Partial Decode (Shift {shift}): {decode}")
            break

    else:
        print("Sorry Its very hard to decode the given msg.")

print("Encode or Decode a Message:")
print("1. Encode")
print("2. Decode")
choice=input("Enter your choice: ")
message=input("Enter your Message: ")

if choice=="1":
    encoded_msg = encode_msg(message)
    print(f"\nEncoded msg: {encoded_msg}\n")
elif choice=="2":
    decode_msg(message)
