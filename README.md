# Analisador de Vídeos do YouTube 🎥

Este projeto é uma aplicação web para analisar vídeos do YouTube utilizando a API do YouTube e o Google Gemini API. A aplicação permite que o usuário insira a URL de um vídeo e receba uma análise que resume o conteúdo e identifica o tema central do vídeo.

## 🚀 Funcionalidades

- **Análise de Vídeos**: O usuário pode inserir a URL de um vídeo do YouTube e receber uma análise automática.
- **Alternância de Tema**: Alternância entre tema claro e escuro.
- **Interface Minimalista**: Layout intuitivo e fácil de usar, com um design limpo e moderno.

## 🔧 Pré-requisitos

Antes de iniciar, você vai precisar das seguintes ferramentas:

- Python 3.9
- Conta de desenvolvedor Google para configurar as APIs
- Dependências listadas em `requirements.txt`

## ⚙️ Configuração

### Passo 1: Clone o Repositório

~~~~bash
git clone https://github.com/seu-usuario/analist_videos.git
cd analist_videos
~~~~

### Passo 2: Crie o Ambiente Virtual e Instale as Dependências
~~~~
python3 -m venv venv
# No Windows: venv\Scripts\activate
pip install -r requirements.txt
~~~~

### Passo 3: Configure as Credenciais de API

1. API do YouTube Data: Gere uma chave de API do YouTube Data e adicione-a ao arquivo .env.
2. Google Gemini API: Gere uma chave de API do Google Gemini e adicione-a também ao arquivo .env.

No arquivo .env, insira as chaves da seguinte forma:

~~~~plaintext
YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
~~~~

### Passo 4: Execute o Servidor
~~~~bash
flask run
~~~~
Abra o navegador e acesse http://127.0.0.1:5000 para usar a aplicação.

## 🌌 Uso da Aplicação

1. Cole a URL do vídeo do YouTube na caixa de entrada.
2. Clique em "Analisar" para iniciar a análise do conteúdo.
3. Veja o resumo do vídeo e o tema central na área de resultado.

## Exemplo
Insira uma URL de vídeo, e o aplicativo retorna:

>**Título:** Exemplo de Título de Vídeo
>
>**Descrição:** Exemplo de descrição do vídeo...
>
>Resumo: O vídeo aborda temas relacionados a...
>
>Tema Central: Educação em tecnologia.

## 🖌️ Alternância de Tema
A aplicação possui um botão de alternância de tema, permitindo a mudança entre o tema claro e o tema escuro. O botão está localizado no canto superior da interface.

## 📁 Estrutura do Projeto

~~~~
analist_videos/
├── static/
│   ├── styles.css        # Estilos da aplicação
│   └── scripts.js        # Script para alternância de tema
├── templates/
│   └── index.html        # Interface principal
├── main.py                # Lógica principal da aplicação
~~~~

## 🛠 Tecnologias Utilizadas

* Python: Linguagem principal para desenvolvimento backend.
* Flask: Framework web para a criação da aplicação.
* YouTube Data API: Para acessar dados dos vídeos do YouTube.
* Google Gemini API: Para geração de análise do conteúdo do vídeo.
* Bootstrap Icons: Ícones para design da interface.
* HTML, CSS e JavaScript: Para construção e estilo da interface.

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias e novas funcionalidades.
