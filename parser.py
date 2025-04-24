def load_grammar(file_path):
    grammar = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or "→" not in line:
                continue
            left, right = line.split("→")
            left = left.strip()
            productions = [prod.strip().split() for prod in right.strip().split('|')]
            grammar.setdefault(left, []).extend(productions)
    return grammar
