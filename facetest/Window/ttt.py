table = "abcdefghijklmnopqrstuvwxyz"
def encode(message,key):
    message = message.replace(" ","");
    result = ""
    keylen = len(key)
    messagelen = len(message)
    _round = messagelen // keylen
    remain = messagelen % keylen
    for i in range(_round):
        for j in range(keylen):
            move = table.index(key[j])
            code = table[(table.index(message[i*keylen+j])+move)%26]
            result += code
    for i in range(remain):
        move = table.index(key[i])
        code = table[(table.index(message[_round*keylen+i])+move)%26]
        result += code
    return result

def decode(code,key):
    code = code.replace(" ","");
    result = ""
    keylen = len(key)
    codelen = len(code)
    _round = codelen // keylen
    remain = codelen % keylen
    for i in range(_round):
        for j in range(keylen):
            move = table.index(key[j])
            message = table[(table.index(code[i*keylen+j])-move)%26]
            result += message
    for i in range(remain):
        move = table.index(key[i])
        message = table[(table.index(code[_round*keylen+i])-move)%26]
        result += message
    return result

def main():
    message = input("Message:")
    key = input("Key:")
    code = encode(message,key)
    print(code)
    message = decode(code,key)
    print(message)

if __name__ == "__main__":
    main()