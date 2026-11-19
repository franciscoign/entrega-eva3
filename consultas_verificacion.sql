USE gimnasio_db;

SELECT COUNT(*) AS total_padres FROM socios_plan;

SELECT COUNT(*) AS total_hijos FROM socios_socio;

SELECT h.id, h.nombre, p.nombre AS clasificacion
FROM socios_socio h
INNER JOIN socios_plan p ON h.plan_id = p.id;
