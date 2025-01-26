tasklist = []

def is_not_blank(s:str)->bool:
    return bool(s and not s.isspace())

def add_task(tasklist: list)-> list:
  task = input("what Do you want to add: ")
  if is_not_blank(task):
    tasklist.append(task)
    return tasklist

def remove_task(tasklist: list)-> list:
  selected_task = int(input("which task do you want to remove (Index N°)?: "))
  if tasklist[selected_task]:
     print(f"{tasklist.pop(selected_task)} has been removed")
  else:
     print("The specified task does not exsist")
  return tasklist

def main():
    print("Hello")
    print(add_task(tasklist))
    print(remove_task(tasklist))

if __name__ == "__main__":
    main()
