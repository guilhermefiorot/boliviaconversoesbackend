# boliviaconversoesbackend

# Conversor de Números Romanos

## Descrição
Uma implementação em Python para conversão de números inteiros para algarismos romanos, desenvolvida utilizando Desenvolvimento Orientado a Testes (TDD).

## Requisitos
- Python 3.12
- pytest (instalável via requirements.txt)

## Instalação
1. Clone o repositório
2. Crie um ambiente virtual (opcional, mas recomendado)
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Executando os Testes
Para rodar os testes, utilize:
```
python -m pytest tests/test_roman_converter.py
```

## Uso
```python
from src.roman_converter import int_to_roman

# Exemplos
print(int_to_roman(2024))  # Saída: MMXXIV
print(int_to_roman(3999))  # Saída: MMMCMXCIX
```

## Limitações
- Suporta números inteiros de 1 a 3999
- Lança exceções para entradas inválidas