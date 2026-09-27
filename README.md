# 🌡️ Pipeline de Dados IoT com Docker, PostgreSQL e Streamlit

Este projeto consiste em um pipeline de dados completo para processar, armazenar e visualizar dados de sensores de temperatura IoT. O projeto foi desenvolvido como entregável da disciplina Disruptive Architectures: IoT, Big Data e IA da UniFECAF.

---

## 🛠️ Tecnologias Utilizadas

* Python 3.12 (Pandas, SQLAlchemy, Psycopg2, Streamlit, Plotly)
* Docker & PostgreSQL
* Git & GitHub
* Dataset: Temperature Readings - IoT Devices (Kaggle)

---

## 📂 Estrutura do Projeto

iot-temperature-pipeline/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── IOT-temp.csv
│
├── docs/
│   └── dashboard_screenshot.png
│
├── sql/
│   └── views.sql
│
└── src/
    ├── pipeline.py
    ├── create_views.py
    └── dashboard.py

---

## ⚙️ Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter instalado em sua máquina:
* Python 3.9+
* Docker Desktop
* Git

### 2. Clonar o Repositório
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO

### 3. Subir o Banco de Dados PostgreSQL (Docker)
Execute o comando para iniciar o contêiner do PostgreSQL:
docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -e POSTGRES_DB=iot_db -p 5432:5432 -d postgres

### 4. Instalar as Dependências Python
pip install -r requirements.txt

### 5. Ingestão de Dados e Criação das Views
Execute os scripts na ordem abaixo:

1. Carga dos dados no PostgreSQL:
   python src/pipeline.py

2. Criação das Views de agregação:
   python src/create_views.py

### 6. Executar o Dashboard Interativo
streamlit run src/dashboard.py

O dashboard será aberto automaticamente no seu navegador no endereço http://localhost:8501.

---

## 📊 Views SQL Criadas

1. avg_temp_por_dispositivo: Calcula a temperatura média registrada por dispositivo.
2. leituras_por_hora: Agrupa o volume de leituras efetuadas por hora do dia para análise de tráfego.
3. temp_max_min_por_dia: Mapeia as variações térmicas extremas (mínima e máxima) ao longo dos dias.

---

## 💡 Insights Obtidos

* Volume Diurno: Identificação dos horários de pico nas leituras dos sensores IoT.
* Estabilidade Térmica: Análise gráfica para monitoramento de desvios e picos anômalos de temperatura por data.