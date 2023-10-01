create_cow_table = """
    create table cow (
        id INT PRIMARY KEY,
        nickname VARCHAR(50),
        age INT
    );
"""

create_milk_yield_table = """
    create table milk_yield (
    	cow_id INT,
    	date DATE,
    	gallons DECIMAL(2,1),
        PRIMARY KEY (cow_id, date),
        FOREIGN KEY (cow_id) REFERENCES cow(cow_id)
            ON UPDATE CASCADE
            ON DELETE RESTRICT
    );
"""
