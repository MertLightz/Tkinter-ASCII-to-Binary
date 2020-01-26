#Tkinter ASCII to Binary
from tkinter import *
from tkinter import messagebox



space = [' ','00100000']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
upper_binary = ['01000001','01000010','01000011','01000100','01000101','01000110','01000111','01001000','01001001','01001010','01001011','01001100','01001101','01001110','01001111','01010000','01010001','01010010','01010011','01010100','01010101','01010110','01010111','01011000','01011001','01011010']
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lower_binary = ['01100001','01100010','01100011','01100100','01100101','01100110','01100111','01101000','01101001','01101010','01101011','01101100','01101101','01101110','01101111','01110000','01110001','01110010','01110011','01110100','01110101','01110110','01110111','01111000','01111001','01111010',]

def ascii_to_binary(binary_label, space, uppercase, upper_binary, lowercase, lower_binary):
    phrase = ASCII_Entry.get()
    count = 0
    converted = ''

    for x in range(0, len(phrase)):
        for i in range(0, len(uppercase)):
            if phrase[x] == uppercase[i]:
                converted += upper_binary[i] + ' '

            elif phrase[x] == lowercase[i]:
                converted += lower_binary[i] + ' '

            elif phrase[x] == space[0]:
                converted += space[1] + ' '
                break

    binary_label.config(text = converted)

root = Tk()
root.title('ASCII to Binary')

ASCII_Label = Label(root, text = 'ASCII:')
ASCII_Label.grid(column = 0, row = 0)

ASCII_Entry = Entry(root)
ASCII_Entry.grid(column = 1, row = 0)

button = Button(root, text = 'CONVERT', command = lambda: ascii_to_binary(binary_label, space, uppercase, upper_binary, lowercase, lower_binary))
button.grid(column = 2, row = 1)

binary = Label(root, text = 'BINARY:')
binary.grid(column = 0, row = 1)

binary_label = Label(root, text = 'N/A')
binary_label.grid(column = 1, row = 1)
