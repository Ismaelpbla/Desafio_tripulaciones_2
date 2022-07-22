from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def routes(request):
    import psycopg2

    connection = psycopg2.connect(user="kscyvqirfqjevw",
                                password="2037f31777df5afc16122fd3fc6a2e8b98a189dba7f5cbfd124977f2d99f9980",
                                host="ec2-34-235-198-25.compute-1.amazonaws.com",
                                port="5432",
                                database="d2no4bighl8610")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM routes_rutas ORDER BY id;")
    routes = cursor.fetchall()

    rutas = []
    for idx, route in enumerate(routes):
        ruta={}
        ruta['route_id'] = int(route[0])
        ruta['name'] = route[1]
        ruta['difficulty'] = route[6]
        ruta['image'] = route[9]
        ruta['duration'] = route[5]
        ruta['startingPoint'] = route[7]
        ruta['endingPoint'] = route[8]
        ruta['description_es'] = route[13]
        ruta['description_va'] = route[14]
        ruta['description_en'] = route[15]
        ruta['transport'] = route[11]
        ruta['type'] = route[12]
        ruta['url'] = route[10]

        points = []

        cursor = connection.cursor()
        query = f'''SELECT * 
        FROM routes_poi as p
        WHERE p.route_id = {idx+1};'''
        cursor.execute(query)
        pois = cursor.fetchall()

        for poi in pois:
            point={}
            point['poi_id'] = int(poi[0])
            point['name'] = poi[1]
            point['description_es'] = poi[5]
            point['description_va'] = poi[4]
            point['description_en'] = poi[6]
            point['latitude'] = poi[2]
            point['longitude'] = poi[3]
            point['image'] = poi[7]
            points.append(point)

        ruta['poi'] = points
        rutas.append(ruta)

    if (connection):
        cursor.close()
        connection.close()
    return HttpResponse(json.dumps(rutas, ensure_ascii=False), content_type="application/json")

def route_id(request):
    import psycopg2

    connection = psycopg2.connect(user="kscyvqirfqjevw",
                                password="2037f31777df5afc16122fd3fc6a2e8b98a189dba7f5cbfd124977f2d99f9980",
                                host="ec2-34-235-198-25.compute-1.amazonaws.com",
                                port="5432",
                                database="d2no4bighl8610")

    cursor = connection.cursor()

    id = int(request.GET.get('id', '1'))
    query_rutas = f"SELECT id FROM routes_rutas;"
    query_ruta = f"SELECT * FROM routes_rutas WHERE id = {id};"
    query_poi = "SELECT * FROM routes_poi;"

    cursor.execute(query_rutas)
    index = cursor.fetchall()

    ruta={}
    if (id,) in index:
        cursor.execute(query_ruta)
        route = cursor.fetchall()
        cursor.execute(query_poi)
        pois = cursor.fetchall()

        ruta['route_id'] = int(route[0][0])
        ruta['name'] = route[0][1]
        ruta['difficulty'] = route[0][6]
        ruta['image'] = route[0][9]
        ruta['duration'] = route[0][5]
        ruta['startingPoint'] = route[0][7]
        ruta['endingPoint'] = route[0][8]
        ruta['description_es'] = route[0][13]
        ruta['description_va'] = route[0][14]
        ruta['description_en'] = route[0][15]
        ruta['transport'] = route[0][11]
        ruta['type'] = route[0][12]
        ruta['url'] = route[0][10]

        points = []

        cursor = connection.cursor()
        query = f'''SELECT * FROM routes_poi WHERE route_id = {id};'''
        cursor.execute(query)
        pois = cursor.fetchall()

        for poi in pois:
            point={}
            point['poi_id'] = int(poi[0])
            point['name'] = poi[1]
            point['description_es'] = poi[5]
            point['description_va'] = poi[4]
            point['description_en'] = poi[6]
            point['latitude'] = poi[2]
            point['longitude'] = poi[3]
            point['image'] = poi[7]
            points.append(point)

        ruta['poi'] = points
        
    else:
        ruta['error'] = 'ID not found'

    if (connection):
        cursor.close()
        connection.close()

    return HttpResponse(json.dumps(ruta, ensure_ascii=False), content_type="application/json")

