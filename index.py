with open('uz_good_train_words.csv', 'r') as file:
 
 i= 1
 for line in file:
    words = line.strip().split(',')
    word = words[1]
    middle_word = word.split()[0]
    print(middle_word)
    with open(f"data_uz/train/pos/{i}.txt", "w") as f:
        f.write(middle_word)
    i+=1