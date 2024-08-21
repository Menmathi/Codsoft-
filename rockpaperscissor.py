import tkinter as tk
import random
def play(choice):
 computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
 if choice == computer_choice:
     result = "It's a tie!"
 elif (choice == 'Rock' and computer_choice == 'Scissors') or (choice == 'Scissors' and computer_choice == 'Paper') or (choice == 'Paper' and computer_choice == 'Rock'):
     result = "You win!"
 else:
     result = "Computer wins!"

 result_label.config(text=f"Your Choice: {choice}\nComputer's Choice:{computer_choice}\n{result}")
root = tk.Tk()
root.title("Rock, Paper, Scissors")
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:",
font=("Arial", 14))
instruction_label.pack(pady=10)
rock_button = tk.Button(root, text="Rock", font=("Arial", 16), command=lambda:
play('Rock'))
rock_button.pack(side=tk.LEFT, padx=20)
paper_button = tk.Button(root, text="Paper", font=("Arial", 16),
command=lambda: play('Paper'))
paper_button.pack(side=tk.LEFT, padx=20)
scissors_button = tk.Button(root, text="Scissors", font=("Arial", 16),
command=lambda: play('Scissors'))
scissors_button.pack(side=tk.LEFT, padx=20)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)
root.mainloop()
