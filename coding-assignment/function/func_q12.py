# Find the Largest Word in a Sentence
def largest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

sentence = input("Enter a sentence: ")
print(f"The largest word in the sentence is: '{largest_word(sentence)}'.")
