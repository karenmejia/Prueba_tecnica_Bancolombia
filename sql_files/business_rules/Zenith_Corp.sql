/**
La presente consulta SQL calcula las variables necesarias dentro del proyecto de acuerdo
con las reglas del negocio establecidas por medio del contrato con el comercio Zenith Corp
**/

CREATE TEMPORARY TABLE {} AS
WITH commission_rule_1 AS (
SELECT
    COUNT(*) AS total_petitions,
    ask_status,
    commerce_id,
    ? AS iva,
    ? AS mes,
    ? AS anio
FROM apicall
WHERE   commerce_id = '3VYd-4lzT-mTC3-DQN5' 
    AND strftime('%m', date_api_call) = mes
    AND strftime('%Y', date_api_call) = anio
GROUP BY 2, 3, 4, 5
)
,commission_rule_2 AS (
SELECT 
    total_petitions AS unsuccessful_petitions
FROM commission_rule_1
WHERE ask_status = 'Unsuccessful'
)
,commission_rule_3 AS (
SELECT
    CASE 
        WHEN ask_status = 'Successful' AND total_petitions >= 0 AND total_petitions <= 22000 THEN 250*iva 
        WHEN ask_status = 'Successful' AND total_petitions >= 22001 THEN 130*iva
        END AS commission, 
    total_petitions,
    ask_status,
    unsuccessful_petitions,
    commerce_id,
    iva,
    mes,
    anio
FROM commission_rule_1, commission_rule_2
)
SELECT
    CASE
        WHEN unsuccessful_petitions > 6000 THEN (total_petitions*commission) * 0.95
    ELSE total_petitions*commission 
    END AS total_value,
    commerce_id,
    commission/iva AS Valor_comision,
    ROUND(iva-1, 2) AS Valor_iva,
    anio || mes AS Fecha_Mes 
FROM commission_rule_3
WHERE ask_status = 'Successful';