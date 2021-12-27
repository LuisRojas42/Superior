insert into Usuario (id_Usuario, Nombre) values(1, 'Luis');
insert into Usuario (id_Usuario, Nombre) values(2, 'Alex');
insert into Usuario (id_Usuario, Nombre) values(3, 'Fernanada');
insert into Usuario (id_Usuario, Nombre) values(4, 'Jessica');
insert into Usuario (id_Usuario, Nombre) values(5, 'Alberto');
insert into Usuario (id_Usuario, Nombre) values(6, 'Gonzalo');

insert into Orden (id_Orden, id_Usuario, fecha) values(1, 1, now());
insert into Orden (id_Orden, id_Usuario, fecha) values(2, 2, now()-1);
insert into Orden (id_Orden, id_Usuario, fecha) values(3, 3, now()-2);

insert into Orden_Platillo(id_Orden, id_Platillo) values(1, 1);
insert into Orden_Platillo(id_Orden, id_Platillo) values(1, 35);
insert into Orden_Platillo(id_Orden, id_Platillo) values(1, 43);

insert into Revisados(id_Usuario, id_Platillo) values(1, 1);
insert into Revisados(id_Usuario, id_Platillo) values(1, 35);
insert into Revisados(id_Usuario, id_Platillo) values(1, 43);
insert into Revisados(id_Usuario, id_Platillo) values(1, 51);

insert into Orden_Platillo(id_Orden, id_Platillo) values(2, 1);
insert into Orden_Platillo(id_Orden, id_Platillo) values(2, 35);
insert into Orden_Platillo(id_Orden, id_Platillo) values(2, 45);

insert into Revisados(id_Usuario, id_Platillo) values(2, 1);
insert into Revisados(id_Usuario, id_Platillo) values(2, 35);
insert into Revisados(id_Usuario, id_Platillo) values(2, 45);
insert into Revisados(id_Usuario, id_Platillo) values(2, 51);

insert into Orden_Platillo(id_Orden, id_Platillo) values(3, 43);
insert into Orden_Platillo(id_Orden, id_Platillo) values(3, 35);
insert into Orden_Platillo(id_Orden, id_Platillo) values(3, 51);

insert into Revisados(id_Usuario, id_Platillo) values(3, 43);
insert into Revisados(id_Usuario, id_Platillo) values(3, 35);
insert into Revisados(id_Usuario, id_Platillo) values(3, 52);
insert into Revisados(id_Usuario, id_Platillo) values(3, 45);