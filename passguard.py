import sys
import math
import argparse

def calculate_entropy(password):
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password): pool_size += 32

    if pool_size == 0 or len(password) == 0:
        return 0

    return math.log2(pool_size) * len(password)

def main():
    parser = argparse.ArgumentParser(description="Evaluate password and token entropy.")
    parser.add_argument("secret", help="The password or string to check")
    args = parser.parse_args()

    entropy = calculate_entropy(args.secret)
    print(f"\nTarget: {args.secret}")
    print(f"Entropy: {entropy:.2f} bits")

    if entropy < 40:
        print("Status: [WEAK] Highly vulnerable to quick brute-force.")
    elif entropy < 60:
        print("Status: [MODERATE] Acceptable for basic use, weak against targeted cracking.")
    else:
        print("Status: [STRONG] High resistance to offline brute-force attacks.\n")

if __name__ == "__main__":
    main()