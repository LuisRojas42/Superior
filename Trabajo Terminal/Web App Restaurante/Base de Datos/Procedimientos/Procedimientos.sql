drop procedure if exists Mas_Pedido;
DELIMITER $$
create procedure Mas_Pedido(in tiempo int, in categoria char)
begin
    #Más pedido en N tiempo
	select Platillo.Nombre_platillo, count(Orden_Platillo.id_Platillo) as pedidos,
	Platillo.id_Categoria from Orden_Platillo 
	inner join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo
	inner join Orden on Orden.id_Orden = Orden_Platillo.id_Orden
	WHERE Orden.fecha >= CURRENT_DATE() - INTERVAL tiempo DAY
	and Platillo.id_Categoria  LIKE categoria 
	group by Orden_Platillo.id_Platillo;
end$$
DELIMITER ;

call Mas_Pedido(10, '%');

drop procedure if exists Set_Revisado;
DELIMITER $$
create procedure Set_Revisado(
	in id_Usuario_param int, in id_Platillo_param int)
begin
    #Más pedido en N tiempo
	insert into Revisados(id_Usuario, id_Platillo) 
    values(id_Usuario_param, id_Platillo_param);
end$$
DELIMITER ;

call Set_Revisado(3, 1);

drop procedure if exists Interacciones_usuario;
DELIMITER $$
create procedure Interacciones_usuario(
    in id_Usuario_param int)
begin
    select Nombre_platillo, tipo from (

		select Platillo.Nombre_Platillo, "Orden" as tipo from Usuario inner join Orden on Orden.id_Usuario = Usuario.id_Usuario inner join Orden_Platillo on Orden.id_Orden = Orden_Platillo.id_Orden inner join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo where Usuario.id_Usuario = id_Usuario_param

	)as Ordenes
	union (

		select Platillo.Nombre_platillo, "Rankeado" as tipo from Usuario inner join Rankings on Usuario.id_Usuario = Rankings.id_Usuario inner join Platillo on Platillo.id_Platillo = Rankings.id_Platillo	where Usuario.id_Usuario = id_Usuario_param

	)union (

		select Platillo.Nombre_platillo, "Visto" as tipo from Usuario inner join Revisados on Usuario.id_Usuario = Revisados.id_Usuario inner join Platillo on Platillo.id_Platillo = Revisados.id_Platillo where Usuario.id_Usuario = id_Usuario_param

	);
end$$
DELIMITER ;

call Interacciones_usuario(1);

drop procedure if exists Platillo_etiquetas;
DELIMITER $$
create procedure Platillo_etiquetas()
begin
    #Etiquetas formadas de Ingredientes y Contenido de cada Platillo pedido
	select Orden.id_Usuario, Platillo.id_Platillo, Ingrediente.Nombre_Ingrediente as etiqueta from Orden_Platillo 
	join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo
	join Orden on Orden.id_Orden = Orden_Platillo.id_Orden
	join Ingrediente_Platillo on Ingrediente_Platillo.id_Platillo = Platillo.id_Platillo
	join Ingrediente on Ingrediente.id_Ingrediente = Ingrediente_Platillo.id_Ingrediente
	union
	select Orden.id_Usuario, Platillo.id_Platillo, Contenido_Platillo.Tipo as etiqueta from Orden_Platillo 
	join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo
	join Orden on Orden.id_Orden = Orden_Platillo.id_Orden
	join Contenido_Platillo on Contenido_Platillo.id_Platillo = Platillo.id_Platillo
	union
	select Orden.id_Usuario, Platillo.id_Platillo, Contenido_Platillo.Sabor as etiqueta from Orden_Platillo 
	join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo
	join Orden on Orden.id_Orden = Orden_Platillo.id_Orden
	join Contenido_Platillo on Contenido_Platillo.id_Platillo = Platillo.id_Platillo
	union
	select Orden.id_Usuario, Platillo.id_Platillo, Contenido_Platillo.Ocacion as etiqueta from Orden_Platillo 
	join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo
	join Orden on Orden.id_Orden = Orden_Platillo.id_Orden
	join Contenido_Platillo on Contenido_Platillo.id_Platillo = Platillo.id_Platillo
	union
	select Orden.id_Usuario, Platillo.id_Platillo, Contenido_Platillo.Temperatura as etiqueta from Orden_Platillo 
	join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo
	join Orden on Orden.id_Orden = Orden_Platillo.id_Orden
	join Contenido_Platillo on Contenido_Platillo.id_Platillo = Platillo.id_Platillo;
end$$
DELIMITER ;

call Platillo_etiquetas();