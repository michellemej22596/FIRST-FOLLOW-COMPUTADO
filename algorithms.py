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



def compute_follow(grammar, start_symbol):
    """
    Calcula los conjuntos FOLLOW para cada no terminal de la gramática.
    :param grammar: diccionario con las producciones
    :param start_symbol: símbolo inicial de la gramática
    :return: diccionario con FOLLOW sets
    """
    pass
