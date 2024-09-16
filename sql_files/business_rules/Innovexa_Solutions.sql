/**
La presente consulta SQL calcula las variables necesarias dentro del proyecto de acuerdo
con las reglas del negocio establecidas por medio del contrato con el comercio Innovexa Solutions
**/

CREATE TEMPORARY TABLE {} AS
WITH commission_rule_1 AS (
SELECT
    commerce_id,
    ask_status,
    ? AS iva,
    ? AS mes,
    ? AS anio
FROM apicall
WHERE   commerce_id = 'KaSn-4LHo-m6vC-I4PU' 
    AND strftime('%m', date_api_call) = mes
    AND strftime('%Y', date_api_call) = anio
)

, commission_rule_2 AS(
SELECT
    CASE 
        WHEN ask_status = 'Successful' THEN 300 * iva END AS commission,
    commerce_id,
    iva,
    mes,
    anio
FROM
    commission_rule_1
)

SELECT
    SUM(commission) AS total_value,
    commerce_id,
    commission/iva AS Valor_comision,
    ROUND(iva-1, 2) AS Valor_iva,
    anio || mes AS Fecha_Mes
FROM commission_rule_2;