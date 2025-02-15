term = ['T', 'E', 'R', 'M', 'O']
term_digited = []

for n in range(5):
    value_digited = str(input(f"Digite a {n+1}° palavra: "))
    if value_digited in term:
        print("tem")
    else:
        print("Não tem")
    term_digited.append(value_digited)

print(term)
print(term_digited)