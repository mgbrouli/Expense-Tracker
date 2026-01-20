class Item:

    def __init__(self, id, date, description, amount):
        self.id = id
        self.date = date
        self.description = description
        self.amount = amount
    def __str__(self):
        return f"{self.id}|{self.date}|{self.description}|{self.amount}"


def write_file(text):

    try:
        with open("file.txt", "a") as file:
            file.writelines(text)
    except FileNotFoundError:
        return False
def get_id():
    try:
        id = []
        with open("file.txt", "r") as f:
            for i in f:
                if i.strip():
                    lista = i.split("|")
                    id.append(int(lista[0]))
        return max(id) + 1 if id else 1
    except FileNotFoundError:
        return 1

def remove_id(id_to_remove):
    rest_itens = []
    encontrado = False

    try:
        with open("file.txt", 'r') as f:
            for linha in f:
                if linha.strip():
                    parts = linha.split("|")
                    if int(parts[0]) != id_to_remove:
                        rest_itens.append(linha)
                    else:
                        encontrado = True
        
        with open("file.txt", 'w') as f:
            f.writelines(rest_itens)
        return encontrado
    except FileNotFoundError:
        return False


def list_itens():
    try:
        itens_list = []
        with open("file.txt", "r") as f:
            for linha in f:
                if linha.strip():
                    itens_list.append(linha)
        return itens_list
    except FileNotFoundError:
        return []


def update_item(id_to_update, new_description, new_amount):
    updated_lines = []
    success = False

    try:
        with open("file.txt", "r") as f:
            for linha in f:
                if linha.strip():
                    dados = linha.split("|")
                    if int(dados[0]) == id_to_update:
                        novo_item = Item(id_to_update, dados[1], new_description, new_amount)
                        updated_lines.append(str(novo_item) + "\n")
                        success = True
                    else:
                        updated_lines.append(linha)
        if success:
            with open("file.txt", "w") as f:
                f.writelines(updated_lines)
        return success
    except FileNotFoundError:
        return False
