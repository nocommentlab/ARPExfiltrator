import sys, getopt, base64
import binascii
array64 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=")

arrayCipher = None
clear64=""

def Decloakify(arg1, arg2):

    global str_buffer
    global arrayCipher
    global clear64
    
    if arrayCipher is None:
        with open( arg2) as file:
            arrayCipher = file.read().splitlines()
    
    if arg1 not in arrayCipher:
        return None

    clear64 += str(array64[arrayCipher.index(arg1)])
    
    try:
        decoded= str(base64.b64decode( clear64 ).decode('ascii'))
        if('$' in decoded):
            clear64 =""
            return decoded

    except binascii.Error as error:
        pass

    return None



