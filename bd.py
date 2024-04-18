import psycopg2

def create_db(conn):
    """Функция, создающая структуру БД (таблицы)."""
    #имя
    #фамилия
    #email
    #телефон
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(80) NOT NULL,
            last_name VARCHAR(80) NOT NULL,
            email VARCHAR(254),
            phones VARCHAR(255)[]);
        """)
    pass

def add_client(conn, first_name, last_name, email, phones):
    """Функция, позволяющая добавить нового клиента."""
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO client(first_name, last_name, email, phones) 
        VALUES(%s, %s, %s, %s);
        """, (first_name, last_name, email, phones))
        conn.commit()
    pass

def data_checking(conn):
    """Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону."""
    #select
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM client;
        """)
        print(cur.fetchall())
    pass

def add_phone(conn, client_id, phone):
    """Функция, позволяющая добавить телефон для существующего клиента."""
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE client
        SET phones = %s
        WHERE id = %s
        """,
        (phone, client_id))
        conn.commit()
    pass

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    """Функция, позволяющая изменить данные о клиенте."""
    #update
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE client
        SET first_name = %s,
            last_name = %s,
            email = %s,
            phones = %s
        WHERE id = %s;
        """, (first_name, last_name, email, phones, client_id))
        conn.commit()
    pass

def delete_phone(conn, client_id, phone):
    """Функция, позволяющая удалить телефон для существующего клиента."""
    #delete
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM client 
        WHERE id=%s AND phones=%s;
        """,(client_id, phone))
        conn.commit()
    pass


def delete_client(conn, client_id):
    """Функция, позволяющая удалить существующего клиента."""
    #delete
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM client 
        WHERE id=%s;
        """,(client_id,))
        conn.commit()

    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    """Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону."""
    #select
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM client;
        """)
        print(cur.fetchall())
    pass


with (psycopg2.connect(database="DataBasePy", user="postgres",
                       password="postgres") as conn):
    create_db(conn)
    add_client(conn, first_name='Наталья', last_name='Смирнова', email='natalia1990@gmail.com',
               phones='00000001')
    # data_checking(conn)
    add_phone(conn, client_id=13, phone="00000000")
    data_checking(conn)
    change_client(conn, client_id = 14, first_name='Наташи', last_name='Смир',
                  email='fjfjfj@gmail.com',
                  phones=None)
    # data_checking(conn)
    delete_phone(conn, client_id=11, phone=None)
    # data_checking(conn)
    delete_client(conn, client_id=19)
    # data_checking(conn)
    find_client(conn, first_name=None, last_name=None, email=None, phone=None)

    pass  # вызывайте функции здесь

conn.close()




