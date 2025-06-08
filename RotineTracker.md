
# Documentação do Projeto: **Rotine Tracker**

## 1. Visão Geral

### Tecnologias Utilizadas
- **Linguagem:** Python  
- **Framework:** FastAPI  
- **Servidor ASGI:** Uvicorn  

### Descrição  
**Rotine Tracker** é um sistema gamificado de acompanhamento de hábitos desenvolvido para incentivar a criação e a manutenção de rotinas saudáveis e produtivas. Os usuários podem registrar atividades diárias — como exercícios físicos, sessões de estudo ou leitura — e acumular pontos com base nessas ações. A pontuação contribui para o nível do usuário na plataforma, promovendo motivação e progresso contínuo.

### Objetivo  
O principal objetivo do Rotine Tracker é **estimular o desenvolvimento de bons hábitos por meio da gamificação**, transformando tarefas cotidianas em metas e recompensas. Além disso, o sistema permite a **criação de desafios entre amigos**, com regras de pontuação personalizadas e rankings, fomentando a interação social e a competição saudável.

---

## 2. Descrição Detalhada do Projeto

### O que é o projeto?  
Rotine Tracker é uma aplicação web que combina ferramentas de organização pessoal com mecânicas de jogos (gamificação). Por meio do registro de atividades e da criação de desafios, o sistema incentiva usuários a manterem hábitos consistentes, oferecendo **feedback visual e recompensas simbólicas** (como pontos, níveis e rankings) com base em seu desempenho.

---

### 2.1 Funcionalidades Principais

#### 1. Registro de Atividades  
Usuários podem cadastrar atividades realizadas, como:
- Estudo
- Exercício físico
- Leitura, entre outros

**Campos obrigatórios:**
- Tipo da atividade  
- Duração  
- Data e hora  

**Campo opcional:**
- Descrição

Ao salvar a atividade, o sistema:
- Calcula a pontuação com base nos dados fornecidos
- Atualiza o nível do usuário
- Exibe uma mensagem de sucesso

---

#### 2. Edição e Exclusão de Atividades  
- É possível **editar** qualquer atividade previamente registrada. O sistema recalcula a pontuação com base nos novos dados.
- Também é possível **excluir** uma atividade. Nesse caso, a pontuação será **subtraída** do total acumulado.

---

#### 3. Desafios Personalizados entre Amigos  
Os usuários podem criar desafios personalizados com as seguintes configurações:
- Nome do desafio  
- Tipos de atividades válidas  
- Regras de pontuação  
- Data de início e término  

Amigos podem participar via **código ou convite direto**. Durante o período do desafio, os participantes competem por uma colocação no **ranking**, que reflete o engajamento individual de cada um.

---

#### 4. Visualização de Ranking  
Cada desafio possui um **ranking em tempo real**, onde os participantes são ordenados conforme a pontuação acumulada. Essa funcionalidade reforça a motivação e o senso de progresso coletivo.

---

#### 5. Autenticação de Usuários  
O sistema inclui um módulo de autenticação com:
- Cadastro (nome, e-mail e senha)
- Login
- Logout

As credenciais são verificadas de forma segura, garantindo uma experiência personalizada para cada usuário.

---

### 2.2 Estrutura do Projeto

```
RotineTracker/
│
├── main.py         # Inicialização da aplicação
├── api.py          # Lógica de rotas e controladores
├── models.py       # Modelos de dados com Pydantic
```

---

## 3. Etapas de Entrega

### Etapa 1: Documento de Requisitos  
- Definição dos Requisitos Funcionais e Não Funcionais  
- Levantamento de funcionalidades essenciais

### Etapa 2: Diagrama de Casos de Uso  
- Identificação de atores  
- Mapeamento das interações do usuário com o sistema  

### Etapa 3: Modelo Lógico do Banco de Dados  
- Definição das entidades e relacionamentos  
- Normalização das tabelas  
- Planejamento do armazenamento das atividades, usuários e desafios

### Etapa 4: Construção da Lógica da API
- Definição e criação das rotas da API (endpoints) para cada funcionalidade:
  - Cadastro, edição e exclusão de atividades
  - Criação e participação em desafios
  - Visualização de ranking
  - Autenticação de usuários (login, logout e registro)
- Integração com os modelos de dados (Pydantic) para validação e consistência das informações recebidas e enviadas.
- Tratamento de erros e mensagens de resposta para garantir uma experiência segura e informativa ao usuário.
- Organização do código em módulos (`main.py`, `api.py`, `models.py`) para manter a arquitetura limpa, escalável e de fácil manutenção.

Essa etapa é fundamental para garantir que todas as operações da aplicação funcionem corretamente e que os dados sejam manipulados de forma segura e eficiente.