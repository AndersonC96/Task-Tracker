# Task Tracker CLI - Gerenciador de Tarefas em Linha de Comando

Um projeto simples em Python para gerenciar tarefas via terminal, armazenando dados em um arquivo JSON. Ideal para quem quer praticar manipulação de arquivos, argumentos de linha de comando e estruturas de dados.

# 🚀 Como Executar o Projeto

## Pré-requisitos

Python 3.x instalado (Download aqui)[https://www.python.org/downloads/]

## Passo a Passo

### 1. **Clone ou Baixe o Projeto**

```bash
git clone https://github.com/AndersonC96/Task-Tracker.git
cd Task-Tracker
```

### 2. **Execute o Script**

```bash
python task_cli.py [comando] [argumentos]
```

# 📋 Comandos Disponíveis

| Comando | Uso | Exemplo |
| --- | --- | --- |
| Adicionar tarefa | `add "Descrição da tarefa"` | `python task_cli.py add "Estudar Python"` |
| Atualizar tarefa | `update ID "Nova descrição"` | `python task_cli.py update 1 "Estudar Django"` |
| Deletar tarefa | `delete ID` | `python task_cli.py delete 1` |
| Marcar como "Em Progresso" | `mark-in-progress ID` | `python task_cli.py mark-in-progress 1` |
| Marcar como "Concluída" | `mark-done ID` | `python task_cli.py mark-done 1` |
| Listar tarefas | `list [status] (opcional: todo, in-progress, done)` | `python task_cli.py list done` |

# 📂 Estrutura do Projeto

```bash
task-tracker-cli/  
├── task_cli.py       # Script principal  
├── tasks.json        # Arquivo de armazenamento (criado automaticamente)  
└── README.md         # Documentação  
```

# 💡 Aprendizados e Habilidades Praticadas

✔ Manipulação de arquivos JSON em Python
✔ Uso de `argparse` para CLI interativo
✔ Estruturação de dados e persistência local
✔ Boas práticas de tratamento de erros