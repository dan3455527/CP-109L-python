input_sentence = input("input the sentence: \n")
word_list = input_sentence.split()
print(f"this list has {len(word_list)} elements : ")
for i in range(len(word_list)):
    print(f"{i:<3d}:{word_list[i]}")
print("------------------")
delete_element_num = input("which one to be deleted: ")
word_list.remove(word_list[int(delete_element_num)])
result = " "
result = result.join(word_list)
print(f"Result : {result}")