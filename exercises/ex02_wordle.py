"""Program to replicate Wordle"""

__author__: str = "730573512"


def contains_char(target_str: str, target_char: str) -> bool:
    """Checks if a character is present in a string"""
    assert len(target_char) == 1, f"len('{target_char}') is not 1"
    idx = 0
    while idx < len(target_str):
        """Iterates each letter in word to check if it contains target character"""
        if target_str[idx] == target_char:
            return True
        idx += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Compares guess to secret and returns a string of emojis"""
    assert len(guess) == len(secret_word), "Guess must be same length as secret"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    WHITE_BOX: str = "\U00002B1C"
    idx = 0
    emoji = ""

    while idx < len(guess):
        if guess[idx] == secret_word[idx]:
            emoji += GREEN_BOX
            """Iterates each guess letter index matches the secret index, adds emoji"""
        elif contains_char(target_str=secret_word, target_char=guess[idx]):
            """Iteratives each guess contains any letter of secret, adds emoji"""
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
            """Adds white emoji to output if the above statements are False"""
        idx += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Prompts user for a guess of the correct length"""

    word_guess = input(f"Enter a {expected_length} character word:")
    while len(word_guess) != expected_length:
        word_guess = input(f"That wasn't {expected_length} chars! Try again:")
    return word_guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turn = 1
    secret_len = len(secret)
    """Variables initialized above since they change with each run of main function"""
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        main_guess = input_guess(secret_len)
        """main_guess variable calls input_guess function to store a guess each loop"""
        if main_guess == secret:
            print(f"You won in {turn}/6 turns!")
            return None
        turn_result = emojified(main_guess, secret)
        """turn_result variable changes each loop so emojis change based on the guess"""
        print(turn_result)
        turn += 1
    print("X/6- Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main(secret="codes")
