CREATE_DW = '''
create table if not exists dimClientes(
	id_cliente int primary key,
	nombre varchar(50), 
	apellido varchar(50),
	correo varchar(50),
	fecha_nacimiento datetime,
	telefono varchar(20),
	no_casa varchar(5),
	avenida int,
	calle int,
	zona int,
	genero varchar(15),
	nombre_sucursal varchar(50)
);

create table if not exists dimCuentas(
	id_cuenta int primary key,
	nombre_cuenta varchar(50),
	balance double,
	id_cliente int,
	tipo_cuenta varchar(50)
);


create table if not exists dimTipoTransacciones(
	id_tipo_transac int primary key,
	tipo_transacciones varchar(50)
);

create table if not exists dimDivisas(
	id_divisa int primary key,
	nombre_divisa varchar(20),
	simbolo varchar(1)
);

create table if not exists dimSucursales(
	id_sucursal int primary key,
	nombre_sucursal varchar(50),
	nombre_sector varchar(50),
	nombre_gerente varchar(50)
);


create table if not exists dimColaboradores(
	id_colaborador int primary key,
	nombre varchar(50),
	apellido varchar(50),
	titulo_cargo varchar(50)
);


create table if not exists dimFechaHora(
	id_fecha varchar(50) primary key,
	year int,
	month int,
	quarter int,
	week int,
	dayofweek int,
	hour int, 
	minute int, 
	is_weekend int,
	fecha_hora datetime
);

-- tabla de hechos
create table if not exists factTransacciones(
	id_transacciion int primary key,
	
	id_divisa int,
	id_cliente int,
	id_colaborador int,
	id_sucursal int,
	id_cuenta_origen int,
	id_cuenta_destino int,
	id_fecha varchar(75),
	monto double,
	
	constraint fk_fact_dimDivisas
		foreign key (id_divisa)
			references dimDivisas(id_divisa),
			
	constraint fk_fact_dimClientes
		foreign key (id_cliente)
			references dimClientes(id_cliente),
			
	constraint fk_fact_dimColaboradores
		foreign key (id_colaborador)
			references dimColaboradores(id_colaborador),
	
	constraint fk_fact_dimSucursal
		foreign key (id_sucursal)
			references dimSucursales(id_sucursal),
	
	constraint fk_fact_dimCuentaO
		foreign key (id_cuenta_origen)
			references dimCuentas(id_cuenta),
	
	constraint fk_fact_dimCuentaD
		foreign key (id_cuenta_destino)
			references dimCuentas(id_cuenta)
);
'''