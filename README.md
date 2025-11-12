# cadastrocliente_mysql
O Projeto CadastroCliente_Mysql é um sistema Full-Stack projetado para gerenciar informações de cadastro de clientese realizando o CRUD de Clientes. O design prioriza a simplicidade, eficiência e clareza na separação de responsabilidades entre o Backend (API) e o Frontend (Interface do Usuário).
🚀 Projeto CRUD de Clientes (Full-Stack)Este projeto implementa um sistema básico de Cadastro, Leitura, Atualização e Exclusão (CRUD) para clientes. Utiliza uma arquitetura Full-Stack simples, combinando um Backend robusto em Python (Flask) e um Frontend leve em HTML/JavaScript.🛠️ Tecnologias Utilizadas|| Camada | Tecnologia | Finalidade || Backend (API) | Python 3.x | Linguagem principal. ||  | Flask | Micro-framework para o servidor REST. ||  | Flask-Smorest | Geração automática da documentação Swagger/OpenAPI. ||  | Flask-SQLAlchemy | ORM para manipulação do banco de dados. || Banco de Dados | MySQL | Persistência e armazenamento de dados. || Frontend (UI) | HTML, CSS Puro, JS (Vanilla) | Interface de usuário e comunicação com a API via fetch. |
⚙️ Estrutura do ProjetoA organização dos arquivos segue o padrão de separação de responsabilidades:
/projeto_clientes/
|-- app.py             # Lógica do Backend, Rotas (API) e Modelagem.
|-- config.py          # Configurações do Flask e String de Conexão com o DB.
|-- requirements.txt   # Lista de dependências Python.
|-- README.md          # Esta documentação.
|-- static/            # Frontend (Servido diretamente pelo Flask)
|   |-- index.html     # Estrutura e Estilo (CSS incorporado).
|   |-- script.js      # Lógica de CRUD (Requisições HTTP).
📦 Instalação e Execução (Passo a Passo)Para rodar o projeto localmente, siga os passos abaixo:Pré-requisitosTer Python 3.8+ instalado.Ter um servidor MySQL/MariaDB instalado e em execução.1. Configuração do Banco de DadosCrie um banco de dados vazio no seu servidor MySQL (ex: crud_clientes).Em seguida, abra o arquivo config.py e atualize a variável SQLALCHEMY_DATABASE_URI com suas credenciais:# Exemplo de configuração no config.py (AJUSTAR CREDENCIAIS)
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://USUARIO:SENHA@localhost/NOME_DO_BANCO'
    # ... demais configurações ...
2. Instalação das DependênciasAbra o terminal na pasta raiz do projeto:# 1. (Opcional) Crie e ative um ambiente virtual
python -m venv venv
# Windows: 
## venv\Scripts\activate
# Linux/macOS: 
## source venv/bin/activate
# 2. Instale todas as bibliotecas necessárias
## pip install -r requirements.txt
# 3. InicializaçãoExecute o script principal do Flask.  
As tabelas do banco de dados serão criadas automaticamente (db.create_all()):python app.py
O servidor estará ativo em http://127.0.0.1:5000/.
🌐 Acesso à Aplicação e APICom o servidor Flask rodando, você tem acesso a duas interfaces principais:1. Frontend (Interface do Usuário)Este é o sistema completo para interagir visualmente com o CRUD.URL de Acesso: http://127.0.0.1:5000/app2. Documentação Interativa da API (Swagger UI)O Swagger é essencial para testar e depurar a API isoladamente, sem depender da interface.URL de Acesso: http://127.0.0.1:5000/swagger
📝 Detalhes do Backend (API RESTful)O Backend é construído com base em Blueprints e MethodViews do Flask-Smorest.Endpoint Base: /clientes| Rota | Método | Função | Detalhes || /clientes | GET | Listar Clientes | Retorna um array JSON de todos os clientes. || /clientes | POST | Criar Cliente | Recebe JSON, valida (CPF/Email únicos) e insere no DB. || /clientes/<int:id> | GET | Detalhar Cliente | Busca cliente por ID (ou retorna 404). || /clientes/<int:id> | PUT | Atualizar Cliente | Atualiza todos os campos do cliente pelo ID. || /clientes/<int:id> | DELETE | Excluir Cliente | Remove o cliente pelo ID (ou retorna 404). |Modelagem de DadosO modelo ClienteModel mapeia diretamente para a tabela cliente no MySQL.| Coluna | Restrições Importantes || id | Chave Primária || cpf | Único e Não Nulo || email | Único || nome | Não Nulo |
🎨 Detalhes do FrontendO design é implementado usando CSS puro (integrado no <style>) com foco em:Responsividade: O layout se adapta bem a diferentes tamanhos de tela (desktop, tablet, mobile).Feedback: A função showMessage em script.js usa classes CSS para exibir mensagens de sucesso (verde) e erro (vermelho) de forma destacada para o usuário.Interação: O script.js gerencia o formulário para operações POST/PUT e popula a tabela com os dados obtidos da API via GET.
🤝 ContribuiçõesSinta-se à vontade para sugerir melhorias, como a adição de paginação, filtros de busca, ou a migração do CSS puro para um framework (como Tailwind CSS ou Bootstrap).
