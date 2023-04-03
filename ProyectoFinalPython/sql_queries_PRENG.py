DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS tipo_transacciones(
    id_tipo_transac INT PRIMARY KEY,
    tipo_transaccion VARCHAR(15) UNIQUE
);

CREATE TABLE IF NOT EXISTS divisas(
    id_divisa INT PRIMARY KEY,
    nombre_divisa VARCHAR(15) UNIQUE,
    simbolo VARCHAR(2) UNIQUE
);

CREATE TABLE IF NOT EXISTS tipo_documentos(
    id_tipo_documento INT PRIMARY KEY,
    nombre_tipo_documento VARCHAR(15) UNIQUE
);

CREATE TABLE IF NOT EXISTS documentos(
    id_documento INT PRIMARY KEY,
    nombre_documento VARCHAR(50),
    uri_documento VARCHAR(100),
    fecha_hora_emision TIMESTAMP,
    tipo_documento INT,

    CONSTRAINT fk_tipo_documento
        FOREIGN KEY (tipo_documento)
            REFERENCES tipo_documentos(id_tipo_documento)

);

CREATE TABLE IF NOT EXISTS generos(
    id_genero INT PRIMARY KEY,
    genero VARCHAR(10) UNIQUE
);

CREATE TABLE IF NOT EXISTS sectores(
    id_sector INT PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE,
    latitud DOUBLE PRECISION,
    longitud DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS direcciones(
    id_direccion INT PRIMARY KEY,
    no_casa VARCHAR(15),
    avenida VARCHAR(50),
    calle VARCHAR(50),
    zona INT,
    id_sector INT,

    CONSTRAINT fk_direccion_sector
        FOREIGN KEY (id_sector)
            REFERENCES sectores(id_sector)
);

CREATE TABLE IF NOT EXISTS cargos(
    id_cargo INT PRIMARY KEY,
    titulo_cargo VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS colaboradores(
    id_colaborador INT PRIMARY KEY,
    nombre VARCHAR(30),
    apellido VARCHAR(30),
    id_cargo INT,

    CONSTRAINT fk_cargo_colaborador
        FOREIGN KEY (id_cargo)
            REFERENCES cargos(id_cargo)
);

CREATE TABLE IF NOT EXISTS sucursales(
    id_sucursal INT PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE,
    id_gerente INT,

    CONSTRAINT fk_sucursal_colaborador
        FOREIGN KEY (id_gerente)
            REFERENCES colaboradores(id_colaborador)
);

CREATE TABLE IF NOT EXISTS tipos_cuentas(
    id_tipo_cuenta INT PRIMARY KEY,
    tipo_cuenta VARCHAR(15) UNIQUE
);

CREATE TABLE IF NOT EXISTS tarjetas(
    id_tarjeta INT PRIMARY KEY,
    nombre VARCHAR(50),
    vencimiento TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cuentas(
    id_cuenta INT PRIMARY KEY,
    nombre_cuenta VARCHAR(75),
    id_tipo_cuenta INT,
    no_tarjeta INT,

    CONSTRAINT fk_cuentas_tipo_cuentas
        FOREIGN KEY (id_tipo_cuenta)
            REFERENCES tipos_cuentas(id_tipo_cuenta),

    CONSTRAINT fk_cuentas_tarjeta
        FOREIGN KEY (no_tarjeta)
            REFERENCES tarjetas(id_tarjeta)
);

CREATE TABLE IF NOT EXISTS clientes(
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    correo VARCHAR(100),
    fecha_nacimiento DATE,
    telefono VARCHAR(20),
    id_direccion INT,
    id_genero INT,

    CONSTRAINT fk_clientes_generos
        FOREIGN KEY (id_genero)
            REFERENCES generos(id_genero),

    CONSTRAINT fk_cliente_direccion
        FOREIGN KEY (id_direccion)
            REFERENCES direcciones(id_direccion)
);

CREATE TABLE IF NOT EXISTS cuentas_clientes(
    id_cuenta INT,
    id_cliente INT,
    fecha_creacion TIMESTAMP,
    balance DOUBLE PRECISION,

    CONSTRAINT pk_cuentas_clientes
        PRIMARY KEY (id_cuenta, id_cliente),

    CONSTRAINT fk_cuentas_clientes
        FOREIGN KEY (id_cuenta)
            REFERENCES cuentas(id_cuenta),

    CONSTRAINT fk_clientes_cuetnas
        FOREIGN KEY (id_cliente)
            REFERENCES clientes(id_cliente)
);

CREATE TABLE IF NOT EXISTS cuentas(
    id_cuentas INT PRIMARY KEY,
    nombre_cuenta VARCHAR(50),
    id_tipo_cuenta INT,
    id_no_tarjeta INT,

    CONSTRAINT fk_cuentas_tipoCuentas
        FOREIGN KEY (id_tipo_cuenta)
            REFERENCES tipos_cuentas(id_tipo_cuenta),

    CONSTRAINT fk_cuentas_noTarjeta
        FOREIGN KEY (id_no_tarjeta)
            REFERENCES tarjetas(id_tarjeta)
);


CREATE TABLE IF NOT EXISTS transacciones(
    id_transaccion INT PRIMARY KEY,
    fecha_hora TIMESTAMP,
    monto DOUBLE PRECISION,
    no_confirmacion INT UNIQUE,

    id_tipo_transaccion INT,
    id_divisa INT,
    id_cliente INT,
    id_documento_respaldo INT,
    id_sucursal INT,
    id_colaborador INT,
    id_cuenta_origen INT,
    id_cuenta_destino INT,

    CONSTRAINT fk_tipo_transaccion_transaccion
        FOREIGN KEY (id_tipo_transaccion)
            REFERENCES tipo_transacciones(id_tipo_transac),

    CONSTRAINT fk_tipo_divisa_transaccion
        FOREIGN KEY (id_divisa)
            REFERENCES divisas(id_divisa),

    CONSTRAINT fk_cliente_transaccion
        FOREIGN KEY (id_cliente)
            REFERENCES clientes(id_cliente),

    CONSTRAINT fk_documento_transaccion
        FOREIGN KEY (id_documento_respaldo)
            REFERENCES documentos(id_documento),

    CONSTRAINT fk_sucursal_transaccion
        FOREIGN KEY (id_sucursal)
            REFERENCES sucursales(id_sucursal),

    CONSTRAINT fk_colaborador_transaccion
        FOREIGN KEY (id_colaborador)
            REFERENCES colaboradores(id_colaborador),

    CONSTRAINT fk_cuentaOrigen_transaccion
        FOREIGN KEY (id_cuenta_origen)
            REFERENCES cuentas(id_cuenta),

    CONSTRAINT fk_cuentaDestino_transaccion
        FOREIGN KEY (id_cuenta_destino)
            REFERENCES cuentas(id_cuenta)
);

SELECT * FROM tipo_transacciones;
SELECT * FROM divisas; '''