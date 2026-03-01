from agents import CalcAgent, ProfessorAgent
from router import Router


calc = CalcAgent("calculator")
prof=ProfessorAgent("professor")


router = Router([calc,prof])

while True:
    print("\nChoose an agent:")
    print("1. calculator")
    print("2. professor")
    print("Type 'exit' to quit")

    choice = input("Your choice: ").lower()

    if choice == "exit":
        print("Goodbye 👋")
        break


    if choice =="calculator":
        expression = input("type a math expression")
        result= router.execute("calculator",expression)
        print("result:",result)
        break
    
    elif choice == "professor":
        print("\nChoose a topic:")
        print("1. list")
        print("2. tuple")
        print("3. dictionary")

        topic = input("Your topic: ")
        result = router.execute("professor", topic)
        print("Explanation:", result)
        break

    else:
        print("invalid choice")
