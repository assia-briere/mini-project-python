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

    # Create the 'Produits' table
    create_produits = """
    CREATE TABLE IF NOT EXISTS Produits3 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        lib VARCHAR(255),
        prix INT
    )
    """

    # Create the 'PC' table with a foreign key to 'Produits'
    create_pc = """
    CREATE TABLE IF NOT EXISTS PC (
        id INT AUTO_INCREMENT PRIMARY KEY,
        marque VARCHAR(255),
        proccesseur VARCHAR(255),
        disc VARCHAR(255),
        ram VARCHAR(255),
        produit_id INT,
        FOREIGN KEY (produit_id) REFERENCES Produits3(id)
    )
    """

    # Create the 'Voiture' table with a foreign key to 'Produits'
    create_voiture = """
    CREATE TABLE IF NOT EXISTS Voiture (
        id INT AUTO_INCREMENT PRIMARY KEY,
        cv INT,
        marque VARCHAR(255),
        martricule VARCHAR(255),
        carb VARCHAR(255),
        produit_id INT,
        FOREIGN KEY (produit_id) REFERENCES Produits3(id)
    )
    """

    # Execute table creation queries
    cursor.execute(create_produits)
    cursor.execute(create_pc)
    cursor.execute(create_voiture)

    connection.commit()
    print("Tables are created successfully")
    insert_pc = """
        INSERT INTO PC (marque, proccesseur, disc, ram, produit_id) 
        VALUES (%(marque)s, %(proccesseur)s, %(disc)s, %(ram)s, %(produit_id)s)
        """
    insert_voiture = """
        INSERT INTO Voiture (cv, marque, martricule, carb, produit_id) 
        VALUES (%(cv)s, %(marque)s, %(martricule)s, %(carb)s, %(produit_id)s)
        """
    # Sample data for 'Produits' table
    produits_data =   {'lib': 'Product 1', 'prix': 100}
    produits_datas = [produits_data for _ in range(10000)]
    start_time = datetime.datetime.now()
    # Insert data into 'Produits' table and retrieve the auto-generated IDs
    produit_ids = []
    for data in produits_datas:
        insert_produit = """
        INSERT INTO Produits3 (lib, prix) 
        VALUES (%(lib)s, %(prix)s)
        """
        cursor.execute(insert_produit, data)
        produit_ids.append(cursor.lastrowid)
        connection.commit()
    

    # Sample data for 'PC' and 'Voiture' tables
    pc_data = {'marque': 'HP', 'proccesseur': 'i5', 'disc': '256GB', 'ram': '8GB'}

    pc_datas = [pc_data for _ in range(5000)]
   
    voiture_data = {'cv': 150, 'marque': 'Toyota', 'martricule': '12345', 'carb': '10'}

    voiture_datas = [voiture_data for _ in range(5000)]
    # Insert data into 'PC' table with the corresponding 'Produits' IDs
   
# Insert data into 'PC' table with the corresponding 'Produits' IDs
    for i, data in enumerate(pc_datas):
        data_copy = data.copy()  # Create a copy of the data dictionary
        data_copy['produit_id'] = produit_ids[i]  # Assign the corresponding 'Produits' ID
        cursor.execute(insert_pc, data_copy)
    # print(i, data_copy)

# Insert data into 'Voiture' table with the corresponding 'Produits' IDs
    for i, data in enumerate(voiture_datas):
        data_copy = data.copy()  # Create a copy of the data dictionary
        data_copy['produit_id'] = produit_ids[i + 5000]  # Assign the corresponding 'Produits' ID
        cursor.execute(insert_voiture, data_copy)
    end_time = datetime.datetime.now()

    elapsed_time = end_time - start_time
    print("Elapsed Time for Inserting Rows:", elapsed_time)
    connection.commit()
    print("Data inserted successfully")

except Exception as e:
    print("Error:", str(e))
finally:
    if 'cursor' in locals():
        cursor.close()
    if connection.is_connected():
        connection.close()
        print("Connection closed")
