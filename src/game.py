import random
import time

def math_game():
    print("Willkommen zum Mathe-Spiel! Löse so viele Aufgaben wie möglich innerhalb von 30 Sekunden.")
    
    start_time = time.time()
    time_limit = 30
    correct_answers = 0

    while True:
        # Berechne die verbleibende Zeit
        elapsed_time = time.time() - start_time
        if elapsed_time >= time_limit:
            break

        # Generiere eine einfache Rechenaufgabe
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])

        if operation == '+':
            correct_result = num1 + num2
        elif operation == '-':
            correct_result = num1 - num2
        elif operation == '*':
            correct_result = num1 * num2

        # Zeige die Aufgabe an
        print(f"Was ist {num1} {operation} {num2}?")
        
        try:
            user_answer = int(input("Deine Antwort: "))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")
            continue

        # Überprüfe die Antwort
        if user_answer == correct_result:
            print("Richtig!")
            correct_answers += 1
        else:
            print(f"Falsch! Die richtige Antwort ist {correct_result}.")

    print(f"Zeit vorbei! Du hast {correct_answers} Aufgaben richtig gelöst.")

if __name__ == "__main__":
    math_game()