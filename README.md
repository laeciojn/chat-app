# Chat App

Aplicação de chat em tempo real desenvolvida com **Flask** e **Flask-SocketIO**. As mensagens enviadas por um cliente são transmitidas para todos os clientes conectados por meio de WebSockets.

## Tecnologias

- **Python**
- **Flask** — criação do servidor web
- **Flask-SocketIO** — comunicação em tempo real
- **HTML** — estrutura da interface
- **CSS** — estilos da aplicação
- **Socket.IO** — conexão entre o navegador e o servidor

## Funcionalidades

- Interface simples para envio de mensagens;
- Comunicação em tempo real;
- Distribuição das mensagens para todos os clientes conectados;
- Layout básico responsivo para a tela de chat.

## Estrutura do projeto

```text
chat-app/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Pré-requisitos

- Python 3.8 ou superior;
- `pip` instalado.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/laeciojn/chat-app.git
   cd chat-app
   ```

2. Crie e ative um ambiente virtual:

   **Linux/macOS:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows:**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Como executar

Inicie a aplicação com:

```bash
python app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

Para testar a comunicação em tempo real, abra a aplicação em duas ou mais abas do navegador e envie mensagens.

## Como funciona

- A rota `/` renderiza a interface definida em `templates/index.html`.
- O cliente estabelece uma conexão Socket.IO com o servidor.
- Quando uma mensagem é enviada, o evento `message` é emitido para o servidor.
- O servidor retransmite a mensagem para todos os clientes conectados.

## Dependências

As dependências do projeto estão definidas em `requirements.txt`:

```text
flask
flask-SocketIO
```

## Melhorias futuras

- Adicionar identificação dos usuários;
- Persistir mensagens em um banco de dados;
- Criar salas de conversa;
- Adicionar autenticação;
- Melhorar o layout e a experiência em dispositivos móveis;
- Configurar execução para produção.

## Licença

Este projeto ainda não possui uma licença definida.
