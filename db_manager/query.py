def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]



CREATE_USER_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS user
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            email VARCHAR(300),
            phone_number VARCHAR(15),
            skills TEXT,
            created_at DATETIME,
            updated_at DATETIME,
            file_path VARCHAR(500),
            category_id INTEGER,
            system_validated BOOLEAN,
            user_validated BOOLEAN
        );
"""

CREATE_SKILLS_CATEGORY_TABLE = """
    CREATE TABLE IF NOT EXISTS category
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(300),
            description TEXT
        );
"""

CREATE_SKILLS_TABLE = """
    CREATE TABLE IF NOT EXISTS skill
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            description TEXT,
            category_id INTEGER
        );
"""

INSERT_USER_QUERY = """
    INSERT INTO user
        (
                    name,
                    email,
                    phone_number,
                    skills,
                    file_path,
                    system_validated
        )
        VALUES
        (
                    '%(name)s',
                    '%(email)s',
                    '%(phone)s',
                    '%(skills)s',
                    '%(file_path)s',
                    '%(system_validated)s'
        );
"""

FETCH_USER_QUERY = "SELECT * from user;"

DELETE_USER_QUERY = "DELETE FROM user WHERE id = '%(id)s';"

SELECT_ALL_QUERY = "SELECT count(id) as total from user;"
SELECT_VALIDATED_QUERY = "SELECT count(id) as completed from user where user_validated != null or user_validated != False;"
SELECT_NOT_VALIDATED_QUERY = "SELECT count(id) as pending from user where user_validated = False or user_validated IS NULL;"

SELECT_PIE_DATA = "select c.name, count(c.name) as total from user inner join category c where user.category_id = c.id GROUP by c.name;"

INSERT_CATEGORY_QUERY = """
INSERT INTO category (name) values('%(name)s');
"""