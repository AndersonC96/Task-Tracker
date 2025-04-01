import argparse
import json
import datetime

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: O arquivo tasks.json está corrompido. Iniciando com uma lista vazia.")
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    new_id = max(task['id'] for task in tasks) + 1 if tasks else 1
    new_task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.datetime.now().isoformat(),
        'updatedAt': datetime.datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarefa adicionada com sucesso (ID: {new_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarefa {task_id} tualizada com sucesso.")
            return
    print(f"Error: Tarefa com ID {task_id} não encontrada.")

def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Tarefa {task_id} deletada com sucesso.")
            return
    print(f"Error: Tarefa com ID {task_id} não encontrada.")

def mark_task_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if task['status'] == new_status:
                print(f"Task {task_id} is already {new_status}.")
                return
            task['status'] = new_status
            task['updatedAt'] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarefa {task_id} marcada como {new_status}.")
            return
    print(f"Error: Tarefa com ID {task_id} não encontrada.")

def list_tasks(status_filter=None):
    tasks = load_tasks()
    if status_filter:
        filtered_tasks = [task for task in tasks if task['status'] == status_filter]
    else:
        filtered_tasks = tasks
    if not filtered_tasks:
        print("No tasks to display.")
        return
    for task in filtered_tasks:
        print(f"ID: {task['id']}")
        print(f"Descrição: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Criado em: {task['createdAt']}")
        print(f"Atualizado em: {task['updatedAt']}")
        print("-" * 20)

def main():
    parser = argparse.ArgumentParser(description='Task tracker CLI')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Add command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('description', type=str, help='Descrição da tarefa')

    # Update command
    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('id', type=int, help='ID da tarefa a ser atualizada')
    update_parser.add_argument('description', type=str, help='Nova descrição da tarefa')

    # Delete command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('id', type=int, help='ID da tarefa a ser excluída')

    # Mark in-progress command
    mark_ip_parser = subparsers.add_parser('mark-in-progress')
    mark_ip_parser.add_argument('id', type=int, help='ID da tarefa a ser marcada como "em andamento"')

    # Mark done command
    mark_done_parser = subparsers.add_parser('mark-done')
    mark_done_parser.add_argument('id', type=int, help='ID da tarefa a ser marcada como "concluída"')

    # List command
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('status', nargs='?', default=None, choices=['todo', 'in-progress', 'done'], help='Filtrar tarefas por status')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'mark-in-progress':
        mark_task_status(args.id, 'in-progress')
    elif args.command == 'mark-done':
        mark_task_status(args.id, 'done')
    elif args.command == 'list':
        list_tasks(args.status)

if __name__ == '__main__':
    main()