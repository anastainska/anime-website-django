import psycopg2
# from config import config

import csv


def parse_file(csv_file):
    reader = csv.reader(csv_file)

    sql_user = """INSERT INTO yummy_user(id, password, email, role)
             VALUES(%s, %s, %s, %s) RETURNING email;"""
    sql_anime = """INSERT INTO yummy_anime(id, title, year, genre, popularity, seasons, description)
            VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING title;"""
    sql_media = """INSERT INTO yummy_mediafile(id, runtime, id_anime_id, video)
               VALUES(%s, %s, %s, %s) RETURNING video;"""
    sql_subscriber = """INSERT INTO yummy_subscriber(user_ptr_id, username, date_of_birth, date_joined, last_login,
                    is_admin, is_active, is_staff, is_superuser)
                   VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING username;"""
    sql_admin = """INSERT INTO yummy_admin(user_ptr_id, admin_name)
                       VALUES(%s, %s) RETURNING admin_name;"""
    sql_folder = """INSERT INTO yummy_folder(id, name, colour, id_subscriber_id)
                           VALUES(%s, %s, %s, %s) RETURNING name;"""
    sql_folder_anime = """INSERT INTO yummy_folder_id_anime(id, folder_id, anime_id)
                               VALUES(%s, %s, %s) RETURNING id;"""
    delete_user = """truncate yummy_user cascade;"""
    delete_anime = """truncate yummy_anime cascade;"""
    delete_media = """truncate yummy_mediafile cascade;"""
    delete_subscriber = """truncate yummy_subscriber cascade;"""
    delete_admin = """truncate yummy_admin cascade;"""
    delete_folder = """truncate yummy_folder cascade;"""
    delete_folder_anime = """truncate yummy_folder_id_anime cascade;"""

    conn = psycopg2.connect(user="postgres",
                            password="Iamcrowley666",
                            host="localhost",
                            port="5432",
                            database="yummy_db",)

    try:
        cur = conn.cursor()
        cur.execute(delete_user)
        cur.execute(delete_anime)
        cur.execute(delete_media)
        cur.execute(delete_subscriber)
        cur.execute(delete_admin)
        cur.execute(delete_folder)
        cur.execute(delete_folder_anime)
        conn.commit()
        for row in reader:
            if row[0] == "User":
                cur.execute(sql_user, (row[1], row[2], row[3], row[4]))
                conn.commit()
                print(row)
            if row[0] == "Anime":
                cur.execute(sql_anime, (row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                conn.commit()
                print(row)
            if row[0] == "Media":
                cur.execute(sql_media, (row[1], row[2], row[3], row[4]))
                conn.commit()
                print(row)
            if row[0] == "Subscriber":
                cur.execute(sql_subscriber, (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                conn.commit()
                print(row)
            if row[0] == "Admin":
                cur.execute(sql_admin, (row[1], row[2]))
                conn.commit()
                print(row)
            if row[0] == "Folder":
                cur.execute(sql_folder, (row[1], row[2], row[3], row[4]))
                conn.commit()
                print(row)
            if row[0] == "Folder_Anime":
                cur.execute(sql_folder_anime, (row[1], row[2], row[3]))
                conn.commit()
                print(row)
        # cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    # for row in reader:
    #     if row:
    #         try:
    #             cur = conn.cursor()
    #             cur.execute(delete)
    #             cur.execute(sql, (row[0], row[1]))
    #             conn.commit()
    #             cur.close()
    #             # conn.cursor()
    #         except (Exception, psycopg2.DatabaseError) as error:
    #             print(error)
    #         finally:
    #             if conn is not None:
    #                 conn.close()
    #         print(row)
    #     else:
    #         print(1111)


with open('Resources/file.csv', 'r') as csv_file:
    parse_file(csv_file)


# import psycopg2
# import csv
#
#
# def parse_file(csv_file):
#     reader = csv.reader(csv_file)
#
#     for row in reader:
#         try:
#             if "zalupa":
#                 connection = psycopg2.connect(user="postgres",
#                                               password="Iamcrowley666",
#                                               host="localhost",
#                                               port="5432",
#                                               database="yummy_db")
#                 cursor = connection.cursor()
#
#                 postgres_insert_query = """INSERT INTO yummy_mediafile(id, runtime, id_anime_id, video)
#                           VALUES(%s, %s, %s, %s);"""
#
#                 cursor.execute(postgres_insert_query, (row[0], row[1], row[2], row[3]))
#
#                 connection.commit()
#                 count = cursor.rowcount
#                 print(count, "Record inserted successfully into table")
#             else:
#                 connection = psycopg2.connect(user="postgres",
#                                               password="Iamcrowley666",
#                                               host="localhost",
#                                               port="5432",
#                                               database="yummy_db")
#                 cursor = connection.cursor()
#
#                 postgres_insert_query = """INSERT INTO yummy_anime(id, title, year, genre, popularity, seasons, description)
#                                          VALUES(%s, %s, %s, %s, %s, %s, %s);"""
#
#                 cursor.execute(postgres_insert_query, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
#
#                 connection.commit()
#                 count = cursor.rowcount
#                 print(count, "Record inserted successfully into table")
#
#         except (Exception, psycopg2.Error) as error:
#             # meow = """select pg_typeof(*) from yummy_anime;"""
#             # print(cursor.execute(meow))
#             print("Failed to insert record into table", type(error), error)
#
#         finally:
#             if connection:
#                 cursor.close()
#                 connection.close()
#                 print("PostgreSQL connection is closed")
#         print(row)
#
#
# with open('Resources/file.csv', 'r') as csv_file:
#     parse_file(csv_file)
