def check_text():
    intext = input("Get me some text to analyze: ").lower()
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

def present(analysis :dict):
  grouped_analysis = ["words","sentences","letters","symbols"]
  for k in grouped_analysis:
    if k in analysis:
      if analysis[k] == 1:
        print(f" there is 1 {k[:-1]} in the provided text")
      else:
        print(f"there are {analysis[k]} {k} in the provided text")
      analysis.pop(k)
    else:
      print(f"there are no {k} in the provided text")
  analysis["<SPACE>"] = analysis.pop(" ")    
  print(" ")
  print("the following distribution was encountered: ")
  for k,v in analysis.items():
    print(f"{k} was found {v} times")

def main():
  while True:
    try:
      text = check_text()
      break
    except ValueError:
        print("Non ASCII character detected, try again")
    continue
  present(analyse_text(text))

main()
