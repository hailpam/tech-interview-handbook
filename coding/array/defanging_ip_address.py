# On Leetcode: https://leetcode.com/problems/defanging-an-ip-address/

class Solution(object):
    def defang_ip_address(self, address):
        defanged = list(address)
        for i, c in enumerate(defanged):
            if c == '.':
                defanged[i] = '[.]'
        
        return ''.join(defanged)

def main():
    s = Solution()

    address = "1.1.1.1"
    print(s.defang_ip_address(address))

    address = "255.100.50.0"
    print(s.defang_ip_address(address))

if __name__ == '__main__':
    main()
