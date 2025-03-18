code = input("Enter your code: ")
key = int(input("Enter your private key: "))
publicKey = int(input("Enter your public key: "))
codeList = code.split(" ")
message = []

for i in range(len(codeList)):
    codeList[i] = int(codeList[i]) 
    m = int(codeList[i])**key % publicKey 
    m = chr(m)
    message.append(m)
print(message)