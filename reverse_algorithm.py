message = 'This program explains reverse cipher.'

translated = '' #Cipher Text is stored here
i = len(message) - 1

while i > 0:
    translated = translated + message[i]
    i = i - 1
print("The Cipher text is :", translated)