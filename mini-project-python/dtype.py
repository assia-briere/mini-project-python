import mysql.connector
import datetime

host = "localhost"
user = "root"
password = ""
database = "test"

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    cursor = connection.cursor()

    create_produit = """
    CREATE TABLE IF NOT EXISTS Produits (
        dtype VARCHAR(255),
        id_produit INT AUTO_INCREMENT PRIMARY KEY,
        lib VARCHAR(255),
        prix INT,
        cv INT,
        marque VARCHAR(255),
        martricule VARCHAR(255),
        carb VARCHAR(255),
        proccesseur VARCHAR(255),
        ram VARCHAR(255),
        disc VARCHAR(255)
    )
    """

    if cursor.execute(create_produit):
        print("Table is created successfully")
    else:
        print("Error creating table")

    voiture_data = {
        'dtype': "voiture",
        'lib': 'dacia',
        'prix': 20000,
        'cv': 17,
        'marque': "opel",
        'martricule': "12345",
        'carb': "10"
    }

    insert_voiture = """
    INSERT INTO Produits (dtype, lib, prix, cv, marque, martricule, carb) 
    VALUES (%(dtype)s, %(lib)s, %(prix)s, %(cv)s, %(marque)s, %(martricule)s, %(carb)s)
    """

    pc_data = {
        'dtype': "pc",
        'lib': 'hp',
        'prix': 20000,
        'cv': 17,
        'marque': "hp",
        'proccesseur': "i10",
        'disc': "252",
        'ram': "16"
    }

    insert_pc = """
    INSERT INTO Produits (dtype, lib, prix, cv, marque, proccesseur, disc, ram) 
    VALUES (%(dtype)s, %(lib)s, %(prix)s, %(cv)s, %(marque)s, %(proccesseur)s, %(disc)s, %(ram)s)
    """

    pc_datas = [pc_data for _ in range(5000)]
    voiture_datas = [voiture_data for _ in range(5000)]

    datas = pc_datas + voiture_datas

    start_time = datetime.datetime.now()
    for d in datas:
        if d["dtype"] == "voiture":
            cursor.execute(insert_voiture, d)
        elif d["dtype"] == "pc":
            cursor.execute(insert_pc, d)
        else:
            print("Unknown dtype")

    end_time = datetime.datetime.now()

    elapsed_time = end_time - start_time
    print("Elapsed Time:", elapsed_time)
    start_time2 = datetime.datetime.now()

    # Fetch all rows from the "Produits" table
    cursor.execute("SELECT * FROM Produits")
    rows = cursor.fetchall()

    # Display all rows
    for row in rows:
        print(row)

    end_time2 = datetime.datetime.now()

    # Calculate elapsed time
    elapsed_time = end_time2 - start_time2
    print("Elapsed Time for Displaying Rows:", elapsed_time)
    connection.commit()
except Exception as e:
    print("Error connecting to MySQL database:", str(e))
finally:
    if 'cursor' in locals():
        cursor.close()
    if connection.is_connected():
        connection.close()
        print("Connection closed")
