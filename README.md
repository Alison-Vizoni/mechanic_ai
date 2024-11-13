# Mechanic AI
Este é um projeto de chatbot de aprendizado contínuo voltado para mecanica automotiva, que utiliza as tecnologias LangGraph, 
Langchain e PostgresSaver para gerenciar checkpoints e memória vetorial. A aplicação é desenvolvida com o modelo de linguagem (LLM) Groq, 
utilizando o model ID llama3-70b-8192, oferecendo interações inteligentes e adaptáveis ao usuário. E para facilitar o 
desenvolvimento e a implantação do projeto, utilizei Docker Compose para isolar o ambiente de execução.

# Pré-requisitos
- Docker
- Docker Compose
- Python 3.8+

# Configuração
Para começar, crie um arquivo `.env` na raiz do projeto e adicione as variaveis abaixo:
```
API_KEY=
CHATBOT_MODEL_ID=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB_NAME=
```

# Execução do Projeto
Para inicializar o projeto, basta executar o comando abaixo:

`docker compose up -d`

Agora é só esperar o docker configurar o ambiente e quando estiver finalizado, o chatbot estará disponivel no endereço
`http://localhost:8501` ou o endereço e porta escolhidos no momento de executar o docker compose.

# Finalizar a Execução do Projeto
Quando quiser finalizar a execução do projeto, basta executar o comando `docker compose down` e o docker ira parar 
todos os serviços descritos no arquivo docker-compose.yml do projeto.
