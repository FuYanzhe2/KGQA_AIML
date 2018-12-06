#coding:utf-8
#访问mysql数据并载入到neo4j
import pymysql
import ConfigParser
from py2neo import Graph,Node,Relationship
import requests
import json
conf = ConfigParser.ConfigParser()


def read_config_file(conf,db):
    conf.read("cfg.info")
    host = conf.get(db, "host")
    port = conf.get(db, "port")
    dbname = conf.get(db, "dbname")
    user_name = conf.get(db, "user_name")
    password = conf.get(db, "password")
    if db=="neo4j":
        bolt = conf.get(db, "bolt")
        return [host,port,bolt,dbname,user_name,password]
    else:
        return [host,port,dbname,user_name,password]

def read_sql_data(db_info,sql_text):
    sql_host,sql_port,sql_dbname,sql_user_name,sql_password = db_info
    conn = pymysql.connect(
            host=sql_host,
            port=int(sql_port),
            user=sql_user_name,
            passwd=sql_password,
            db=sql_dbname,
            charset='utf8',
        )
    cur = conn.cursor()
    cur.execute(sql_text)
    col_name = cur.description
    word_list = cur.fetchall()
    return col_name,word_list

def creat_neo4j_graph(neo4j_info):
    host,port,bolt,dbname,user_name,password = neo4j_info
    neo_graph = Graph(
        host = host,
        http_port =int(port),
        bolt_port=int(bolt),
        username=dbname,
        password=password
    )
    return neo_graph

def main():
    LOAD_DATA = False
    conf = ConfigParser.ConfigParser()
    sql_info = read_config_file(conf,db = "mysql")
    neo4j_info = read_config_file(conf,db = "neo4j")
    neo_graph = creat_neo4j_graph(neo4j_info)


    if LOAD_DATA:
        neo_graph.delete_all()
        neo_graph.begin()
        #导入genre表
        sql_text = "SELECT * from genre"
        col_name,word_list = read_sql_data(sql_info,sql_text)
        for i in range(len(word_list)):
            node = Node("Catagroy",genre_id = word_list[i][0],genre_name = word_list[i][1])
            neo_graph.merge(node)
        print(u"genre表格导入完成......")

        #导入movie表
        sql_text = "SELECT * from movie"
        col_name,word_list = read_sql_data(sql_info,sql_text)
        for i in range(len(word_list)):
            node = Node("Movie",movie_id = word_list[i][0],movie_title = word_list[i][1],movie_introduction =word_list[i][2]
                        ,movie_rating = word_list[i][3],movie_release_date= word_list[i][4])
            neo_graph.merge(node)
        print(u"movie表格导入完成......")

        #导入movie_to_genre# 表
        sql_text = "SELECT * from movie_to_genre"
        col_name,word_list = read_sql_data(sql_info,sql_text)
        for i in range(len(word_list)):
            node = Node("movie_to_genre",movie_id = word_list[i][0],genre_id = word_list[i][1])
            neo_graph.merge(node)
        print(u"movie_to_genre表格导入完成......")

        #导入person# 表
        sql_text = "SELECT * from person"
        col_name,word_list = read_sql_data(sql_info,sql_text)
        for i in range(len(word_list)):
            if word_list[i][3]==None:
                person_n = word_list[i][4]
            else:
                person_n = word_list[i][3]
            node = Node("Person",person_id = word_list[i][0],person_birth_day = word_list[i][1],person_death_day=word_list[i][2],
                    person_name = person_n,person_biography=word_list[i][5],person_birth_place=word_list[i][6])
            neo_graph.merge(node)
        print(u"person表格导入完成......")

        #导入person_to_movie# 表
        sql_text = "SELECT * from person_to_movie"
        col_name,word_list = read_sql_data(sql_info,sql_text)
        for i in range(len(word_list)):
            node = Node("person_to_movie",person_id = word_list[i][0],movie_id = word_list[i][1])
            neo_graph.merge(node)
        print(u"person_to_movie表格导入完成......")

    #创建PART_OF关系
    cypher_text1 = """
                    MATCH (n:Catagroy),(s:movie_to_genre),(m:Movie)
                    WHERE n.genre_id = s.genre_id AND s.movie_id=m.movie_id
                    Merge (n)-[:PART_OF]->(m)

                """
    neo_graph.run(cypher_text1)
    print(u"PART_OF关系创建完成......")
    #创建ACTIVE_IN关系
    cypher_text2 = """
                    MATCH (k:Person),(p:person_to_movie),(q:Movie)
                    WHERE k.person_id = p.person_id AND p.movie_id=q.movie_id
                    Merge (k)-[:ACTIVE_IN]->(q)
                """
    neo_graph.run(cypher_text2)
    print(u"ACTIVE_IN关系创建完成......")


if __name__ == "__main__":
    main()

