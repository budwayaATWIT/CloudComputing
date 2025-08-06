import mysql.connector

# Connect to MySQL inside the container
conn = mysql.connector.connect(
    host="localhost",
    port=3306,  
    user="mgs_user",
    password="pa55word",
    database="my_guitar_shop"
)
cursor = conn.cursor()

# Load queries from the SQL file
with open("init/guitar_shop_queries.sql") as f:
    queries = [q.strip() for q in f.read().split(';') if q.strip()]

def menu():
    print("\nSQL Query Driver : Select a query to run:\n")
    for i, q in enumerate(queries, 1):
        preview = q.split('\n')[0][:60].replace('\n', ' ')
        print(f"{i}. {preview}...")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("\nEnter a query number to execute (or 0 to exit): ")
        if choice == "0":
            break
        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(queries):
                print("Invalid selection.")
                continue
            query = queries[idx]
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("Query executed successfully (no results returned).")
        except Exception as e:
            print(f"Error: {e}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
