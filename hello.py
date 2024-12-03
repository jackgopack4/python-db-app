import psycopg

def main():
    with psycopg.connect("dbname=postgres user=postgres host=localhost password=mysecretpassword port=5432") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Check if the table 'users' exists
            cur.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = 'users'
                );
            """)
            table_exists = cur.fetchone()[0]

            if not table_exists:
                # Execute a command: this creates a new table
                cur.execute("""
                    CREATE TABLE users (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100),
                        email VARCHAR(100) UNIQUE
                    )
                """)
                cur.execute("""
                    INSERT INTO users (name, email) VALUES
                        ('Alice Johnson', 'alice.johnson@example.com'),
                        ('Bob Smith', 'bob.smith@example.com'),
                        ('Charlie Brown', 'charlie.brown@example.com'),
                        ('David Wilson', 'david.wilson@example.com'),
                        ('Eva Green', 'eva.green@example.com'),
                        ('Frank White', 'frank.white@example.com'),
                        ('Grace Lee', 'grace.lee@example.com'),
                        ('Hannah Scott', 'hannah.scott@example.com'),
                        ('Ian Black', 'ian.black@example.com'),
                        ('Jane Doe', 'jane.doe@example.com')
                """)

            # Query the database and obtain data as Python objects.
            cur.execute("SELECT * FROM users")
            firstuser = cur.fetchone()
            print(firstuser)

            # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
            # of several records, or even iterate on the cursor
            for record in cur:
                print(record)

            # Make the changes to the database persistent
            conn.commit()

if __name__ == '__main__':
    main()
