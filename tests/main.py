point: str = "*"

while True:
    three_range: int = int(input("Digite o tamanho da arvore: "))
    if three_range > 1:
        for _ in range(three_range + 1):
            print(((" " * (three_range - _)) + point * _ ) + (point * _ ))
        break
    print("O valor deve ser maior que 1...")