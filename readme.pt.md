# Projeto MLOps - Pipeline Completo para Machine Learning

[![CI](https://github.com/fogata/mlops-project/actions/workflows/ci.yml/badge.svg)](https://github.com/fogata/mlops-project/actions/workflows/ci.yml)

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
* **Render** – Plataforma de deploy contínuo na nuvem
* **MLflow (futuro)** – Rastreamento de experimentos
* **Evidently (futuro)** – Monitoramento de modelos em produção
* **MLflow (futuro)** – Rastreamento de experimentos
* **Evidently (futuro)** – Monitoramento de modelos em produção

---

## 🚀 Funcionalidades

* [x] API REST com endpoint `/predict`
* [x] Pipeline automatizada com DVC para reproduzir o treino
* [x] Dockerfile para empacotamento da aplicação
* [x] Ambiente virtual configurado com requirements.txt
* [x] CI/CD com GitHub Actions
* [ ] Integração com armazenamento remoto (S3, GDrive, etc.)

---

## 📂 Estrutura de Pastas

```text
mlops-project/
├── .github
|   ├── actions         
|   └── workflow        # ci/cd
├── data/               # Dados versionados via DVC
├── notebooks/          # Prototipagem exploratória
├── src/
│   ├── training/       # Scripts de treino
│   ├── serving/        # FastAPI e carregamento de modelo
│   └── utils/          # Funções auxiliares
├── models/             # Modelos serializados
├── Dockerfile
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

## 🌳 Estrutura de Branches

Este projeto utiliza uma estratégia de versionamento baseada em Git com múltiplas branches:

| Branch                   | Finalidade                                        |
| ------------------------ | ------------------------------------------------- |
| `main`                   | Código estável e pronto para produção             |
| `dev`                    | Desenvolvimento contínuo (integração de features) |
| `feature/train-pipeline` | Desenvolvimento da pipeline de treino             |
| `feature/api`            | Desenvolvimento da API FastAPI                    |
| `feature/monitoring`     | Integração de monitoramento e métricas            |
| `feature/mlflow`         | Integração com MLflow                             |

### Comandos para criação das branches

```bash
# Criar e subir branch de desenvolvimento
git checkout -b dev
git push -u origin dev

# Criar branches de feature a partir de 'dev'
git checkout -b feature/train-pipeline
git push -u origin feature/train-pipeline

git checkout -b feature/api
git push -u origin feature/api

git checkout -b feature/monitoring
git push -u origin feature/monitoring

git checkout -b feature/mlflow
git push -u origin feature/mlflow
```

---


---

## 🌐 Acesso à API via Render

A aplicação está deployada na nuvem via Render. Para acessá-la:

- Documentação interativa (Swagger):  
  👉 `https://mlops-api.onrender.com/docs`

- Endpoint de inferência:  
  `POST https://mlops-api.onrender.com/predict`

### Exemplo de chamada:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

A resposta será:

```json
{
  "prediction": [0]
}
```

> O modelo será treinado automaticamente no primeiro deploy, caso ainda não exista.


## 📝 Licença

Este repositório é disponibilizado sob a licença **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

**Você pode:**

* Compartilhar e adaptar o conteúdo para fins não comerciais

**Você deve:**

* Dar crédito apropriado ao autor (Felipe Ogata)
* Não utilizar para fins comerciais

Detalhes completos: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

[![License: CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/)

---

## ✉️ Contato

Felipe Ogata
📧 [felipeogata@gmail.com](mailto:felipeogata@gmail.com)