def poi(request):
    import psycopg2

    connection = psycopg2.connect(user="kscyvqirfqjevw",
                                password="2037f31777df5afc16122fd3fc6a2e8b98a189dba7f5cbfd124977f2d99f9980",
                                host="ec2-34-235-198-25.compute-1.amazonaws.com",
                                port="5432",
                                database="d2no4bighl8610")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM routes_poi ORDER BY id;")
    pois = cursor.fetchall()

    points = []
    for poi in pois:
        point={}
        point['poi_id'] = int(poi[0])
        point['name'] = poi[1]
        point['description_es'] = poi[5]
        point['description_va'] = poi[4]
        point['description_en'] = poi[6]
        point['latitude'] = poi[2]
        point['longitude'] = poi[3]
        point['image'] = poi[7]
        points.append(point)

    if (connection):
        cursor.close()
        connection.close()
    return HttpResponse(json.dumps(points, ensure_ascii=False), content_type="application/json")

def poi_id(request):
    import psycopg2

    connection = psycopg2.connect(user="kscyvqirfqjevw",
                                password="2037f31777df5afc16122fd3fc6a2e8b98a189dba7f5cbfd124977f2d99f9980",
                                host="ec2-34-235-198-25.compute-1.amazonaws.com",
                                port="5432",
                                database="d2no4bighl8610")

    id = int(request.GET.get('id', '1'))
    cursor = connection.cursor()

    query = f'''SELECT * FROM routes_poi WHERE id = {id};'''
    cursor.execute(query)
    poi = cursor.fetchall()

    cursor.execute("SELECT id FROM routes_poi;")
    index = cursor.fetchall()
    point={}
    
    if (id,) in index:

        point['poi_id'] = int(poi[0][0])
        point['name'] = poi[0][1]
        point['description_es'] = poi[0][5]
        point['description_va'] = poi[0][4]
        point['description_en'] = poi[0][6]
        point['latitude'] = poi[0][2]
        point['longitude'] = poi[0][3]
        point['image'] = poi[0][7]

    else:
        point['error'] = 'ID not found'

    if (connection):
        cursor.close()
        connection.close()

    return HttpResponse(json.dumps(point, ensure_ascii=False), content_type="application/json")

# def populate(request):
#     import psycopg2
#     import pandas as pd

#     connection = psycopg2.connect(user="kscyvqirfqjevw",
#                                 password="2037f31777df5afc16122fd3fc6a2e8b98a189dba7f5cbfd124977f2d99f9980",
#                                 host="ec2-34-235-198-25.compute-1.amazonaws.com",
#                                 port="5432",
#                                 database="d2no4bighl8610")
#     cursor = connection.cursor()

#     df_routes = pd.read_csv('routes/data/routes.csv', index_col=0)
#     insert_query = f"""INSERT INTO routes_rutas(name,
#                 esp_resume,
#                 eng_resume,
#                 val_resume,
#                 duration,
#                 dificulty,
#                 start,
#                 end_point,
#                 image,
#                 url,
#                 transport,
#                 type,
#                 esp_description,
#                 val_description,
#                 eng_description) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#     cursor.executemany(insert_query, df_routes.values)
#     connection.commit()

#     df_poi = pd.read_csv('routes/data/poi.csv', index_col=0)
#     insert_query2 = f"""INSERT INTO routes_poi(route_id,
#                 name,
#                 lat,
#                 lon,
#                 val_description,
#                 cast_description,
#                 eng_description) values (%s,%s,%s,%s,%s,%s,%s)"""

#     cursor.executemany(insert_query2, df_poi.values)
#     connection.commit()

#     if (connection):
#         cursor.close()
#         connection.close()
#     return HttpResponse(["Maldito Friki"])
