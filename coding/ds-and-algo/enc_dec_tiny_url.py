import random

# On Leetcode: https://leetcode.com/problems/encode-and-decode-tinyurl/

class Solution(object):
    """
    The main idea consists in creating a fixed-size code mapping the long URL. The algorithm
    defines a typical code generation method which is leverage to create the mapping, upon
    encoding. Upon decoding, instead, the code maps the long URL back and allows to retrieve
    it.
    """

    BASE_URL = 'http://tinyurl.com/%s'
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz_-ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%*0123456789'

    def __init__(self, code_len=6):
        self.long_url_dict = {}
        self.short_url_dict = {}
        self.code_len = code_len

    def __generate_code(self):
        chars = []
        for _ in range(self.code_len):
            chars.append(self.ALPHABET[random.randint(0, len(self.ALPHABET) - 1)])
        
        return ''.join(chars)

    def encode_url(self, url):
        code = None
        while True:
            code = self.__generate_code()
            if code not in self.short_url_dict:
                self.short_url_dict[code] = url
                break
        
        return self.BASE_URL % code

    def decode_url(self, url):
        code = url.split('/')[3]
        if code not in self.short_url_dict:
            return None
        
        return self.short_url_dict[code]

def main():
    s = Solution()

    url = 'https://leetcode.com/problems/encode-and-decode-tinyurl/'
    tiny_url = s.encode_url(url)
    print(tiny_url)
    long_url = s.decode_url(tiny_url)
    print(long_url)

if __name__ == '__main__':
    main()
