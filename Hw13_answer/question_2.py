input_sentence = input("input the sentence: \n")
word_list = []
for word in input_sentence.split():
    word = word.strip(",.?!")
    word_list.append(word)
print(word_list)
    
