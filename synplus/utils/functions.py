import sqlite3


def synplus_init() -> None:
    print("""
    _______  __   __  __    _  _______  ___      __   __  _______ 
   |       ||  | |  ||  |  | ||       ||   |    |  | |  ||       |
   |  _____||  |_|  ||   |_| ||    _  ||   |    |  | |  ||  _____|
   | |_____ |       ||       ||   |_| ||   |    |  |_|  || |_____ 
   |_____  ||_     _||  _    ||    ___||   |___ |       ||_____  |
    _____| |  |   |  | | |   ||   |    |       ||       | _____| |
   |_______|  |___|  |_|  |__||___|    |_______||_______||_______|
                                                           v0.1.0
""")


def who(user: str, password: str) -> str:

    user = user.lower()

    is_user_admin = user == "admin" and password == "admin"
    is_data_viewer = user == "data" and password == "viewer"

    if is_user_admin:
        return "admin"

    if is_data_viewer:
        return "viewer"
    
    return "guest"


def insert_data(city, gender, lgbtqia_plus):
    
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO data (city, gender, lgbtqia_plus)
    VALUES (?,?,?)
    """, (city, gender, lgbtqia_plus))

    conn.commit()
    print()
    print('!! Dados inseridos com sucesso.')
    conn.close()


def update_data(id, city, gender, lgbtqia_plus):

    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE data
    SET city = ?, gender = ?, lgbtqia_plus = ?
    WHERE id = ?
    """, (city, gender, lgbtqia_plus, id))

    conn.commit()
    print()
    print('!! Dados atualizados com sucesso.')
    conn.close()


def read_data(city):

    cities = ["recife", "jaboatao", "camaragibe"]

    if city in cities:

        conn = sqlite3.connect("storage.db")
        cursor = conn.cursor()

        cursor.execute(f"""
        SELECT * FROM data WHERE city="{city}";
        """)

        print()
        for linha in cursor.fetchall():
            print(linha)

        conn.close()


def remove_data(id):

    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM data
    WHERE id = ?
    """, (id,))

    conn.commit()
    print()
    print('!! Registro excluido com sucesso.')
    conn.close()


def data_view():

    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM data;
    """)

    print()
    for linha in cursor.fetchall():
        print(linha)

    conn.close()
