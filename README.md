# Ecora - Seu Marketplace Sustentável

Bem-vindo ao **Ecora**, um aplicativo de marketplace focado na sustentabilidade, ajudando vendedores e consumidores a se conectarem de forma consciente.

---

## 📖 Sobre o Projeto

O objetivo do **Ecora** é proporcionar um ambiente seguro e simples onde pequenos e grandes vendedores possam divulgar e vender seus produtos de forma sustentável. Oferece funcionalidades para:

- Cadastrar produtos sustentáveis.
- Comprar produtos disponibilizados na plataforma.
- Adicionar vídeos educativos sobre reutilização ou descarte consciente.
- Deixar depoimentos e compartilhar experiências.
- Aprender mais sobre sustentabilidade com nossa seção de vídeos educacionais.

---

## 🚀 Funcionalidades

### 👤 **Usuários**
- **Cadastro de Usuários**: Realizado usando CPF, nome e senha. A validação do CPF é feita para garantir autenticidade.
- **Login**: Acesso seguro com CPF e senha.

### 🛍️ **Produtos**
- **Cadastro de Produtos**: 
  - Nome
  - Descrição
  - Preço
  - Quantidade disponível
  - Link de vídeo (opcional)
- **Listagem de Produtos Disponíveis**: Consulte produtos cadastrados na plataforma.
- **Compra de Produtos**: Sistema simples para adquirir produtos, simulando uma transação com cartão.

### ✨ **Recursos Extras**
- **Depoimentos**: Adicione feedback e veja o que outros usuários pensam sobre a plataforma.
- **Vídeos Educacionais**:
  - Adicione links de vídeos para promover práticas sustentáveis.
  - Consulte os links adicionados.

---

## 💻 Tecnologias Utilizadas

- **Python**: Lógica principal do programa.
- **JSON**: Armazenamento de dados de usuários, produtos, depoimentos, e vídeos de forma persistente.

---

## 📋 Pré-requisitos

Antes de executar o programa, garanta que você tenha:
- **Python 3.13** ou superior instalado.
- Biblioteca Python padrão de entrada/saída (como `json`).

---

## ▶️ Como Executar

1. Clone ou baixe o repositório para sua máquina.
2. Certifique-se de ter os arquivos `main.py`, `functions.py` e `classes.py` no mesmo diretório.
3. Execute o aplicativo a partir do arquivo `main.py`:

```shell script
python main.py
```


4. Siga as instruções interativas no terminal para explorar o sistema.

---

## 🗂 Estrutura

- **main.py**: Arquivo principal que inicia o programa e conecta as funcionalidades.
- **functions.py**: Contém as principais funções do programa, como menus, cadastro, manipulação de arquivos e lógica de funcionamento.
- **classes.py**: Define as classes `User` (usuário) e `Produto` (produto), que estruturam os dados no sistema.
- **Arquivos JSON**:
  - `dados.json`: Armazena dados de usuários cadastrados.
  - `produtos.json`: Contém informações dos produtos cadastrados.
  - `depoimentos.json`: Registra depoimentos dos usuários.
  - `video_educacional.json`: Lista de links de vídeos educacionais.

---

## 🔒 Segurança

- Validação de dados como CPF e senha.
- Simulação de transações seguras.
- Armazenamento de dados estruturados em arquivos JSON, permitindo integração e persistência.

---

## 🎯 Melhorias Futuras
- Implementar uma interface gráfica para maior acessibilidade.
- Adicionar uma API para acessar os produtos e usuários remotamente.
- Melhorar a encriptação dos dados dos usuários para maior segurança.

---

## 🙌 Contribuição

Gostou do projeto? Sinta-se à vontade para sugerir melhorias ou reportar problemas.

---

## 📞 Contato

Para dúvidas ou sugestões, entre em contato com os desenvolvedores. Estamos abertos a feedbacks para melhorar a experiência sustentável de nossos usuários.

---

**Obrigado por utilizar o Ecora! Vamos juntos construir um futuro mais sustentável. 🌱**
