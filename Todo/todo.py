tasklist = []

def is_not_blank(s:str)->bool:
    return bool(s and not s.isspace())

def add_task(tasklist: list)-> list:
  task = input("what Do you want to add: ")
  if is_not_blank(task):
    tasklist.append(task)
    return tasklist
  else:
    return tasklist

def remove_task(tasklist: list)-> list:
  selected_task = int(input("which task do you want to remove (Index N°)?: "))
  try:
     print(f"{tasklist.pop(selected_task)} has been removed")
  except IndexError:
     print("The specified task does not exsist")
  return tasklist

def display(tasklist:list)->None:
  if not tasklist:
    print ("YOUR ALL DONE")
  else:
    for count, task in enumerate(tasklist):
      print (f"{count}. {task}")

def menu(tasklist)->None:  
  while True:
    display(tasklist)
    print("")
    print("Please choose your action")
    print("Press A to add a task")
    print("Press R to remove a task")
    print("Press S to save the current task list")
    print ("Press Q to exit the program")
    print("")
    action = input("Please select your action: ").upper()

    match action:
      case "A":
        tasklist = add_task(tasklist)
      case "R":
        tasklist = remove_task(tasklist)
      case "S":
        print("not yet implemented")
      case "Q":
        print("Goodbye")
        break

def main():
    print ("Welcome User")
    print("")
    menu(tasklist)


if __name__ == "__main__":
    main()
