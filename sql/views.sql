## View 1
    CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
    SELECT 
        "room_id/id" AS device_id, 
        AVG(temp) AS avg_temp
    FROM temperature_readings
    GROUP BY "room_id/id";
    ,

## View 2
    CREATE OR REPLACE VIEW leituras_por_hora AS
    SELECT 
        EXTRACT(HOUR FROM TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora,
        COUNT(*) AS contagem
    FROM temperature_readings
    GROUP BY hora
    ORDER BY hora;
    ,

## View 3
    CREATE OR REPLACE VIEW temp_max_min_por_dia AS
    SELECT 
        DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS data,
        MAX(temp) AS temp_max,
        MIN(temp) AS temp_min
    FROM temperature_readings
    GROUP BY DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI'))
    ORDER BY data;