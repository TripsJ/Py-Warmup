def check_text():
    intext = input("Get me some text to analyze: ")
    if intext.isascii():
        return intext
    else:
        raise ValueError

def analyse_text(text):
  store = {}
  for letter in text:
    if letter in store:
      store[letter]+=1
    else:
      store[letter] = 1
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
