import random

def greet_protagonist(name="Lucky"):
    """Greets the protagonist with a Housefull-esque flair."""
    greetings = [
        f"Oye {name}! Tension gayi tel lene!",
        f"Kya haal hai, {name} bhai? Folks ki problem, ab hogi bye-bye!",
        f"{name} ji, Housefull ki shaan! Har mushkil hogi aasaan!",
        f"Arre {name}! Apni comedy se machao dhamaal, aur karo sabko khushhaal!",
    ]
    print(random.choice(greetings))

def get_folks_problem():
    """Gets a description of the problem faced by the folks."""
    problem = input("Lucky bhai, batao kya gadbad hai? Folks kis pareshani mein hain? ")
    return problem

def suggest_housefull_solution(problem):
    """Suggests a potentially hilarious and chaotic 'Housefull' style solution."""
    solutions = [
        f"Iska simple solution hai, {problem} ko bhool jao aur ek zabardast gaana shuru kar do!",
        f"Lagta hai thodi confusion ho gayi hai. Ek kaam karo, sab log apni identity badal lo!",
        f"Yeh problem? Chutkiyon ka kaam hai! Bas ek bada sa jhooth bolo aur sab theek ho jayega... shayad!",
        f"Tension not! Ek unexpected guest ko bulao aur dekho kaise sab ulajh jaate hain aur problem gayab ho jaati hai!",
        f"Mera idea hai, ek fake kidnapping plan karo! Sab darr jayenge aur asli problem bhool jayenge!",
        f"Why worry? Ek full-on misunderstanding create karo! Confusion mein hi solution chupa hai!",
        f"Ek kaam karo, sabko ek imaginary dushman ke baare mein batao. Sab usse darr kar yeh bhool jayenge!",
        f"Jab problem samajh na aaye, toh ek shaadi fix kar do! Rishton ki uljhan mein sab bhool jayenge!",
    ]
    print("\nLucky soch raha hai...")
    print(random.choice(solutions))

def ask_for_feedback():
    """Asks the protagonist for feedback on the suggested solution."""
    feedback = input("Lucky bhai, yeh idea kaisa laga? Kuch aur chahiye? (Haan/Nahi): ").lower()
    return feedback

def main():
    """Main function to run the Housefull problem solver."""
    greet_protagonist()
    problem = get_folks_problem()
    print(f"\nAchha, toh yeh problem hai: '{problem}'.")

    suggest_housefull_solution(problem)

    while True:
        feedback = ask_for_feedback()
        if feedback == "haan":
            suggest_housefull_solution(problem)
        elif feedback == "nahi":
            print("\nBas phir kya! Housefull style mein sab theek ho jayega!")
            break
        else:
            print("Lucky bhai ko samajh nahi aaya! 'Haan' ya 'Nahi' bolo!")

if __name__ == "__main__":
    main()
