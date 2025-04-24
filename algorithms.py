def compute_first(grammar):
    first = {symbol: set() for symbol in grammar}

    def first_of(symbol, visited=set()):
        if symbol not in grammar:
            return {symbol}

        if symbol in visited:
            return set()  # Evita recursión infinita por recursividad izquierda

        visited.add(symbol)

        result = set()
        for production in grammar[symbol]:
            for i, sym in enumerate(production):
                sym_first = first_of(sym, visited.copy())
                result |= (sym_first - {'ε'})
                if 'ε' not in sym_first:
                    break
            else:
                result.add('ε')

        first[symbol] |= result
        return first[symbol]

    for non_terminal in grammar:
        first_of(non_terminal)

    return first


def compute_follow(grammar, start_symbol, first_sets):
    follow = {symbol: set() for symbol in grammar}
    follow[start_symbol].add('$')

    changed = True
    while changed:
        changed = False
        for A, productions in grammar.items():
            for production in productions:
                for i in range(len(production)):
                    B = production[i]
                    if B in grammar:  # Solo calcular FOLLOW para no terminales
                        beta = production[i + 1:]

                        # FIRST(beta)
                        first_beta = set()
                        if beta:
                            for symbol in beta:
                                # Si es terminal, su FIRST es él mismo
                                if symbol in grammar:
                                    first_beta |= (first_sets[symbol] - {'ε'})
                                else:
                                    first_beta.add(symbol)
                                    break
                                if 'ε' not in first_sets[symbol]:
                                    break
                            else:
                                first_beta.add('ε')

                            before = len(follow[B])
                            follow[B] |= (first_beta - {'ε'})
                            if 'ε' in first_beta:
                                follow[B] |= follow[A]
                            if len(follow[B]) > before:
                                changed = True
                        else:
                            before = len(follow[B])
                            follow[B] |= follow[A]
                            if len(follow[B]) > before:
                                changed = True

    return follow                   