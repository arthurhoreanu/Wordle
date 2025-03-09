import socket
import json
import random
from multiprocessing import Process


def check_guess(guess, secret_word):
    result = {'letters': [], 'won': False}
    secret_word_count = {letter: secret_word.count(letter) for letter in set(secret_word)}
    guess_status = ['gray'] * len(guess)

    # First pass: mark correct positions (green)
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            guess_status[i] = 'green'
            secret_word_count[guess[i]] -= 1

    # Second pass: mark present but incorrect positions (yellow)
    for i in range(len(secret_word)):
        if guess_status[i] == 'gray' and guess[i] in secret_word and secret_word_count[guess[i]] > 0:
            guess_status[i] = 'yellow'
            secret_word_count[guess[i]] -= 1

    # Build the result
    for i in range(len(guess)):
        result['letters'].append({'letter': guess[i], 'status': guess_status[i]})
    result['won'] = (guess == secret_word)
    return result

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file.readlines()]
    return words

def handle_client(client_socket, address):
    words = load_words('words.txt')
    secret_word = random.choice(words)
    print(f"[{address}] Secret word: {secret_word}")
    max_attempts = 6
    attempts = 0
    try:
        while attempts < max_attempts:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            guess = data.strip().lower()
            attempts += 1
            result = check_guess(guess, secret_word)
            if attempts >= max_attempts and not result['won']:
                result['message'] = f"You've used all attempts. The word was: {secret_word}"
            client_socket.send(json.dumps(result).encode('utf-8'))
            if result['won']:
                break
    except Exception as e:
        print(f"[{address}] Error: {e}")
    finally:
        print(f"[{address}] Connection closed.")
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(5)
    print("Server is running and waiting for connections...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            process = Process(target=handle_client, args=(client_socket, client_address))
            process.start()
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()