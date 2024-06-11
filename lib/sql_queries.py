# Select all female bears and return their name and age
select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""

# Select all bears' names and orders them alphabetically
select_all_bears_names_alphabetically = """
    SELECT
        bears.name
    FROM bears
    ORDER BY bears.name ASC;
"""

# Select all bears' names and ages that are alive and order them by age
select_all_alive_bears_return_name_and_age_order_by_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE alive=1
    ORDER BY bears.age ASC;
"""

# Select the oldest bear and return its name and age
select_oldest_bear_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    ORDER BY bears.age DESC
    LIMIT 1;
"""

# Select the youngest bear and return its name and age
select_youngest_bear_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    ORDER BY bears.age ASC
    LIMIT 1;
"""

# Select the bear with the name "Sergeant Brown" and return all columns
select_sergeant_brown_return_all_columns = """
    SELECT *
    FROM bears
    WHERE name='Sergeant Brown';
"""

# Select all bears that are alive and order them by temperament
select_all_alive_bears_order_by_temperament = """
    SELECT *
    FROM bears
    WHERE alive=1
    ORDER BY temperament;
"""
