select * from orden;
select * from Orden_Platillo;
select * from Revisados;
select * from Usuario;

SET SQL_SAFE_UPDATES = 0;
#delete from Usuario where Nombre = 'Usr01';
#delete from Revisados where id_Usuario = 3 and id_Platillo = 2;
#delete from Rankings;
update Usuario set Nombre = "usr" where Nombre="101994360380017395432";
SET SQL_SAFE_UPDATES = 1;

select Orden.id_orden, Usuario.Nombre, Platillo.Nombre_platillo, Orden.fecha from Orden
inner join Usuario on Usuario.id_Usuario = Orden.id_Usuario
inner join Orden_Platillo on Orden.id_Orden = Orden_Platillo.id_orden
inner join Platillo on Platillo.id_Platillo = Orden_platillo.id_Platillo;

select Orden.id_orden, Usuario.Nombre, Platillo.Nombre_platillo, Orden.fecha from Orden
inner join Usuario on Usuario.id_Usuario = Orden.id_Usuario
inner join Orden_Platillo on Orden.id_Orden = Orden_Platillo.id_orden
inner join Platillo on Platillo.id_Platillo = Orden_platillo.id_Platillo
WHERE Orden.fecha >= CURRENT_DATE() - INTERVAL 2 DAY;

select Orden.id_orden, Usuario.Nombre, Platillo.Nombre_platillo 
from Orden inner join Usuario on Usuario.id_Usuario = Orden.id_Usuario 
inner join Orden_Platillo on Orden.id_Orden = Orden_Platillo.id_orden 
inner join Platillo on Platillo.id_Platillo = Orden_platillo.id_Platillo
where Usuario.id_Usuario = 1;

select Nombre_platillo, tipo from (

	select Platillo.Nombre_platillo, "Orden" as tipo from Usuario 
	inner join Orden on Orden.id_Usuario = Usuario.id_Usuario
	inner join Orden_Platillo on Orden.id_Orden = Orden_Platillo.id_orden 
	inner join Platillo on Platillo.id_Platillo = Orden_platillo.id_Platillo
	where Usuario.id_Usuario = 1

)as Ordenes
union (

	select Platillo.Nombre_platillo, "Rankeado" as tipo from Usuario
	inner join Rankings on Usuario.id_Usuario = Rankings.id_Usuario
	inner join Platillo on Platillo.id_Platillo = Rankings.id_Platillo
	where Usuario.id_Usuario = 1

)union (

	select Platillo.Nombre_platillo, "Visto" as tipo from Usuario
	inner join Revisados on Usuario.id_Usuario = Revisados.id_Usuario
	inner join Platillo on Platillo.id_Platillo = Revisados.id_Platillo
	where Usuario.id_Usuario = 1

);

select Platillo.Nombre_platillo, "Orden" as tipo from Usuario 
inner join Orden on Orden.id_Usuario = Usuario.id_Usuario
inner join Orden_Platillo on Orden.id_Orden = Orden_Platillo.id_orden 
inner join Platillo on Platillo.id_Platillo = Orden_platillo.id_Platillo
where Usuario.id_Usuario = 1;
    
select Platillo.Nombre_platillo, "Rankeado" as tipo from Usuario
inner join Rankings on Usuario.id_Usuario = Rankings.id_Usuario
inner join Platillo on Platillo.id_Platillo = Rankings.id_Platillo
where Usuario.id_Usuario = 1;

select Platillo.Nombre_platillo, "Visto" as tipo from Usuario
inner join Revisados on Usuario.id_Usuario = Revisados.id_Usuario
inner join Platillo on Platillo.id_Platillo = Revisados.id_Platillo
where Usuario.id_Usuario = 1;

select p.id_Platillo, Nombre_platillo, Nombre_ingrediente from Ingrediente_Platillo ip
join Ingrediente i on i.id_Ingrediente = ip.id_Ingrediente
join Platillo p on p.id_Platillo = ip.id_Platillo where ip.id_Platillo = 15;

select p.id_Platillo, Nombre_platillo, Nombre_etiqueta, cantidad from Etiqueta_Platillo ep
join Etiqueta e on e.id_Etiqueta = ep.id_Etiqueta
join Platillo p on p.id_Platillo = ep.id_Platillo where ep.id_Platillo = 2;

use Restaurante;
select max(id_Orden) from Orden;
insert into Orden(id_Orden, id_Usuario, fecha, Codigo_qr) values(24, (select id_Usuario from Usuario where nombre='114518122078180188707'), CURDATE(), 'qr');

select * from Orden;

insert into Orden_Platillo(id_Orden, id_Platillo) values(24, (select id_Platillo from Platillo where Nombre_platillo = 'Cerveza Indio'));

select * from Orden_Platillo;

call Platillo_etiquetas();

select id_Usuario from Usuario where nombre='114518122078180188707';

insert into Usuario(nombre) values("114518122078180188707");

select * from Usuario;

SET SQL_SAFE_UPDATES = 0;
update Usuario set Nombre='3' where Nombre = 'Alex';
SET SQL_SAFE_UPDATES = 1;

insert into Rankings (id_Usuario, id_Platillo, ranking) values(3, 1, 5);

select id_Usuario from Usuario where nombre='3';

select * from Rankings;

