
def encrypt(string, ciphered=[]):
    # let's get the middle point
    l = len(string)
    if l < 1:
        return
    i = int(l / 2)
    # let's course correct according to the algorithm
    if l % 2 == 0:
        i -= 1
    # let's append the character
    ciphered.append(string[i])
    # let's recurse left and then right
    encrypt(string[:i], ciphered)
    encrypt(string[i + 1:], ciphered)

def main():
    S = "abc"
    R = "bac"
    ciphered = []
    encrypt(S, ciphered)
    print(R, ''.join(ciphered))

    S = "abcd"
    R = "bacd"
    ciphered = []
    encrypt(S, ciphered)
    print(R, ''.join(ciphered))

    S = "abcxcba"
    R = "xbacbca"
    ciphered = []
    encrypt(S, ciphered)
    print(R, ''.join(ciphered))

    S = "facebook"
    R = "eafcobok"
    ciphered = []
    encrypt(S, ciphered)
    print(R, ''.join(ciphered))

if __name__ == '__main__':
    main()
