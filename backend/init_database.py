import sqlite3



if __name__ == '__main__':
    conn = sqlite3.connect('clickdown.db')
    c = conn.cursor()

    query = 'drop table if exists users'
    c.execute(query)
    query = 'drop table if exists tasks'
    c.execute(query)
    query = 'drop table if exists friend_requests'
    c.execute(query)
    query = 'drop table if exists friend_list'
    c.execute(query)
    
    # create table users
    query = """
            CREATE TABLE IF NOT EXISTS users (
                id              integer     primary key,
                username        text        unique not null,
                password        text        not null,
                email           text        unique not null,
                first_name      text        not null,
                last_name       text        not null,
                phone_number    text        not null,
                company         text        ,
                recovery        integer
            );
            """
    c.execute(query)

    # create table tasks
    query = """
            CREATE TABLE IF NOT EXISTS tasks (
                id              integer     primary key,
                owner           integer     not null,
                title           text        not null,
                description     text        not null,
                creation_date   text        not null,
                deadline        text        ,
                labels          text        ,
                current_state   text        not null,
                progress        integer     ,
                time_estimate   integer     ,
                difficulty      text        ,
                foreign key     (owner)     references users (id)
            );
            """
    c.execute(query)
    
    # create friend lists
    query = """
            CREATE TABLE IF NOT EXISTS friend_requests (
                user_from       integer     not null,
                user_to         integer     not null,
                foreign key     (user_from) references users (id),
                foreign key     (user_to)   references users (id),
                constraint      connection  primary key (user_from, user_to)
            );
            """
    c.execute(query)
    
    query = """
            CREATE TABLE IF NOT EXISTS friend_list (
                user_a          integer     not null,
                user_b          integer     not null,
                foreign key     (user_a)    references users (id),
                foreign key     (user_b)    references users (id),
                constraint      connection  primary key (user_a, user_b)
            );
            """
    
    c.execute(query)
    
    conn.commit()

    # insert test data
    query = f"""
            INSERT INTO users (username, password, email, first_name, last_name, phone_number, company)
            VALUES ('charles', '123456Qq', '1105282259@qq.com', 'Yue', 'Qi', '12345', '123');
            """
    c.execute(query)
    
    query = f"""
                INSERT INTO users (username, password, email, first_name, last_name, phone_number, company)
                VALUES ('gavin', 'Testing123', '1@gmail.com', 'Gavin', 'Wang', '54321', '321');
                """
    c.execute(query)
    
    conn.commit()
    c.close()
    conn.close()