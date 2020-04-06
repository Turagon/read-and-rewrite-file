def file_read(file_name) :
    word = []
    with open(file_name, "r", encoding = "Big5") as f:
        for w in f :
            word.append(w.strip("\n"))
    return word

def dictionary(r_file_read) :
    dictionary = {}
    n = 0
    for line in r_file_read :
        for w in line :
            if w == "，" :
                continue
            elif w in dictionary :
                dictionary[w] += 1
            else :
                dictionary[w] = 1
    return dictionary

def main() :
    word = file_read("dict.txt")
    dictionary1 = dictionary(word)
    d = sorted(dictionary1.items(), key = lambda item:item[1], reverse = True )
    print(d)
    print(len(dictionary1))
    
    while True :
        w = input("Please input the word you want to look up")
        if w in dictionary1 :
            print("This is the result : ", dictionary1[w])
        elif w == "q" :
            break
        else :
            print("The word does not in dictionary")

main()




