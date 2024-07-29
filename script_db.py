import sqlite3 as sql


def init_db():
    conexao = sql.connect("finances.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            usuario VARCHAR(100) NOT NULL UNIQUE,
            senha VARCHAR(100) NOT NULL
        )
        """
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS categorias (
            id_categoria INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            nome_categoria VARCHAR(100) NOT NULL,
            categoria BOOLEAN
        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            id_usu INT NOT NULL,
            valor FLOAT NOT NULL,
            efetuado BOOLEAN,
            fixo BOOLEAN,
            tipo BOOLEAN,
            data TEXT,
            id_cat INT NOT NULL,
            descricao VARCHAR(200),
            FOREIGN KEY (id_usu) REFERENCES usuarios(id_usuario),
            FOREIGN KEY (id_cat) REFERENCES categorias(id_categoria)
        )
        '''
    )

    conexao.commit()
    conexao.close()


def adc_usuario(usuario, senha):
    conexao = sql.connect("finance.db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha)
    )
    conexao.commit()
    conexao.close()


def adc_categoria(nome, categoria):
    conexao = sql.connect("finance.db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO categorias (nome_categoria, categoria) VALUES (?, ?)", (nome, categoria)
    )
    conexao.commit()
    conexao.close()


def adc_transacao(usuario, valor, efetuado, fixo, tipo, data, categoria, descricao):
    conexao = sql.connect("finance.db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO transacoes (id_usu, valor, efetuado, fixo, tipo, data, id_cat, descricao) VALUES "
        "(?, ?, ?, ?, ?, ?, ?, ?)", (usuario, valor, efetuado, fixo, tipo, data, categoria, descricao)
    )
    conexao.commit()
    conexao.close()


def buscar_categoria(numero_categoria):
    conexao = sql.connect("finances.db")
    with conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """SELECT nome_categoria FROM categorias WHERE categoria = ?;""", (numero_categoria, )
        )
        return cursor.fetchall()


def procura_usuario(nome_usuario):
    conexao = sql.connect("finances.db")
    with conexao:
        cursor = conexao.cursor()
        cursor.execute(
            """SELECT usuario, senha FROM usuarios WHERE usuario = ?""", (nome_usuario, )
        )
        return cursor.fetchone()


if __name__ == '__main__':
    init_db()
