class AutocompleteSystem:
    def __init__(self, words):
        self.words = words

    def search(self, prefix):
        result = []
        for word in self.words:
            if word.startswith(prefix):
                result.append(word)
        return result


# ----- Dynamic Input -----

n = int(input("number of words: "))          # number of words
words = input("enter words: ").split()       # words in one line
if(len(words)!=n):

    print("Error : Number of words doesn't match")
else:
    prefix = input("enter prefix: ").strip()     # prefix to search
    system = AutocompleteSystem(words)
    output = system.search(prefix)
    print("output: ",output)