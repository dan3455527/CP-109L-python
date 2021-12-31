file_name = input("input the file name : ")
file_path = "./Hw12_answer/" + file_name
try:
    file = open(file_path, "r")
    words = file.read().split()
    for word in words:
        word = word.lower()
        if word[0] == "w" and word[-1] == "k":
            print(word)
except:
    raise FileNotFoundError