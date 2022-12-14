---Carga masiva de la tabla categoria
COPY categoria FROM 'proyecto-final-ingdatos\tablas_f\categoria.csv' WITH DELIMITER ';' CSV HEADER; --check

---Carga masiva de la tabla usuario
COPY usuario FROM 'proyecto-final-ingdatos\tablas_f\usuario_f.csv' WITH DELIMITER ';' CSV HEADER;--check

--Carga masiva de la tabla autor
COPY autor FROM 'proyecto-final-ingdatos\tablas_f\autor_f.csv' WITH DELIMITER ';' CSV HEADER; --check

----Carga masiva de la tabla ubicacion
COPY ubicacion FROM 'proyecto-final-ingdatos\tablas_f\ubicacion.csv' WITH DELIMITER ',' CSV HEADER; --check

--Carga masiva de la tabla editorial
COPY editorial FROM 'proyecto-final-ingdatos\tablas_f\editorial_f.csv' WITH DELIMITER ';' CSV HEADER; --check

--Carga masiva de la tabla libro
COPY libro FROM 'proyecto-final-ingdatos\tablas_f\libro.csv' WITH DELIMITER ';' CSV HEADER; 

--Carga masiva de la tabla evaluar
COPY evaluar FROM 'proyecto-final-ingdatos\tablas_f\evaluar_f.csv' WITH DELIMITER ',' CSV HEADER; 
