"""
String: Thisissometext

+-------+  \
|Thisiss|   \ h pixels high
|ometext|   /
+-------+  /

\_______/
  w pixels wide
"""

def get_height(fs):
    """
    Returns the height for the font size.
    """
    return 1

def get_width(fs, char):
    """
    Returns the width for the given character at the given font size.
    """
    return 1

# TBD - implement height and width, as well as the binary search solution

class Solution(object):
    MIN_FS = 8  # minimum font size
    MAX_FS = 96 # maximum font size

    def wrap_text(self, width, height, string):
        font_sizes = [x for x in range(self.MIN_FS, self.MAX_FS + 1)]

        for idx, font_size in enumerate(font_sizes):
            line_width = 0
            line_break = 0
            for char in string:
                width = get_width(font_size, char)
                line_width += width
                if line_width > width:          # overflowing, so word on the next line
                    line_break += 1
                    line_width = width
            if line_break * get_height(font_size) > height:
                return font_sizes[idx]          # previous one should fit, no need to go further
        
        return font_sizes[0]                    # a default

def main():
    s = Solution()

    width = 8
    height = 2
    string = 'Thisissometext'
    print(s.wrap_text(width, height, string))

if __name__ == '__main__':
    main()
