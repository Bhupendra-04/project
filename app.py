import pymysql

def create_connection():
    return pymysql.connect(
        host='host.docker.internal',   # Docker me ho to 'mysqldb'
        user='root',
        password='root',
        database='user_info'
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        )
    ''')
    connection.commit()
    cursor.close()

def insert_name(connection, name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    connection.commit()
    cursor.close()

    with open("servers.txt", "a") as file:
        file.write(name + "\n")

def fetch_all_usernames(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM users")
    usernames = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return usernames

def main():
    connection = create_connection()
    create_table(connection)

    while True:
        print("\n1. Insert name")
        print("2. Fetch all usernames")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            insert_name(connection, name)
            print("Name inserted successfully.")

        elif choice == "2":
            usernames = fetch_all_usernames(connection)

            if usernames:
                print("All usernames:")
                for name in usernames:
                    print(name)
            else:
                print("No usernames found.")

        elif choice == "3":
            print("Goodbye")
            connection.close()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()