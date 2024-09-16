/**
La presente consulta SQL calcula las variables necesarias dentro del proyecto de acuerdo
con las reglas del negocio establecidas por medio del contrato con el comercio NexaTech Industries
**/

CREATE TEMPORARY TABLE {} AS
WITH commission_rule_1 AS (
SELECT
    COUNT(*) AS total_petitions,
    commerce_id,
    ? AS iva,
    ? AS mes,
    ? AS anio
FROM apicall
WHERE   ask_status = 'Successful' 
    AND commerce_id = 'Vj9W-c4Pm-ja0X-fC1C' 
    AND strftime('%m', date_api_call) = mes
    AND strftime('%Y', date_api_call) = anio
GROUP BY 2, 3, 4, 5
)

,commission_rule_2 AS (
SELECT
    CASE 
        WHEN total_petitions >= 0 AND total_petitions <= 10000 THEN 250*iva
        WHEN total_petitions >= 10001 AND total_petitions <= 20000 THEN 200*iva
        WHEN total_petitions >= 20001 THEN 170*iva
        END AS commission,
    total_petitions,
    commerce_id,
    iva,
    mes,
    anio
FROM commission_rule_1
)

SELECT
    total_petitions*commission AS total_value,
    commerce_id,
    commission/iva AS Valor_comision,
    ROUND(iva-1, 2) AS Valor_iva,
    anio || mes AS Fecha_Mes
FROM commission_rule_2;