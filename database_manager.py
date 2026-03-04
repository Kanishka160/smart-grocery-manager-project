import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="smart_grocery_db",
        user="postgres",
        password="Kanishka",
        port="5432"
    )

def setup_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price NUMERIC(10, 2) NOT NULL
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()
