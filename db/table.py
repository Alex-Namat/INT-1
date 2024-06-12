from db.connection import get_connection
from faker import Faker

fake = Faker()

class TestTable:
    def __init__(self, cust_id, str):
        self.id = cust_id
        self.str = str

    def __str__(self):
        return f"(Id: {self.id}, Str: {self.str})"
    
    def __repr__(self): 
         return f"(Id: {self.id}, Str: {self.str})"
    
    def __hash__(self) -> int:
        return hash((self.id, self.str))
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TestTable):
            return NotImplemented
        return self.id == other.id and self.str == other.str
    

def create():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE test_table (
                    id serial PRIMARY KEY,
                    str VARCHAR NOT NULL)
                """)
            connection.commit()

def generated_rows(num_rows = 100):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            for _ in range(num_rows):
                cursor.execute(
                "INSERT INTO test_table (str) VALUES (%s)", (fake.name(),))
            connection.commit()

def delete():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM test_table")
            connection.commit()

def select_like(pattern = 'A%'):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM test_table WHERE str LIKE %s",  (pattern,))
             
        
def return_select_like(pattern = 'A%') -> list[TestTable]:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM test_table WHERE str LIKE %s",  (pattern,))
            return [TestTable(id, str) for id, str in cursor]
              
def create_index():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE INDEX idx_str ON test_table (str)")
            connection.commit()

def drop_index():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DROP INDEX idx_str")
            connection.commit()