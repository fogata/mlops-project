# Projeto MLOps - Pipeline Completo para Machine Learning

## 📌 Finalidade do Projeto

Este projeto tem como objetivo demonstrar um fluxo moderno e profissional de MLOps (Machine Learning Operations), integrando boas práticas de engenharia de software, versionamento de dados, reprodutibilidade e automação de deploy para modelos de machine learning.

O foco é permitir que desenvolvedores e cientistas de dados implementem uma pipeline robusta que envolva:

* Treinamento automatizado de modelos
* Versionamento de dados e modelos com DVC
* Serviço de inferência via API REST com FastAPI
* Containerização com Docker e orquestração via docker compose
* Base para futura automação com CI/CD, MLflow e monitoramento

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI** – Serviço de inferência HTTP
* **scikit-learn** – Treinamento e validação de modelos
* **DVC** – Versionamento de dados e definição de pipelines reprodutíveis
* **Docker** – Empacotamento do ambiente
* **Docker Compose** – Orquestração local dos containers
* **MLflow (futuro)** – Rastreamento de experimentos
* **Evidently (futuro)** – Monitoramento de modelos em produção

---

## 🚀 Funcionalidades

* [x] API REST com endpoint `/predict`
* [x] Pipeline automatizada com DVC para reproduzir o treino
* [x] Dockerfile para empacotamento da aplicação
* [x] docker-compose para execução local
* [x] Ambiente virtual configurado com requirements.txt
* [ ] CI/CD com GitHub Actions (em progresso)
* [ ] Integração com armazenamento remoto (S3, GDrive, etc.)

---

## 📂 Estrutura de Pastas

```text
mlops-project/
├── data/               # Dados versionados via DVC
├── notebooks/          # Prototipagem exploratória
├── src/
│   ├── training/       # Scripts de treino
│   ├── serving/        # FastAPI e carregamento de modelo
│   └── utils/          # Funções auxiliares
├── models/             # Modelos serializados
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── dvc.yaml
├── .gitignore
└── README.md
```

---

## 👨‍💻 Como usar

1. Clone este repositório:

```bash
git clone https://github.com/SEU_USUARIO/mlops-project.git
cd mlops-project
```

2. Crie e ative o ambiente virtual (Windows):

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicialize o DVC:

```bash
dvc init
dvc repro
```

5. Rode o servidor da API:

```bash
uvicorn src.serving.main:app --reload
```

Acesse em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📝 Licença

Este repositório é disponibilizado sob a licença **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

**Você pode:**

* Compartilhar e adaptar o conteúdo para fins não comerciais

**Você deve:**

* Dar crédito apropriado ao autor (Felipe Ogata)
* Não utilizar para fins comerciais

Detalhes completos: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

---

## ✉️ Contato

Felipe Ogata
📧 [felipeogata@gmail.com](mailto:felipeogata@gmail.com)
