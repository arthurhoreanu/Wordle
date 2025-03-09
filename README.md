# Wordle

Welcome to **Wordle**, a fun and engaging word-guessing game! This project is a simple implementation of the popular game where players have to guess a secret 5-letter word within six attempts.

## Functionalities

- **Server-Client Architecture**: The game uses a Python server to handle game logic and a PHP client for user interaction.
- **Word Validation**: Each guess is validated and feedback is provided to the player.
- **Feedback Mechanism**: Letters are marked as:
  - 🟩 **Green**: Correct letter in the correct position.
  - 🟨 **Yellow**: Correct letter in the wrong position.
  - ⬜ **Gray**: Incorrect letter.

## Rules of the Game

1. **Objective**: Guess the secret 5-letter word.
2. **Attempts**: You have 6 attempts to guess the word.
3. **Feedback**: After each guess, you will receive visual clues:
   - 🟩 Green: The letter is correct and in the right position.
   - 🟨 Yellow: The letter is correct but in the wrong position.
   - ⬜ Gray: The letter is not in the secret word.

## Project Structure

- `words.txt`: List of possible secret words.
- `server.py`: Python server handling game logic and client connections.
- `client.php`: PHP client for user interaction and displaying feedback.
