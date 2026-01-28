# Surfarte

Surfarte é um site voltado para aulas de surf, desenvolvido com Django, que permite a interação entre usuários por meio de avaliações, além do gerenciamento de professores e planos de aulas.

O sistema trabalha com autenticação, perfis de usuário e controle de permissões, simulando um cenário real de aplicação web.

---

## Sobre o Projeto

Surfarte é uma aplicação web desenvolvida com Django para o gerenciamento de aulas de surf. O sistema permite que usuários se cadastrem, façam login e publiquem avaliações sobre as aulas, além de consultar informações sobre professores e planos disponíveis.

A aplicação possui controle de acesso baseado em permissões, garantindo que cada usuário interaja com o sistema de acordo com seu nível de autorização.

---

## Objetivo do Projeto

Este projeto possui caráter educacional e foi desenvolvido com o objetivo de aplicar, na prática, conceitos fundamentais de desenvolvimento web, como autenticação de usuários, controle de permissões, operações de CRUD e integração entre front-end e back-end utilizando Django, HTML, CSS e Bootstrap.

## Funcionalidades

### Usuário Comum
Após realizar cadastro e login, o usuário pode:

- Publicar avaliações sobre as aulas de surf  
- Visualizar avaliações de outros usuários  
- Visualizar apenas suas próprias avaliações  
- Adicionar e atualizar informações do perfil (nome completo, telefone, etc.)  
- Visualizar tabelas de professores  
- Visualizar tabelas de planos de aulas  

---

### Administrador
Usuários pertencentes ao grupo Administrador possuem permissões adicionais, podendo:

- Editar e excluir dados das tabelas:
  - Avaliação
  - Professor
  - Plano
- Cadastrar novos professores no sistema  
- Cadastrar novos planos de aulas  
- Gerenciar informações gerais da aplicação  

---

## Tipos de Usuário

O sistema trabalha com dois níveis principais de usuários:

- Usuário comum — acesso às funcionalidades de avaliação, perfil e visualização de dados.  
- Administrador — acesso ampliado para gerenciamento completo das informações do sistema.

As permissões são controladas utilizando os recursos nativos de autenticação e autorização do Django.

---

## Tecnologias Utilizadas

- HTML  
- CSS  
- Bootstrap  
- Python  
- Django  
- SQLite    

---

