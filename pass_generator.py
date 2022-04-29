import random
import string


def run():
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=64))
    print(f"Tu nuevo password es: {password}.")


if __name__ == "__main__":
    run()