class ReverseString:
    def __init__(self, s):
        self.s = s

    def reverse(self):
        return self.s[::-1]

s = input("Enter a string: ")
o = ReverseString(s)
print("Reversed string:", o.reverse())