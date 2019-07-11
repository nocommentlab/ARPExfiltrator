import os, sys, getopt, base64

array64 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=")


def Cloakify( arg1, arg2 ):
    output_buffer = []

    try:
        with open( arg2 ) as file:
            cipherArray = file.readlines()
    except:
        #print ""
        #print "!!! Oh noes! Problem reading cipher '", arg2, "'"
        #print "!!! Verify the location of the cipher file" 
        #print ""
        pass
    
    for char in base64.b64encode(arg1.encode('ascii')):
            #print(char)
            if char != '\n':              
                output_buffer.append(cipherArray[ array64.index(chr(char)) ])
                print(array64[array64.index(chr(char))], end='')
    
    #print(output_buffer)
    
    return output_buffer