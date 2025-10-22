# Trabalho final: Automação de Testes com Appium para o App ""
# ALESSANDRO BARBOSA DE OLIVEIRA
Este projeto documenta o processo de automação de testes para a funcionalidade "Transactions" do aplicativo móvel **Budget Watch**, utilizando Appium com Python. O objetivo foi criar e executar um conjunto de testes estruturados para validar os requisitos funcionais e de negócio definidos, além de gerar evidências dos resultados.

--------------------------------------------

## 📂 Estrutura do Projeto

A organização dos arquivos e diretórios do projeto segue a estrutura abaixo: (projeto github)

|-trabalho_final_automacao_testes/
|  |--app_moneytracker/
|  |  |--enunciado/
|  |  |  |--Trabalho Final.docx.pdf  (Documento de requisitos)
|  |  |--pages/
|  |  |  |--accountPage.py
|  |  |  |--addAccountCase.py
|  |  |  |--addIncomePage.py
|  |  |  |--basePage.py
|  |  |  |--mainPage.py
|  |  |  |--shortSummaryPage.py
|  |  |--relatorios/
|  |  |  |--Relatory - Test Case Specification and Report.xlsx (Planilha de casos de teste)
|  |  |--test_evidences/
|  |  |  |--screnshots/
|  |  |  |  |-- arquivos de evidencias.png
|  |  |  |--Alessandro_video_teste_case.mp4 (Vídeo de demonstração)
|  |  |--testCase/
|  |  |  |--accountTestCase.py
|  |  |  |--baseTestCase.py
|  |  |  |--incomeTestCase.py
|  |  |  |--mainPageTestCase.py
|  |  |  |--shortSummaryTestCase.py
|  |  |--Data.py
|  |  |--__init__.py
|  |  |--app_moneytracker.apk
|  |--.gitignore
|  |--README.md

---------------------------------------------------------------------------------

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

---------------------------------------------------------------------------

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

-------------------------------------------------------------------------------

## 🎥 Demonstração em Vídeo

Uma gravação da execução completa dos testes, incluindo a narração de cada etapa e a demonstração dos bugs encontrados, está disponível no diretório:
`/video/Alessandro_trabalhofinal_video_teste_case.mp4`

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
