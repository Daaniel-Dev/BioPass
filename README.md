BioPass - Seu Marketplace de Produtos Sustentáveis
Descrição
O BioPass é um sistema de marketplace desenvolvido em Python, que opera via console. Ele foi projetado para ser uma plataforma onde os usuários podem comprar e vender produtos com um foco em sustentabilidade. O sistema inclui funcionalidades completas de gerenciamento de usuários e produtos, um processo de compra simulado e seções interativas para depoimentos e compartilhamento de conteúdo educacional, promovendo uma comunidade engajada com práticas sustentáveis.

Funcionalidades
O sistema oferece um conjunto robusto de funcionalidades para os usuários:

Gerenciamento de Usuários
Cadastro: Permite que novos usuários criem uma conta com nome, CPF e senha. O sistema inclui uma validação para o formato do CPF.

Login: Usuários já cadastrados podem acessar a plataforma de forma segura.

Alteração de Cadastro: Usuários podem atualizar suas informações pessoais, como nome, senha e até mesmo o CPF.

Exclusão de Conta: Oferece a opção para que um usuário exclua sua conta e todos os dados associados a ela de forma permanente.

Gerenciamento de Produtos
Cadastro de Produtos: Vendedores podem adicionar produtos à venda, especificando nome, descrição, preço, quantidade em estoque e, opcionalmente, um link de vídeo.

Listagem de Produtos: Todos os usuários podem ver os produtos disponíveis. Vendedores têm uma visão filtrada para gerenciar apenas os seus próprios itens.

Alteração de Produtos: Vendedores podem editar os detalhes de seus produtos já cadastrados.

Exclusão de Produtos: Permite que vendedores removam seus produtos da plataforma.

Processo de Compra
Comprar Produto: Usuários podem navegar pela lista de produtos e realizar uma compra. O sistema impede que um vendedor compre seus próprios produtos.

Simulação de Pagamento: O processo de compra inclui uma etapa de pagamento fictício com cartão de crédito para simular uma transação real.

Controle de Estoque: A quantidade de um produto é automaticamente abatida do estoque após uma compra ser finalizada.

Comunidade e Educação
Depoimentos: Uma seção onde os usuários podem deixar seus comentários e feedback sobre a plataforma, além de ver os depoimentos de outros.

Vídeos Educacionais: Um espaço para compartilhar e visualizar links de vídeos sobre sustentabilidade e práticas ecológicas.

Como Executar o Projeto
Para colocar o BioPass em funcionamento, siga os passos abaixo.

Pré-requisitos:

Ter o Python 3 instalado em sua máquina.

(Opcional para Windows) Habilitar Suporte a Cores no Terminal:
O aplicativo utiliza cores para melhorar a legibilidade e a experiência do usuário. Se você estiver usando o Windows e as cores não forem exibidas corretamente no Prompt de Comando, pode ser necessário habilitar o suporte a terminais virtuais. Para fazer isso, abra o Prompt de Comando (cmd) e execute o seguinte comando uma única vez:

reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1

Estrutura de Arquivos:

Certifique-se de que todos os arquivos (main.py, functions.py, classes.py) estão no mesmo diretório.

Crie uma pasta chamada database neste mesmo diretório. É nesta pasta que o sistema irá criar e armazenar os arquivos de dados (.json).

/seu-projeto
|-- database/
|-- classes.py
|-- functions.py
`-- main.py

Execução:

Abra um terminal ou prompt de comando.

Navegue até o diretório onde os arquivos do projeto estão localizados.

Execute o comando a seguir para iniciar a aplicação:

python main.py

Interação:

Após a execução, o menu principal do BioPass será exibido no console. Siga as instruções na tela para navegar pelas diferentes opções.

Estrutura do Código
O projeto está organizado em três arquivos principais:

main.py: É o ponto de entrada da aplicação. Ele é responsável por apresentar o menu principal e controlar o fluxo de navegação do usuário, orquestrando as chamadas para as outras funções do sistema.

functions.py: Este arquivo é o cérebro do sistema. Ele contém toda a lógica para as funcionalidades, incluindo cadastro, login, manipulação de produtos, o processo de compra e as funções de interação com a comunidade. Também gerencia a leitura e escrita dos arquivos JSON que funcionam como banco de dados.

classes.py: Define as estruturas de dados fundamentais do projeto. Contém as classes User e Produto, que modelam os usuários e os produtos, respectivamente, garantindo uma organização de dados clara e coesa.
