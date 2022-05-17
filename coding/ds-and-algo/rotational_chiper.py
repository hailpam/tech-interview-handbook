
chars = list('abcdefghijklmnopqrstuvwxyz')

def find(char):
    for i, elem in enumerate(chars):        # O(26) ~ O(1)
        if char == elem:
            return i
    return -1

def cipher(string, factor):
    l_string = list(string)
    for i, char in enumerate(l_string):     # O(N), N is the length of the string
        # assuming that this is the only separator character...
        if char == '-':
            continue
        try:
            x = int(char)
            # it is a legit integer
            x += factor
            l_string[i] = str(x % 10)
        except:
            # it is a legit char, assume that -1 is never returned
            j = find(char.lower())
            j += factor
            # restore in case of uppercase character
            if char.isupper():
                x = chars[j % len(chars)].upper()
            else:
                x = chars[j % len(chars)]
            l_string[i] = x
    return ''.join(l_string)

def main():
    string = 'Zebra-493'
    print('Zebra-493', 'Cheud-726', cipher(string, 3))

    string = 'abcdefghijklmNOPQRSTUVWXYZ0123456789'
    print('abcdefghijklmNOPQRSTUVWXYZ0123456789', 'nopqrstuvwxyzABCDEFGHIJKLM9012345678', cipher(string, 39))

if __name__ == '__main__':
    main()
