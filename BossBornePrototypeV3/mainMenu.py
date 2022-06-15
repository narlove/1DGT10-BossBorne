from levels.level1 import run_level1
import os

print("Welcome to BossBorne, a game that involves beating your boss.")
print("Enter start to start the game")
response = str(input(">"))

if response == 'start':
    os.system('cls||clear')
    run_level1()