from collections import defaultdict

def check_text():
    intext = input("Get me some text to analyze: ")
    if intext.isascii():
        return intext.lower()
    else:
        raise ValueError

def analyse_text(text):
   store = defaultdict(int)
   sentence_ends = [".","!","?"]
   if text[-1] in sentence_ends:
       store["words"] += 1
   for element in text:
       store[element]+=1
       if element in sentence_ends:
           store["sentences"] +=1
       elif element == " ":
           store["words"] += 1
       if element.isalpha():
           store["letters"] += 1
       else:
           store["symbols"] += 1
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

  if " " in analysis.keys():
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
