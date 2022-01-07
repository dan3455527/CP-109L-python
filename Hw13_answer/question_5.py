input_sentence = input("input the sentence: \n")
word_list = []
for word in input_sentence.split():
    word_list.insert(0, word)

print(word_list)
result = " "
result = result.join(word_list)

print(result)