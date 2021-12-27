create database Restaurante;

use Restaurante;

Create Table Categoria(
	id_Categoria int auto_increment,
    Nombre_categoria varchar(50),
    primary key (id_Categoria)
);

Create Table Platillo(
	id_Platillo int auto_increment,
    Nombre_platillo varchar(100),
    id_Categoria int,
    Video_RA varchar(100),
    primary key(id_Platillo),
    index (id_Categoria),
    foreign key (id_Categoria) references Categoria(id_Categoria)
);

Create Table Ingrediente(
	id_Ingrediente int auto_increment,
    Nombre_ingrediente varchar(50),
    primary key (id_Ingrediente)
);

Create Table Etiqueta(
	id_Etiqueta int auto_increment,
    Nombre_etiqueta varchar(50),
    primary key (id_Etiqueta)
);

Create Table Usuario(
	id_Usuario int auto_increment,
    Nombre varchar(50),
    id_Recomendacion int,
    edad int,
    primary key (id_Usuario)
);

Create Table Orden(
	id_Orden int auto_increment,
    id_Usuario int,
    fecha datetime,
    Codigo_qr varchar(100),
    primary key (id_Orden),
    index (id_Usuario),
    foreign key (id_Usuario) references Usuario(id_Usuario)
);

Create Table Ingrediente_Platillo(
	id_Ingrediente int,
    id_Platillo int,
    Cantidad varchar(10),
    index (id_Ingrediente),
    foreign key (id_Ingrediente) references Ingrediente(id_Ingrediente),
    index (id_Platillo),
    foreign key (id_Platillo) references Platillo(id_Platillo)
);

Create Table Orden_Platillo(
	id_Orden int,
    id_Platillo int,
    index (id_Orden),
    foreign key (id_Orden) references Orden(id_Orden),
    index (id_Platillo),
    foreign key (id_Platillo) references Platillo(id_Platillo)
);

Create Table Etiqueta_Platillo(
	id_Etiqueta int,
    id_Platillo int,
    Cantidad varchar(30),
    index (id_Etiqueta),
    foreign key (id_Etiqueta) references Etiqueta(id_Etiqueta),
    index (id_Platillo),
    foreign key (id_Platillo) references Platillo(id_Platillo)
);

Create Table Rankings(
	id_Usuario int,
    id_Platillo int,
    ranking int,
    index (id_Usuario),
    foreign key (id_Usuario) references Usuario(id_Usuario),
    index (id_Platillo),
    foreign key (id_Platillo) references Platillo(id_Platillo)
);

Create Table Contenido_Platillo(
	id_platillo int,
	Tipo varchar(30),
    Sabor varchar(30),
    Ocacion varchar(30),
    Temperatura varchar(30),
    index (id_Platillo),
    foreign key (id_Platillo) references Platillo(id_Platillo)
);

Create Table Revisados(
	id_Usuario int,
    id_Platillo int,
    index (id_Usuario),
    foreign key (id_Usuario) references Usuario(id_Usuario),
    index (id_Platillo),
    foreign key (id_Platillo) references Platillo(id_Platillo)
);
