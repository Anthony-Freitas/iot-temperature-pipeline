from sqlalchemy import create_engine, text

# Conexão com o PostgreSQL no Docker
engine = create_engine('postgresql+psycopg2://postgres:iot123@localhost:5432/iot_db')

views_sql = [
    """
    CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
    SELECT 
        "room_id/id" AS device_id, 
        AVG(temp) AS avg_temp
    FROM temperature_readings
    GROUP BY "room_id/id";
    """,
    """
    CREATE OR REPLACE VIEW leituras_por_hora AS
    SELECT 
        EXTRACT(HOUR FROM TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora,
        COUNT(*) AS contagem
    FROM temperature_readings
    GROUP BY hora
    ORDER BY hora;
    """,
    """
    CREATE OR REPLACE VIEW temp_max_min_por_dia AS
    SELECT 
        DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS data,
        MAX(temp) AS temp_max,
        MIN(temp) AS temp_min
    FROM temperature_readings
    GROUP BY DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI'))
    ORDER BY data;
    """
]

def create_views():
    with engine.begin() as conn:
        for query in views_sql:
            conn.execute(text(query))
    print("Views SQL criadas com sucesso!")

if __name__ == '__main__':
    create_views()