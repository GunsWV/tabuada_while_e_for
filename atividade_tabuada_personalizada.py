numero = int(input("Digite aqui o numero para tabuada:"))
i = int(input("Agora digite onde a tabuada devera começar:"))
termino = int(input("Digite até qual número o multiplicador deva ir:"))

while i <= termino:
    print(f" {i} x {numero} x {i * numero}")
    i += 1
