import os
import pandas as pd
from sqlalchemy import create_engine, text

# Conexão com o PostgreSQL no Docker
DATABASE_URI = 'postgresql+psycopg2://postgres:iot123@localhost:5432/iot_db'
engine = create_engine(DATABASE_URI)

def run_pipeline():
    print("Iniciando leitura do arquivo CSV...")
    
    # Caminho ajustado independente de onde o script é executado
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, '..', 'data', 'IOT-temp.csv')
    
    df = pd.read_csv(csv_path)
    
    print("Preparando o banco de dados...")
    # Remove a tabela antiga caso exista, incluindo dependências (Views)
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS temperature_readings CASCADE;"))
    
    print("Inserindo dados no PostgreSQL...")
    df.to_sql('temperature_readings', con=engine, if_exists='replace', index=False)
    print("Dados inseridos com sucesso na tabela 'temperature_readings'!")

if __name__ == '__main__':
    run_pipeline()