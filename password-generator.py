import random
import string

def password_generate(length):
    #All character sets

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    #combine everthing

    all_chars = lower_case + upper_case + digits + symbols

    #ensure password has at least one of each type
    password= [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(symbols)
        ]

    # Fill the rest with random characters
    password += random.choices(all_chars , k=length - 4)

    #Now shuffle to make it unpredictable
    random.shuffle(password)

    return "".join(password)

def main():
    print("\n🔐 Password Generator")

    while True:
        try:
            length = int(input("Enter password length (min 6): "))
            if length < 6:
                print("❌ Password must be at least 6 characters.")
                continue

            password = password_generate(length)
            print(f"\n Your secure password: {password}")

            again = input("\nGenerate another? (yes/no): ").lower()
            if again != "yes":
                print("\n👋 Goodbye!")
                break
        except ValueError:
            print("❌ Please enter a valid number.")


if __name__ == "__main__":
    main()
