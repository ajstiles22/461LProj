def customEncrypt(inputText, n, d):
    reversedText = ''
    for v in range(len(inputText) - 1, -1, -1):
        reversedText += inputText[v]
    #print(reversedText)
    encryptedText = ''
    for v in range(0, len(reversedText)):
        if d == 1: 
            encryptedText += chr(ord(reversedText[v]) + n)
        elif d == -1: 
            encryptedText += chr(ord(reversedText[v]) - n)
    return encryptedText