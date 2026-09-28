from sqlalchemy import create_engine, text

DATABASE_URI = 'postgresql+psycopg2://postgres:iot123@localhost:5432/iot_db'
engine = create_engine(DATABASE_URI)

sql_commands = [
    """
    CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
    SELECT 
        device_id, 
        ROUND(AVG(temperature)::numeric, 2) AS avg_temp
    FROM temperature_readings
    GROUP BY device_id;
    """,
    """
    CREATE OR REPLACE VIEW leituras_por_hora AS
    SELECT 
        EXTRACT(HOUR FROM timestamp) AS hora,
        COUNT(*) AS contagem
    FROM temperature_readings
    WHERE timestamp IS NOT NULL
    GROUP BY hora
    ORDER BY hora;
    """,
    """
    CREATE OR REPLACE VIEW temp_max_min_por_dia AS
    SELECT 
        DATE(timestamp) AS data,
        MAX(temperature) AS temp_max,
        MIN(temperature) AS temp_min
    FROM temperature_readings
    WHERE timestamp IS NOT NULL
    GROUP BY DATE(timestamp)
    ORDER BY data;
    """
]

def create_views():
    with engine.begin() as conn:
        for query in sql_commands:
            conn.execute(text(query))
        print("Views SQL criadas com sucesso no PostgreSQL!")

if __name__ == '__main__':
    create_views()