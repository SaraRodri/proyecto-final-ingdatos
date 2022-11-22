

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
            GROUP BY autor.id
            ORDER BY count(autor.id) DESC;"""

def librosEditorial():
    return """SELECT autor.nombre,count(autor.id)
                FROM libro INNER JOIN autor on libro.id_autor=autor.id
                GROUP BY autor.id
                ORDER BY count(autor.id) DESC;"""

def calificacion_yr():
    return """SELECT libro.publicacion_yt,AVG(prom.cal)
            FROM libro INNER JOIN( SELECT id_libro, AVG(calificacion) as cal FROM evaluar GRoup by id_libro) as prom on libro.id=prom.id_libro
            GROUP BY libro.publicacion_yt
            ORDER BY AVG(prom.cal) DESC;"""

def categoria():
    return """SELECT categoria.nombre, COUNT (libro.id)
            from libro INNER JOIN categoria on libro.id_categoria=categoria.id
            GROUP BY categoria.nombre
            ORDER BY COUNT (libro.id) DESC;"""
