def is_not_blank(s:str)->bool:
    return bool(s and not s.isspace())

def add_task(tasklist: list[str])-> list:
  task = input("what Do you want to add: ")
  if is_not_blank(task):
    tasklist.append(task)
    return tasklist
  else:
    return tasklist

def remove_task(tasklist: list[str])-> list:
  if not tasklist:
    print ("No Tasks in list")
    return tasklist

  while True:
    userinput = input("which task do you want to remove (Index N°)?: ")
    if userinput.isdigit():
      selected_task = int(userinput)
      break
    else:
      continue

  try:
     print(f"{tasklist.pop(selected_task)} has been removed")
  except IndexError:
     print("The specified task does not exsist")
  return tasklist

def display(tasklist:list[str])->None:
  if not tasklist:
    print ("YOUR ALL DONE")
  else:
    for count, task in enumerate(tasklist):
      print (f"{count}. {task}")

def save_to_file(tasklist :list[str])->bool:
  with open("tasks.txt","w") as file:
    for element, task in enumerate(tasklist):
      file.write(f"{element}. {task}\n")
    return True

def menu(tasklist)->None:  
  while True:
    print("")
    print("Please choose your action")
    print("Press A to add a task")
    print("Press D to display the task list")
    print("Press R to remove a task")
    print("Press L to load a tasklist from a file")
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
        print("saving...")
        if save_to_file(tasklist):
          print("Tasks saved to tasks.txt")
        else:
          print("saving failed")
      case "D":
        print("")
        print("-"*30)
        display(tasklist)
        print("-"*30)
      case "Q":
        print("Goodbye")
        break
      case _:
        print("invalid inuput")

def main():
    tasklist = []
    print ("Welcome User")
    print("")
    print("-"*30)
    display(tasklist)
    print("-"*30)
    menu(tasklist)


if __name__ == "__main__":
    main()
