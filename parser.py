def load_grammar(file_path):
    grammar = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or "→" not in line:
                continue
            left, right = line.split("→")
            left = left.strip()
            productions_raw = right.strip().split('|')

            productions = []
            for prod in productions_raw:
                symbols = prod.strip().split()
                if symbols == ['ε'] or symbols == ['epsilon']:
                    productions.append(['ε'])  # usamos 'ε' como símbolo especial
                else:
                    productions.append(symbols)

            grammar.setdefault(left, []).extend(productions)
    return grammar
