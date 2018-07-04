## VOLI (Vó Online)

> Livro de receitas dos tempos modernos.

A Voli é um agregador de receitas que se propõe a não ficar no caminho entre você e sua comida. Oferecendo uma interface minimalista para visualizar e salvar receitas e  um bot de Telegram, suas receitas estão sempre a mão.

Outras características relevantes:

- Serviço self-hosted
- Proposta de comunicação entre as diferentes instâncias (federação)
- Desenvolvido em Python + Django

### Funcionalidades (road map)

- (OK) Adicionar links de receitas através do bot no telegram ou site, opcionalmente com nome e tags
- (OK) Página responsiva para visualizar as receitas
- (OK) Filtrar receitas salvas por tags
- Campo de pesquisa na página
- Adicionar receitas diretamente (sem um link)
- Extrair (Scrapy) informações de receitas adicionadas com link
- Melhorar interface do Bot com teclados modificados
- Criar bot inline para buscar e enviar receitas a amigos sem sair da conversa
- Extrair ingredientes e quantidades das receitas
- Apresentar informações nutricionais sobre ingredientes
- Estimar informaçoes nutricionais das receitas e custo

### Colabore

Para rodar o projeto em sua maquina, primeiro certifique-se de que tenha:

- git
- Python 3.6.4
- Um token para o bot. Você pode conseguir um conversando com o BotFather: https://telegram.me/botfather

Depois, siga os passos abaixo:

```bash
# Clonar o repositório
$ git clone https://github.com/vractal/voli.git

# Criar e ativar um virtualenv
$ python3 -m venv .voli
$ source .voli/bin/activate

# Instalar as dependências de desenvolvimento
$ pip install -r requirements-dev.txt

# Criar o schema do banco de dados
$ python manage.py migrate

# Criar a variável "token" dentro do app do bot
# Substitua '<token>' por seu token, mantendo o resto.
$ echo token=\"<token>\" > voli/telebot/token.py

# Por fim, rodar os testes
$ python manage.py test
```

Se não apresentar nenhum erro, já está tudo pronto. Para iniciar a aplicação, rode esses comandos (cada um em uma aba do terminal):

```bash
# Iniciar o bot
$ python manage.py startbot
# Iniciar o servidor de testes
$ python manage.py runserver
```

### Licença

[GNU General Public License version 3](https://www.gnu.org/licenses/gpl.html)
