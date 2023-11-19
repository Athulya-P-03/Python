def longest_length(word):
    word=max(word,key=len)
    print("Longest word:",word)
    print("Its lenght is", len(word))
a=["book","pen","pencil","bag","calculator"]
longest_length(a)
