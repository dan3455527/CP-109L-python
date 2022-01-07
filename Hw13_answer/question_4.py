input_sentence = input("input the sentence: \n")
word_list = input_sentence.split()
print(f"this list has {len(word_list)} elements : ")
for i in range(len(word_list)):
    print(f"{i:<3d}:{word_list[i]}")
print("------------------")
insert_element_num = input("which one to be insert: ")
insert_element = input("what to insert : ")
word_list.insert(int(insert_element_num), insert_element)
result = " "
result = result.join(word_list)
print(f"Result : {result}")