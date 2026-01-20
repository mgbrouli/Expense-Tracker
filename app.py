import argparse
from datetime import datetime
from util import Item, write_file, get_id, remove_id, list_itens, update_item

current_datetime = datetime.now()
date_string = current_datetime.strftime("%Y-%m-%d")

parser = argparse.ArgumentParser(description="Gerenciador de finanças pessoais")

subparsers = parser.add_subparsers(dest="command", help="Comandos disponiveis")

#-----Command add ------
parser_add = subparsers.add_parser("add", help="Adicionar nova despesa")
parser_add.add_argument("--description", required=True, help="Descricao da despesa")
parser_add.add_argument("--amount", type=int, required=True, help="Valor da despesa")

# --- Command: remove ---
# Adiciona o subcomando 'remove'
parser_remove = subparsers.add_parser("remove", help="Remover uma despesa")
parser_remove.add_argument("--id", type=int, required=True, help="ID da despesa a ser removida")

# --- COMANDO: list ---
# Adiciona o subcomando 'list' (não precisa de argumentos extras)
parser_list = subparsers.add_parser("list", help="Listar todas as despesas")

# --- COMANDO: summary ---
parser_summy = subparsers.add_parser("summary", help="Soma todos os valores")
parser_summy.add_argument("--month", help="Seleciona o mes qual sera somado")

# --- COMANDO: update ---
parser_update = subparsers.add_parser("update", help="Atualizar uma despesa existente")
parser_update.add_argument("--id", type=int, required=True, help="ID da despesa")
parser_update.add_argument("--description", required=True, help="Nova descrição")
parser_update.add_argument("--amount", type=int, required=True, help="Novo valor")

args = parser.parse_args()

id = get_id()

# Lógica para decidir o que fazer baseado no comando digitado
if args.command == "add":
    print(f"# Expense added sucessfully (ID: {id})")
    new_amount = Item(id , date_string , args.description, args.amount)
    write_file(str(new_amount) + '\n')
    

elif args.command == "remove":
    if remove_id(args.id):
        print(f"ID {args.id} removido com sucesso")
    else:
        print("ID não encontrado")

elif args.command == "list":
    print(f"{'ID':<5} {'DATE':<15} {'Description':<10} {'Amount':<10}")
    for itens in list_itens():
        if itens.strip():
            dados = itens.strip().split("|")

            id_val = dados[0]
            data_val = dados[1]
            desc_val = dados[2]
            amount_val = dados[3]

            print(f"{id_val:<5} {data_val:<15} {desc_val:<10} {amount_val:<10}")

elif args.command == "summary":
    itens = list_itens()
    res = sum(int(item.split("|")[-1]) for item in itens)   
    print("expenses: $", res)

elif args.command == "update":
    if update_item(args.id, args.description, args.amount):
        print(f"ID {args.id} atualizado com sucesso!")
    else:
        print(f"Erro: ID {args.id} não encontrado para atualização.")

else:
    parser.print_help()
