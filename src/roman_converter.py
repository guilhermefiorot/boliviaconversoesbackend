def int_to_roman(numero):
    """
    Converte um número inteiro para sua representação em algarismos romanos.

    Args:
        numero (int): Número inteiro a ser convertido (1-3999)

    Returns:
        str: Representação em algarismos romanos

    Raises:
        ValueError: Se o número estiver fora do intervalo suportado
    """
    # Validações iniciais
    if not isinstance(numero, int):
        raise TypeError("O input deve ser um número inteiro")

    if numero < 1 or numero > 3999:
        raise ValueError("O número deve estar entre 1 e 3999")

    # Tabela de mapeamento de valores romanos
    valores_romanos = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    # Conversão
    resultado = ""
    for valor, simbolo in valores_romanos:
        while numero >= valor:
            resultado += simbolo
            numero -= valor

    return resultado
