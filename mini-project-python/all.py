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
    CREATE TABLE IF NOT EXISTS Produits2 (
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
        'lib': 'dacia',
        'prix': 7000,
        'cv': 17,
        'marque': "dacia",
        'martricule': "12345",
        'carb': "10"
    }

    insert_voiture = """
    INSERT INTO Produits2 (lib, prix, cv, marque, martricule, carb) 
    VALUES (%(lib)s, %(prix)s, %(cv)s, %(marque)s, %(martricule)s, %(carb)s)
    """

    pc_data = {
        'lib': 'hp',
        'prix': 70000,
        'cv': 0,  # Add this line for PCs
        'marque': "hp",
        'proccesseur': "i9",
        'disc': "252",
        'ram': "16"
    }

    insert_pc = """
    INSERT INTO Produits2 (lib, prix, cv, marque, proccesseur, disc, ram) 
    VALUES (%(lib)s, %(prix)s, %(cv)s, %(marque)s, %(proccesseur)s, %(disc)s, %(ram)s)
    """

    pc_datas = [pc_data for _ in range(5000)]
    voiture_datas = [voiture_data for _ in range(5000)]

    datas = pc_datas + voiture_datas

    start_time = datetime.datetime.now()
    for d in datas:
        if d['cv'] > 0:
            cursor.execute(insert_voiture, d)
        else:
            cursor.execute(insert_pc, d)

    end_time = datetime.datetime.now()

    elapsed_time = end_time - start_time
    print("Elapsed Time for Inserting Rows:", elapsed_time)

    start_time2 = datetime.datetime.now()

    # Fetch all rows from the "Produits2" table
    cursor.execute("SELECT * FROM Produits2")
    rows = cursor.fetchall()

    # Display all rows
    for row in rows:
        if row[3] > 0:  # Check if cv is greater than 0 to distinguish between PCs and cars
            print("Voiture : ", row)
        else:
            print("PC : ", row)

    end_time2 = datetime.datetime.now()

    elapsed_time2 = end_time2 - start_time2
    print("Elapsed Time for Displaying Rows:", elapsed_time2)

    connection.commit()
except Exception as e:
    print("Error connecting to MySQL database:", str(e))
finally:
    if 'cursor' in locals():
        cursor.close()
    if connection.is_connected():
        connection.close()
        print("Connection closed")
