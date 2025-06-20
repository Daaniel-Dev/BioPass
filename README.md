# BioPass - Marketplace de Produtos Sustentáveis

**BioPass** é um sistema em Python que conecta consumidores e vendedores de produtos sustentáveis em um ambiente interativo via terminal. A aplicação permite a comercialização de produtos eco-friendly, promovendo o consumo consciente e incentivando a responsabilidade ambiental.

---

## Problema Abordado

Consumidores preocupados com o meio ambiente frequentemente enfrentam dificuldades para encontrar produtos sustentáveis e fornecedores confiáveis. Ao mesmo tempo, pequenos produtores sustentáveis têm pouco alcance digital. O BioPass resolve esse problema ao conectar esses dois públicos de forma prática e acessível.

---

## Como Funciona

### Para todos os usuários
- Cadastro e login por **CPF** e senha
- Alteração e exclusão de conta
- Visualização de produtos disponíveis
- Compra de produtos com verificação de estoque
- Acesso a vídeos educativos
- Envio e leitura de depoimentos

### Para vendedores
- Cadastro de produtos com nome, preço, quantidade, descrição e link de vídeo
- Gerenciamento de produtos (edição e exclusão)

Os dados são armazenados em arquivos JSON, simulando persistência em um sistema de banco de dados simples.

---

## Conceitos Aplicados

- **Modularização:** Separação clara entre `main.py`, `functions.py` e `classes.py`
- **Programação orientada a objetos:** Classes `User` e `Produto` com encapsulamento de atributos
- **Manipulação de arquivos:** Leitura e escrita de dados em arquivos `.json` simulando um banco de dados
- **Validações:** Verificação de CPF com cálculo de dígitos verificadores e autenticação
- **Listas e dicionários:** Gerenciamento de produtos, usuários e depoimentos com estruturas de dados apropriadas
- **Controle de fluxo:** Menus interativos, tratamento de exceções, laços e condições bem aplicadas

---

## Execução

1. Faça o download do projeto e extraia para uma pasta local.
2. Certifique-se de ter o **Python 3.13** ou superior instalado.

No terminal (**Windows**):

```bash
cd caminho\para\pasta\BioPass
```

*(Opcional) Ative o suporte a cores no terminal:*
```cmd
reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1
```

Execute o programa:
```cmd
python main.py
```

---

## Estrutura de Arquivos

```
BioPass/
│
├── main.py                 # Ponto de entrada da aplicação
├── functions.py            # Lógica principal de cadastro, login, menus, produtos, vídeos, depoimentos
├── classes.py              # Definição das classes User e Produto
├── database/               # Pasta onde os arquivos JSON são salvos
│   ├── dados.json
│   ├── produtos.json
│   ├── depoimentos.json
│   └── video_educacional.json
```

---

## Team

- Daniel Gonçalves
- Arthur Alexandre
- Ludmilla Arlane
- Wesley Telles
- Júlio Augusto
- Marcelo Bezerra

