<h1>
  Synplus
</h1>

Synplus é um programa de Interface de Linhas de Comando (CLI) interno da Simplifica+ . É projetado para tornar possível a visualização dos dados armazenados em arquivos `.txt`   pelo website que o projeto vem desenvolvendo. 

O Syplus oferece praticidade e não impõe quaisquer biblioteca de terceiros como dependência. 



---



## 🧩 Como usar

Para copiar o projeto, use os comandos:

```bash
  # Clone o repositório
  ❯ git clone https://github.com/matheusdesjardins/Simplifica-mais.git

  # Entrar no diretório do projeto
  ❯ cd Simplifica-mais
  
  # Entrar no diretório do Synplus
  ❯ cd Synplus
```

Para iniciar o projeto, você utiliza o Python:

```bash
  # Ubuntu 20.04
  ❯ python3 main.py
```

```powershell
  # Windows 10
  ❯ python main.py
```



## 🧪 Um simples exemplo

```bash 
❯ python3 main.py

   Copyright (c), Simplifica+ 2021
   Email comments or suggestions to <contato@simplifica.mais>

   Synplus v0.01.pre (built-with python)
   Programa interno desenvolvido pelos membros de computação da Simplifica+


?. Login: admin
?. Senha: admin
```

```bash 
# Outra conta registrada
?. Login: data
?. Senha: view
```

```bash 
# Ainda outra conta registrada
?. Login: simplifica
?. Senha: mais
```



<h2 align="center">
  Documentação 📖
</h2>

<p align="center">
  <span>Componentes</span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <span>Detalhamento</span>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <span>Mudanças</span>
</p>


---



### 🧱 Componentes

`ID: 001` 

---

```python
registered_accounts = {
    "Accounts": [
        ('admin', 'admin'), 
        ('data', 'view'),
        ('simplifica', 'mais')
    ]
}
```

_registered_accounts_ é um dicionário (estrutura de dados) do tipo coleção.  _registered_accounts_ contém apenas um par de chave/valor, sendo eles a chave _"Accounts"_ e seu valor uma lista de tuplas. Essa tuplas seguem o seguinte template: `(user, password)`, onde _user_ e _password_ são do tipo str (string).

`ID: 002` 

---

```python
authenticator = None
```

_authenticator_ é uma variável que receberá valores esperados do tipo number. São os valores: `0, 1, 2, 3` onde, 0 representa uma conta não registrada, 1 a conta de maior privilégios , 2 a conta para visualizar os dados e 3 conta para testes de fluxo lógico dos algoritmos que serão inseridos aos formulários no website.

### ⚙️ Detalhamento

`ID: 001` 

---

```
'[1] Registrar usuário para ambulatório LGTBQIA+.'
```

_Em breve..._

`ID: 002` 

```
'[2] Registrar busca por atendimento imediato.'
```

_Em breve..._

`ID: 003` 

---

```
 '[3] Registrar metadados do Website.'
```

_Em breve..._

`ID: 004` 

---

```
'[1] Visualizar dados de acesso ao site.'
```



`ID: 005` 

---

``` 
'[2] Visualizar dados por ambulatórios LGTBQIA+.'
```

_Em breve..._

`ID: 006` 

---

```
'[3] Visualizar dados da busca por atendimento imediato.'
```

_Em breve..._

### ⛓️ Mudanças



---



<p align="center">by Simplifica+</p>

