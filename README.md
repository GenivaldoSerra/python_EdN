# Escola da Nuvem - Python
Repositorio criado para resolver as atividades de Python da Escola da Nuvem.

---

# 🐍 Repositório de Exercícios de Python

Este repositório contém uma coleção de exercícios práticos em Python, organizados para facilitar o aprendizado e a prática da linguagem. Além disso, fornecemos instruções detalhadas para configurar o ambiente de desenvolvimento utilizando Git e Pyenv.
E para rodar os execíciros que utilizam `Streamlit`, execute o comando abaixo:

```bash
streamlit run pasta/arquivo.py
```

## 📁 Estrutura do Repositório

Cada diretório contém:
- Arquivos `.py` com os exercícios
- Instruções específicas (`README.md`) se necessário
- Recursos adicionais conforme aplicável

## 🛠️ Configuração do Ambiente

Para ajudar ainda mais na instalação e configuração do ambiente recomendo esses dois videos da Jornada de Dados:

Video 1:
```bash
https://www.youtube.com/watch?v=-M4pMd2yQOM&t=1657s
```
Video 2:
```bash
https://www.youtube.com/watch?v=9LYqtLuD7z4&t=683s
```

### 1. Instalando o Git no Ubuntu

Para instalar o Git em sistemas baseados no Ubuntu:

```bash
sudo apt update
sudo apt install git
````

Após a instalação, configure seu nome de usuário e e-mail:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```

Verifique a instalação:

```bash
git --version
```

### 2. Instalando o Pyenv no Ubuntu

O Pyenv permite gerenciar múltiplas versões do Python. Siga os passos abaixo para instalá-lo:

#### a. Atualize os pacotes do sistema:

```bash
sudo apt update
```

#### b. Instale as dependências necessárias:

```bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
libffi-dev liblzma-dev
```

#### c. Instale o Pyenv:

```bash
curl https://pyenv.run | bash
```

#### d. Configure as variáveis de ambiente:

Adicione as seguintes linhas ao final do arquivo `~/.bashrc` (ou `~/.zshrc` se estiver usando Zsh):

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Aplique as mudanças:

```bash
exec "$SHELL"
```

#### e. Verifique a instalação:

```bash
pyenv --version
```

### 3. Instalando uma Versão Específica do Python com Pyenv

Liste as versões disponíveis:

```bash
pyenv install --list
```

Instale a versão desejada (exemplo: 3.10.4):

```bash
pyenv install 3.10.4
```

Defina a versão instalada como padrão:

```bash
pyenv global 3.10.4
```

Verifique a versão ativa do Python:

```bash
python --version
```

## 🚀 Como Usar Este Repositório

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/exercicios-python.git
cd exercicios-python
```

2. Navegue até o diretório do exercício desejado:

```bash
cd 01-introducao
```

3. Execute o script Python:

```bash
python nome_do_exercicio.py
```

## 📚 Referências

* [Documentação Oficial do Python](https://docs.python.org/pt-br/3/)
* [Documentação do Git](https://git-scm.com/doc)
* [Repositório do Pyenv no GitHub](https://github.com/pyenv/pyenv)


