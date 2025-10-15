# Trabalho final: Automação de Testes com Appium para o App ""

Este projeto documenta o processo de automação de testes para a funcionalidade "Transactions" do aplicativo móvel **Budget Watch**, utilizando Appium com Python. O objetivo foi criar e executar um conjunto de testes estruturados para validar os requisitos funcionais e de negócio definidos, além de gerar evidências dos resultados.

---

## 📂 Estrutura do Projeto

A organização dos arquivos e diretórios do projeto segue a estrutura abaixo:

|-trabalho1_automacao_testes/
|  |--budget_app/
|  |  |--enunciado/
|  |  |  |--Trabalho_TestesEstruturados.pdf  (Documento de requisitos)
|  |  |--test_case/
|  |  |  |--Relatory - Test Case Specification and Report.xlsx (Planilha de casos de teste)
|  |  |--test_evidences/
|  |  |  |--test_evidences_transactions/
|  |  |  |  |-- (Screenshots de evidências dos testes)
|  |  |--video/
|  |  |  |--Alessandro_video_teste_case.mp4 (Vídeo de demonstração)
|  |  |--budget_test.py
|  |  |--Data.py
|  |  |--transactions_test.py
|  |--.gitignore
|  |--README.md

---

## 💻 Ambiente de Testes

Os testes foram executados utilizando a seguinte configuração de hardware:

* **Dispositivo de Teste:** Smartphone Multilaser F Pro 2
    * **Sistema Operacional:** Android 11
    * **Memória RAM:** 1 GB
* **Máquina de Execução:** Notebook
    * **Sistema Operacional:** Windows 11
    * **Processador:** Intel Core i3 1.2 GHz (12ª geração)
    * **Memória RAM:** 12 GB DDR4-3200MHz
    * **Armazenamento:** SSD de 256 GB

---

## 🛠️ Ferramentas e Tecnologias

A automação foi desenvolvida com o auxílio das seguintes ferramentas e versões:

* **Servidor Appium:** Appium-Desktop `v1.22.3-4`
* **Inspeção de Elementos:** Appium Inspector `v2025.8.1`
* **Espelhamento de Tela:** Scrcpy
* **Linguagem de Programação:** Python `v3.12.4`
* **Framework de Teste:** Unittest (integrado ao Python)
* **IDE de Desenvolvimento:** PyCharm Community `v2024.2.3`
* **Gerenciador de Ambiente:** Anaconda3 `v2024.10.1`
* **Dependências:**
    * Node.js `v18.12.0`
    * NPM `v8.19.2`
    * Java JDK `v8.0.392.8`
* **SDK Android:** Android Studio `v2023.3`

---

## ✅ Cobertura de Requisitos e Resultados

Todos os requisitos da funcionalidade "Transactions" foram cobertos pelos testes automatizados. A execução revelou tanto funcionalidades operantes quanto inconsistências (bugs) no comportamento do aplicativo.

| Req. | Descrição | Status do Teste | Observações                                                                        |
|:----:|:-----------|:---------------:|:-----------------------------------------------------------------------------------|
| **1** | Não permitir registro duplicado. |  🔴 **FALHOU**  | **Bug Encontrado:** O aplicativo permite salvar transações com dados idênticos.    |
| **2** | Campos `name` e `value` não podem ser vazios. |  ✅ **PASSOU**   | A mensagem de erro "Value is empty" é exibida corretamente.                        |
| **3** | O campo `value` pode ser 0. |  ✅ **PASSOU**   | A transação é salva com sucesso com o valor 0.                                     |
| **4** | Limite de 30 caracteres para o campo `name`. |  🔴 **FALHOU**  | **Bug Encontrado:** O aplicativo permite salvar nomes com mais de 30 caracteres.   |
| **5** | Limite de 20 caracteres para o campo `value`. |  🔴 **FALHOU**  | **Bug Encontrado:** O aplicativo permite salvar valores com mais de 20 caracteres. |
| **6** | Permitir datas no passado, presente e futuro. |  ✅ **PASSOU**  | O app permite adicionar as datas selecionadas                                      |
| **7** | Campo `Receipt` é opcional e abre a câmera. |  ✅ **PASSOU**   | O fluxo de salvar sem anexo funciona, e o botão abre um app do sistema.            |
| **8** | Permitir edição (exceto do nome). |  🔴 **FALHOU**  | **Bug Encontrado:** O aplicativo permite incorretamente a alteração do nome.       |
| **9** | Permitir a remoção de um registro. |  ✅ **PASSOU**   | A transação é removida com sucesso da lista.                                       |

---

## 🎥 Demonstração em Vídeo

Uma gravação da execução completa dos testes, incluindo a narração de cada etapa e a demonstração dos bugs encontrados, está disponível no diretório:
`budget_app/video/Alessandro_video_teste_case.mp4`

** FERRAMENTAS UTILIZADAS **
1. Appium-Desktop: versão 1.22.3-4 (para rodar o servidor Appium);
2. Appium Inspector: versão 2025.8.1 (para fazer o mapeamento dos itens utilizando o Smartphone físico);
3. Scrcpy (Faz o espelhamento do celular na tela do PC/Notebook para acompanhamento dos testes);
4. Versão do nodejs: 18.12.0;
5. Versão do npm: 8.19.2
6. Versão do java: 8.0.392.8 adoptium;
7. Versão do python: 3.12.4;
8. Anaconda3 2024.10.1 (para criação do ambiente virtual e configurar o projeto)
9. Pycharm Community: versão 2024.2.3 (para trabalhar no projeto Python);
10. Android Studio: versão 2023.3 (configurar alguns plugins para rodar o projeto e o emulador, se necessário);

#######################################################################################################
