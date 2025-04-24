from parser import load_grammar
from algorithms import compute_first, compute_follow

if __name__ == "__main__":
    grammar = load_grammar("grammar.txt")

    print("Gramática cargada:")
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} → {productions}")

    print("\nConjuntos FIRST:")
    first = compute_first(grammar)
    for symbol, first_set in first.items():
        print(f"Primero({symbol}) = {first_set}")

    print("\nConjuntos FOLLOW:")
    start_symbol = list(grammar.keys())[0]
    follow = compute_follow(grammar, start_symbol, first)
    for symbol, follow_set in follow.items():
        print(f"Siguiente({symbol}) = {follow_set}")