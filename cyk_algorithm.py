import json
import sys

def cyk_algorithm(grammar, string):
    n = len(string)
    r = len(grammar)

    # Inisialisasi tabel CYK
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Invers dari grammar untuk pencarian cepat
    inverse_rules = {}
    for lhs, productions in grammar.items():
        for rhs in productions:
            inverse_rules.setdefault(rhs, set()).add(lhs)

    # Basis: huruf terminal
    for i, char in enumerate(string):
        for lhs in inverse_rules.get(char, []):
            table[0][i].add(lhs)

    # Iterasi untuk substring panjang >= 2
    for l in range(2, n + 1):  # panjang substring
        for s in range(n - l + 1):  # start posisi
            for p in range(1, l):  # split point
                left = table[p - 1][s]
                right = table[l - p - 1][s + p]
                for B in left:
                    for C in right:
                        for lhs in inverse_rules.get(B + C, []):
                            table[l - 1][s].add(lhs)

    # Cek apakah simbol awal S ada di pojok kiri atas
    return "S" in table[-1][0]

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.json>")
        return

    with open(sys.argv[1], "r") as f:
        data = json.load(f)

    grammar = data["grammar"]
    string = data["input"]

    result = cyk_algorithm(grammar, string)
    if result:
        print(f"String '{string}' is ACCEPTED by the grammar.")
    else:
        print(f"String '{string}' is REJECTED by the grammar.")

if __name__ == "__main__":
    main()
