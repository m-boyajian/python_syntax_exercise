"""upper()-It converts the given string into uppercase and returns the string."""

def print_upper_words(words):
    for word in words:
        print(word.upper())

"""The startswith() method returns True if the string starts with the specified value, otherwise False.
example from W3:
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)"""

def print_upper_words2(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

"""Takes in 2 parameters: words and starts-with. If the letter in starts-with matches the starting letter of a word, it will print the word  """
def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

        