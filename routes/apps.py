from django.apps import AppConfig

class RoutesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'routes'


    def ready(self):
        import psycopg2
        import pandas as pd


        connection = psycopg2.connect(user="kscyvqirfqjevw",
                                    password="2037f31777df5afc16122fd3fc6a2e8b98a189dba7f5cbfd124977f2d99f9980",
                                    host="ec2-34-235-198-25.compute-1.amazonaws.com",
                                    port="5432",
                                    database="d2no4bighl8610")

        cursor = connection.cursor()

        cursor.execute("TRUNCATE routes_rutas, routes_poi RESTART IDENTITY")
        df_routes = pd.read_csv('routes/data/routes.csv')
        insert_query = f"""INSERT INTO routes_rutas(name,
                    esp_resume,
                    eng_resume,
                    val_resume,
                    duration,
                    dificulty,
                    start,
                    end_point,
                    image,
                    url,
                    transport,
                    type,
                    esp_description,
                    val_description,
                    eng_description) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor.executemany(insert_query, df_routes.values)
        print("\x1b[1;32m"+"-------------------Populate Routes OK------------------------"+"\033[0;m")

        df_poi = pd.read_csv('routes/data/poi.csv')
        insert_query2 = f"""INSERT INTO routes_poi(route_id,
                    name,
                    lat,
                    lon,
                    val_description,
                    cast_description,
                    eng_description,
                    images) values (%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor.executemany(insert_query2, df_poi.values)
        connection.commit()
        print("\x1b[1;32m"+"-------------------Populate POI OK------------------------"+"\033[0;m")

        if (connection):
            cursor.close()
            connection.close()
        print("\x1b[1;32m"+"-------------------Populate Tables OK------------------------"+"\033[0;m")