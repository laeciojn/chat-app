# 💬 Chat App

Aplicação de **chat em tempo real** construída com Flask e Flask-SocketIO. As mensagens enviadas por um usuário são transmitidas instantaneamente para todos os clientes conectados por WebSockets.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?logo=flask&logoColor=white)
![Socket.IO](https://img.shields.io/badge/Socket.IO-Real--time-010101?logo=socket.io&logoColor=white)

## ✨ Funcionalidades

- Comunicação em tempo real com Socket.IO;
- Mensagens distribuídas para todos os clientes conectados;
- Interface responsiva e moderna;
- Indicador visual do estado da conexão;
- Validação para impedir mensagens vazias;
- Rolagem automática para a mensagem mais recente;
- Estrutura simples e fácil de expandir.

## 🖼️ Visão geral

A aplicação possui uma interface de chat com:

- cabeçalho com o status da conexão;
- área para exibição das mensagens;
- estado vazio antes da primeira mensagem;
- campo de texto e botão de envio;
- suporte a telas menores.

## 🧰 Tecnologias

- **Python** — linguagem principal;
- **Flask** — servidor web;
- **Flask-SocketIO** — comunicação bidirecional em tempo real;
- **HTML5** — estrutura semântica da interface;
- **CSS3** — layout, responsividade e estilos visuais;
- **JavaScript** — interação com a interface e eventos Socket.IO.

## 📁 Estrutura do projeto

```text
chat-app/
├── app.py                 # Servidor Flask e eventos Socket.IO
├── requirements.txt       # Dependências do projeto
├── static/
│   └── style.css          # Estilos da interface
├── templates/
│   └── index.html         # Página principal do chat
└── README.md
```

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior;
- `pip`;
- Git.

### 1. Clone o repositório

```bash
git clone https://github.com/laeciojn/chat-app.git
cd chat-app
```

### 2. Crie um ambiente virtual

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## ▶️ Como executar

Inicie o servidor com:

```bash
python app.py
```

Depois, abra no navegador:

```text
http://127.0.0.1:5000
```

Para testar o chat, abra a aplicação em duas ou mais abas ou janelas do navegador e envie mensagens. Todas as abas conectadas deverão receber as mensagens em tempo real.

## 🔌 Fluxo de comunicação

1. O navegador acessa a rota `/`.
2. O Flask renderiza `templates/index.html`.
3. O cliente JavaScript estabelece uma conexão Socket.IO.
4. Ao enviar uma mensagem, o cliente emite o evento `message`.
5. O servidor retransmite a mensagem aos clientes conectados.
6. Cada cliente atualiza sua lista de mensagens e rola até o conteúdo mais recente.

O evento utilizado pelo cliente e pelo servidor é:

```text
message
```

## 🛠️ Desenvolvimento

Ao alterar os arquivos da interface, reinicie o servidor quando necessário e atualize o navegador para visualizar as mudanças.

Antes de abrir uma contribuição, verifique:

- se a aplicação inicia corretamente;
- se o envio e o recebimento de mensagens continuam funcionando;
- se a interface permanece utilizável em telas pequenas;
- se não há mensagens vazias sendo enviadas.

## 🔮 Próximas melhorias

- Identificação dos usuários;
- Persistência das mensagens em banco de dados;
- Salas de conversa;
- Autenticação;
- Histórico de mensagens;
- Testes automatizados;
- Configuração para execução em produção;
- Containerização com Docker.

## 📄 Licença

Este projeto ainda não possui uma licença definida.
