# Chat App

Uma aplicação de comunicação em tempo real desenvolvida para demonstrar uma experiência de chat simples, rápida e extensível com Flask e Flask-SocketIO.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Socket.IO](https://img.shields.io/badge/Socket.IO-real--time-010101?logo=socket.io&logoColor=white)](https://socket.io/)

## Sobre o projeto

O Chat App conecta múltiplos clientes em uma mesma conversa e distribui as mensagens instantaneamente por meio de WebSockets. O projeto combina uma base backend objetiva com uma interface responsiva, acessível e preparada para futuras evoluções.

A implementação mantém o evento `message` como contrato central entre cliente e servidor, deixando a arquitetura simples de entender e fácil de ampliar.

## Destaques

- Comunicação bidirecional em tempo real;
- Atualização instantânea para todos os clientes conectados;
- Interface responsiva para desktop e dispositivos móveis;
- Indicador visual do estado da conexão;
- Prevenção de mensagens vazias;
- Rolagem automática para o conteúdo mais recente;
- HTML semântico e estados de foco acessíveis;
- Estrutura enxuta para prototipação e aprendizado.

## Stack tecnológica

| Camada | Tecnologia | Responsabilidade |
| --- | --- | --- |
| Backend | Python e Flask | Servidor web e roteamento |
| Real-time | Flask-SocketIO | Eventos e comunicação bidirecional |
| Interface | HTML5 | Estrutura semântica |
| Estilos | CSS3 | Layout responsivo e identidade visual |
| Cliente | JavaScript | Interação e eventos Socket.IO |

## Estrutura

```text
chat-app/
├── app.py                 # Aplicação Flask e eventos Socket.IO
├── requirements.txt       # Dependências do projeto
├── static/
│   └── style.css          # Estilos da interface
├── templates/
│   └── index.html         # Cliente web do chat
└── README.md              # Documentação
```

## Primeiros passos

### Requisitos

- Python 3.8 ou superior;
- pip;
- Git.

### Instalação

```bash
git clone https://github.com/laeciojn/chat-app.git
cd chat-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

No Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Execução

```bash
python app.py
```

Acesse `http://127.0.0.1:5000` no navegador. Para validar a comunicação em tempo real, abra a aplicação em duas ou mais abas e envie mensagens entre elas.

## Como funciona

1. O Flask disponibiliza a rota principal `/`.
2. O servidor renderiza `templates/index.html`.
3. O navegador abre uma conexão Socket.IO.
4. O formulário emite o evento `message` ao enviar uma mensagem válida.
5. O servidor retransmite o conteúdo para os clientes conectados.
6. Cada cliente atualiza a conversa e mantém a mensagem mais recente visível.

## Contrato de eventos

O evento utilizado na comunicação entre frontend e backend é:

```text
message
```

Esse contrato deve ser preservado ao adicionar novos recursos para manter a compatibilidade entre o servidor e a interface web.

## Diretrizes de desenvolvimento

Antes de enviar alterações, valide:

- inicialização correta da aplicação;
- envio e recebimento de mensagens em múltiplas abas;
- comportamento em telas pequenas;
- tratamento de mensagens vazias;
- atualização correta do estado da conexão;
- ausência de alterações acidentais no contrato `message`.

## Próximas possibilidades

- Identidade e presença dos usuários;
- Persistência e histórico de mensagens;
- Salas e conversas privadas;
- Autenticação e autorização;
- Notificações e indicador de mensagens não lidas;
- Testes automatizados;
- Observabilidade e logs estruturados;
- Empacotamento com Docker;
- Configuração para produção.

## Licença

Este projeto ainda não possui uma licença definida.
