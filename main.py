from parser import load_grammar
from algorithms import compute_first, compute_follow

if __name__ == "__main__":
    grammar = load_grammar("grammar.txt")

    print("Gramática cargada:")
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} → {productions}")

    # llamadas a compute_first y compute_follow
