class reverse:

    def __init__(self, word_s):
        self.s = word_s

    def reverse(self):
        return self.s[::-1]
    
word = input("enter the word to be reversed : ")
rev_ob = reverse(word)
result = rev_ob.reverse()
print("reversed string : ", result)