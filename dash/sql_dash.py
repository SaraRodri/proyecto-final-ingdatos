def ctAutores():
    return """SELECT ROUND(cal.prom),COUNT (ROUND(cal.prom)) from(
            SELECT autor.nombre,AVG(promedio.avg) as PROM
            FROM (libro inner join autor ON libro.id_autor=autor.id) INNER JOIN (SELECT id_libro, AVG(calificacion) 
                    FROM evaluar GRoup by id_libro) AS promedio ON Libro.id=promedio.id_libro
                    GROUP BY autor.nombre
                    ORDER BY PROM DESC) as cal GROUP BY ROUND(cal.prom) ORDER BY ROUND(cal.prom) DESC;"""


def ctEditorial():
    return """SELECT ROUND(cal.prom),COUNT (ROUND(cal.prom)) from(
                SELECT editorial.nombre,AVG(promedio.avg) as PROM
                FROM (libro INNER JOIN editorial ON libro.id_editorial=editorial.id) INNER JOIN (SELECT id_libro, AVG(calificacion) FROM evaluar GRoup by id_libro) AS promedio ON Libro.id=promedio.id_libro
                        GROUP BY editorial.nombre
                        ORDER BY PROM DESC) as cal GROUP BY ROUND(cal.prom) ORDER BY ROUND(cal.prom) DESC;"""


def librosAutor():
    return """SELECT autor.nombre,count(autor.id)
            FROM libro INNER JOIN autor on libro.id_autor=autor.id
			WHERE autor.nombre != 'N/A'
            GROUP BY autor.id
            ORDER BY count(autor.id) DESC;"""


def librosEditorial():
    return """SELECT editorial.nombre,count(editorial.id)
                FROM libro inner join editorial on libro.id_editorial=editorial.id
                WHERE editorial.nombre != 'n/a'
                GROUP BY editorial.id
                ORDER BY count(editorial.id) DESC;"""


def calificacion_yr():
    return """SELECT publicacion_yt, Count(publicacion_yt) 
        from libro 
        where publicacion_yt!=1 and publicacion_yt!= 2023 AND publicacion_yt!= 2024 AND publicacion_yt!= 2025 AND publicacion_yt!= 2023 AND publicacion_yt!= 2030 AND publicacion_yt>1800
        group by publicacion_yt order by publicacion_yt;"""


def prom_aut():
    return """SELECT autor.nombre,AVG(promedio.avg) as PROMEDIO
        FROM (libro inner join autor ON libro.id_autor=autor.id) INNER JOIN (SELECT id_libro, AVG(calificacion) FROM evaluar GRoup by id_libro) AS promedio ON Libro.id=promedio.id_libro
        GROUP BY autor.nombre
        ORDER BY PROMEDIO DESC;"""


def categoria():
    return """SELECT categoria.nombre, COUNT (libro.id)
            from libro INNER JOIN categoria on libro.id_categoria=categoria.id
            WHERE categoria.nombre != 'N/A'
            GROUP BY categoria.nombre
            ORDER BY COUNT (libro.id) DESC;"""
