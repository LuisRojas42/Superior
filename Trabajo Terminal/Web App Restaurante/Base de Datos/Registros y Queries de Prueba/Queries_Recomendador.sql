#Get-Rankings por Hot Rankings
select Platillo.Nombre_platillo, Rankings.ranking, count(Rankings.ranking) as conteo,
Platillo.id_Categoria from Rankings  
inner join Platillo on Platillo.id_Platillo = Rankings.id_Platillo
WHERE Orden.fecha >= CURRENT_DATE() - INTERVAL 1 DAY 
and Platillo.id_Categoria  LIKE '%' 
group by Rankings.id_Platillo, Rankings.ranking;

#Get-Reglas por FP-Growth
select Platillo.Nombre_platillo, count(Orden_Platillo.id_platillo) as pedidos from Orden_Platillo 
inner join Platillo on Platillo.id_Platillo = Orden_Platillo.id_Platillo
group by Orden_Platillo.id_platillo;

#Get-Asosiaciones por Bayes
select Platillo.Nombre_platillo as id_Platillo, ranking from rankings
inner join Platillo on Platillo.id_Platillo = rankings.id_Platillo;

select Orden.id_orden, Usuario.Nombre, Platillo.Nombre_platillo from Orden 
inner join Usuario on Usuario.id_Usuario = Orden.id_Usuario 
inner join Orden_Platillo on Orden.id_Orden = Orden_Platillo.id_orden 
inner join Platillo on Platillo.id_Platillo = Orden_platillo.id_Platillo;

#Más pedido en N tiempo
select Platillo.Nombre_platillo, count(Orden_Platillo.id_Platillo) as pedidos,
Platillo.id_Categoria from Orden_Platillo 
inner join Platillo on Platillo.id_Platillo = Orden_platillo.id_Platillo
inner join Orden on Orden.id_Orden = Orden_platillo.id_Orden
WHERE Orden.fecha >= CURRENT_DATE() - INTERVAL 1 DAY
and Platillo.id_Categoria  LIKE 2 
group by Orden_Platillo.id_Platillo;

select * from ingrediente;