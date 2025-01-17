def check_text():
    intext = input("Get me some text to analyze: ")
    if intext.isascii():
        return intext
    else:
        raise ValueError

def analyse_text(text):
    words = 0
    letters  = 0
    symbols = 0
    sentences = 0
    sentence_ends = [".","!","?"]
    store = {}
    if text[-1] in sentence_ends:
        words += 1
    for element in text:
        if element in store:
            store[element]+=1
        else:
            store[element] = 1
        if element in sentence_ends:
            sentences +=1
        elif element == " ":
            words += 1
        if element.isalpha():
            letters += 1
        else:
            symbols += 1
    store["letters"] = letters
    store["symbols"] = symbols
    store["sentences"] = sentences


    return store

def main():
  while True:
    try:
      text = check_text()
      break
    except ValueError:
        print("Non ASCII character detected, try again")
        continue
    
  print(analyse_text(text))

main()
