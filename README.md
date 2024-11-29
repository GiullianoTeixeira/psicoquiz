# Psicoquiz
Esse projeto é destinado ao ensino de programação em Python para alunos do projeto "Olá, Mundos!" da Conpec.

O projeto é um quiz para avaliar alguns aspectos psicológicos do usuário e devolver um parecer, dicas e orientações em caso de respostas com tendências ruins. Vale ressaltar que o resultado **não é um diagnóstico**, apenas um direcionamento ao usuário com base em suas respostas.

O objetivo deste projeto é praticar os conhecimentos de lógica de programação, condicionais, laços e funções usando, principalmente, os arquivos `.py` e as relações entre eles.

# Como acessar o quiz
O quiz foi hosteado usando PythonAnywhere e pode ser acessado [aqui](https://bit.ly/psicoquiz). Se esse link não funcionar, avise-me o quanto antes.

Esse quiz foi feito para uso em telas grandes.

# Principais arquivos e pastas
As seguintes explicações foram dadas ao grupo responsável por esse projeto. Elas estão aqui de modo adaptado.

## Resumo dos arquivos Python do projeto

- **app.py** → arquivo central, responsável por iniciar o quiz.
- **config.py** → configura uma chave secreta que se relaciona aos cookies salvos pelo quiz (basicamente, para se lembrar se o usuário atual é novo ou não).
- **routes.py** → estabelece conexões (rotas) entre as páginas do quiz.
- **logic.py** → define a lógica de cálculo e impressão dos resultados ao usuário.
- **questions.py** → reúne perguntas, respostas e seus pesos.
- **results.py** → associa um número a um resultado.
- **text.py** → reúne todo o texto do quiz.

## Resumo dos outros arquivos e pastas do projeto

- A pasta **templates** possui os arquivos `.html`, que definem a estrutura do site.  
- A pasta **static** possui imagens e um arquivo `.css`, que define a estética do site.  
- As pastas **__pycache__** fazem o programa ser mais rápido.  
- A pasta **.venv** facilita a criação de uma instalação Python, principalmente quando precisamos de aplicações de versões diferentes  
  (análogo a aplicativos que podem ser usados por celulares novos e muito antigos!).  
- O arquivo **.env** possui a chave secreta usada pelo `config.py`.  
  Arquivos `.env` não devem ser vistos por ninguém que não tenha acesso ao computador em que ele está [de fato, não está neste repositório!].
- O arquivo **.gitignore** possui nomes de arquivos que não serão enviados à Internet  
  quando o código do site estiver disponível, como as pastas `pycache`, o `.env` e o `.venv`.
- O arquivo **requirements.txt** possui as aplicações necessárias para rodar o site.  
  Antes de usá-lo, uma pessoa deve rodar um comando que instala tudo que estiver nessa pasta.
- O arquivo **README.md** ("leia-me" em inglês) possui instruções e informações gerais sobre o site e o código.

Última atualização deste README: 27/11/2024.
