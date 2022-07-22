def connect_database(user, password, host, port, database):
    import psycopg2

    connection = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database)

    return connection