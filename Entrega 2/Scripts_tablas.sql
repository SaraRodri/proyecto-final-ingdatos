----Tablas actualizadas
CREATE TABLE categoria(
	id int,
	nombre text,
	PRIMARY KEY (id)
);

CREATE TABLE autor(
	id int,
	nombre text,
	fecha_nto date,
	PRIMARY KEY (id)
);

CREATE TABLE ubicacion(
	id int,
	ubicacion text,
	PRIMARY KEY (id)
);

CREATE TABLE editorial(
	id int,
	nombre text,
	id_ubicacion int,
	PRIMARY KEY (id),
	FOREIGN KEY (id_ubicacion) REFERENCES ubicacion(id)
);
CREATE TABLE usuario(
	id text,
	nombre varchar(80),
	PRIMARY KEY (id)
);
CREATE TABLE libro (
	id text,
	titulo text,
	publicacion_yt int,
	num_paginas int,
	id_categoria int,
	id_editorial int,
	id_autor int,
	PRIMARY KEY(id),
	FOREIGN KEY (id_categoria) REFERENCES categoria(id),
	FOREIGN KEY (id_editorial) REFERENCES editorial(id),
	FOREIGN KEY (id_autor) REFERENCES autor(id)
);


CREATE TABLE evaluar(
	id_Usuario text,
	id_libro text,
	calificacion int,
	PRIMARY KEY(id_Usuario,id_libro),
	FOREIGN KEY (id_Usuario) REFERENCES usuario(id),
	FOREIGN KEY (id_libro) REFERENCES libro(id)
);
