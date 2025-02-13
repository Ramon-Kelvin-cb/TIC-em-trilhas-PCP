LINEBREAKER = "-"*100

UNIDADES_DE_MEDIDA = [
    'Quilograma',
    'Grama',
    'Litro',
    'Mililitro',
    'Unidade',
    'Metro',
    'Centímetro'
]

# Gerador de IDs que são números inteiros
class IdManager:
    def __init__(self):
        self.actual = 0

    def newId(self):
        self.actual += 1
        return self.actual

idManager = IdManager()

# Representação de um objeto na lista de compras
class Produto:
    def __init__(self, nome, unidade, quantidade, descricao):
        self.id = idManager.newId()
        self.nome = nome
        self.unidade = unidade
        self.quantidade = quantidade
        self.descricao = descricao

    # Representação em texto de cada objeto da lista
    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nMedida: {self.unidade}\nQtd: {self.quantidade}\nDescrição: {self.descricao}\n"

lista = []
print("Olá! Seja bem vindo à sua lista de compras, aqui você poderá gerenciar o que você irá comprar!\n")
while True:
    print("Aquui estão seus produtos:\n")
    for produto in lista:
        print(produto)

    print("Funcionalidades:\n(0) Adicionar Produto\n(1) Remover Produto\n(2) Pesquisar produtos por nome\n(s) Sair\n")

    funcionalidade = input("O que deseja fazer? (Digite o número da funcionalidade ou 's' para sair)\n-> ")
    print("")

    match funcionalidade:
        case "s" | "S": # Saindo da lista
            print("Ok, até mais e obrigado pelos peixes!")
            print(LINEBREAKER)
            break
        case "0":
            nome = input("Qual o nome do produto que quer adicionar?\n-> ")
            print("")

            print("Qual das seguintes é a unidade de medida do seu produto?")
            for i, unidade in enumerate(UNIDADES_DE_MEDIDA):
                print(f'({i}) {unidade}')
            unidade = int(input("-> "))
            print("")

            unidade = UNIDADES_DE_MEDIDA[unidade]

            qtd = int(input("Qual é a quantidade desse produto?\n-> "))
            print("")

            dscp = input("Dê uma breve descrição do produto, por favor\n-> ")
            print("")

            produto = Produto(nome, unidade, qtd, dscp)
            lista.append(produto)
            print(f'Produto adicionado com sucesso!\n{LINEBREAKER}')
        case "1": # Removendo item da lista
            if not lista:
                print("Ainda não há produtos em sua lista, que tal adicionar alguns?\n")
                print(LINEBREAKER)
                continue
            else:
                idsInList = [el.id for el in lista]
                toRemove = int(input("Qual o ID do produto que deseja remover?\n-> "))
                print("")

                if not toRemove in idsInList:
                    print(f"Não existe nenhum produto com esse ID, verifique a lista novamente e repita o processo\n{LINEBREAKER}")
                    continue
                else:
                    lista = [obj for obj in lista if obj.id != toRemove]
                    print(f"Produto removido da lista!\n{LINEBREAKER}")
                    continue
        case "2":
            nome = input('Qual o nome do produto que você deseja verificar?\n-> ')
            print("")
            matches = [el for el in lista if el.nome == nome]

            if not matches:
                print(f"Não foi encontrada nenhuma correspondência na lista, repita o processo e verifique a grafia do nome do produto\n{LINEBREAKER}")
            else:
                print(f"Foram encontradas {len(matches)} correspondências:\n")
                for el in matches:
                    print(el)
                print(LINEBREAKER)
