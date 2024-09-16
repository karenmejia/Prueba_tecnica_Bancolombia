/** 
La presente consulta SQL obtiene la tabla de resultados para ser enviada a cada comercio
teniendo en cuenta si cada uno se encuentra activo o no.
**/

SELECT
    t2.Fecha_Mes,
    t1.commerce_name AS Nombre,
    t1.commerce_nit AS Nit,
    t2.Valor_comision,
    t2.Valor_iva,
    t2.total_value AS Valor_Total,
    t1.commerce_email AS Correo
FROM
    {} t2
INNER JOIN
    commerce t1
ON  t1.commerce_id = t2.commerce_id
WHERE commerce_status = 'Active';
    
