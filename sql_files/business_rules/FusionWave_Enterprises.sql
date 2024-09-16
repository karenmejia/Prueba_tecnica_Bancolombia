/**
La presente consulta SQL calcula las variables necesarias dentro del proyecto de acuerdo
con las reglas del negocio establecidas por medio del contrato con el comercio FusionWave Enterprises
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
WHERE   commerce_id = 'GdEQ-MGb7-LXHa-y6cd' 
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
        WHEN ask_status = 'Successful' THEN 300*iva 
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
        WHEN unsuccessful_petitions >= 2500 AND unsuccessful_petitions <= 4500 THEN (total_petitions*commission) * 0.95
        WHEN unsuccessful_petitions >= 4501 THEN (total_petitions*commission) * 0.92
    ELSE total_petitions*commission 
    END AS total_value,
    commerce_id,
    commission/iva AS Valor_comision,
    ROUND(iva-1, 2) AS Valor_iva,
    anio || mes AS Fecha_Mes

FROM commission_rule_3
WHERE ask_status = 'Successful';

