def reverse_words(text):
  #go for it
    split=text.split(" ")
    lst2=[]
    for i in split:
        lst2.append(i[::-1])
    M=" ".join(lst2)
    return M
    