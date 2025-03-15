def find_sum(find: float | int, list_: list[float | int]) -> dict:
    assert isinstance(find, float | int), "Invalido o valor 'find' deve ser flutuante ou inteiro"
    assert isinstance(list_, list), "Invalido o valor 'list_' deve ser uma lista com números flutuantes ou inteiros"

    list_.sort()
    sum_: float | int
    for index in list_:
        for v in list_:
            sum_ = v + index
            if sum_ == find: return f"valor encontrado {v} + {index} = {v + index}"


print(find_sum(18, [4, 11, 2, 8, 9]))