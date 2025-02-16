# Princípios do design orientado a objetos (SOLID)

> Simple Responsability Principle (Princípio da responsabilidade única)

Uma classe deve ter apenas um motivo para mudar(evite conjuções aditivas: e, bem como, também...). Este principio está intimamente ligado com outro conhecido como `Separation of concens`

> Open/closed principle (Princípio do aberto/fechado)

Classes ou objetos e metodos devem estar abertos para extensão, mas fechados para modificações

> Liskov substituion principle (Princípio da substituição de Liskov)

Classes derivadas devem ser capazer de substituir totalmente classes-bases

> Interface segregation principle (Principio da segregação de interface)

Os clientes não devem ser forçados sa depender de interfaces que não utilizam

> Dependency inversion principle (Principio da inversçao de dependencia)

Módulos de alto nivel não devem ser dependentes do modulos de baixo nivel ambos devem depender de abstrações. Detalhes devem depnder das abstrações, não o inverso.
