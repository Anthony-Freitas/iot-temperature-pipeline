import os
import pandas as pd
from sqlalchemy import create_engine, text

DATABASE_URI = 'postgresql+psycopg2://postgres:iot123@localhost:5432/iot_db'
engine = create_engine(DATABASE_URI)

def run_pipeline():
    print("Iniciando leitura do arquivo CSV...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, '..', 'data', 'IOT-temp.csv')
    
    df = pd.read_csv(csv_path)
    
    print("Tratando e transformando os dados (ETL)...")
    # 1. Padronizar nomes de colunas
    df.columns = df.columns.str.strip().str.lower()
    
    # 2. Renomear as colunas
    df.rename(columns={
        'room_id/id': 'device_id',
        'noted_date': 'timestamp',
        'temp': 'temperature',
        'out/in': 'location'
    }, inplace=True)
    
    # 3. Converter coluna de data/hora para datetime do pandas
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d-%m-%Y %H:%M', errors='coerce')
    
    print("Preparando o banco de dados...")
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS temperature_readings CASCADE;"))
    
    print("Inserindo dados tratados no PostgreSQL...")
    df.to_sql('temperature_readings', con=engine, if_exists='replace', index=False)
    print("Dados limpos e inseridos com sucesso!")

if __name__ == '__main__':
    run_pipeline()