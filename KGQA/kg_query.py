#coding:utf-8
import ConfigParser
from py2neo import Graph

class neo4j_graph(object):
    def __init__(self):
        conf = ConfigParser.ConfigParser()
        neo4j_info = self.read_config_file(conf,db = "neo4j")
        self.neo_graph = self.creat_neo4j_graph(neo4j_info)

    def read_config_file(self,conf,db):
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
    def creat_neo4j_graph(self,neo4j_info):
        host,port,bolt,dbname,user_name,password = neo4j_info
        neo_graph = Graph(
            host = host,
            http_port =int(port),
            bolt_port=int(bolt),
            username=dbname,
            password=password
        )
        return neo_graph
    def run(self,query):
        kg_result = self.neo_graph.run(query)
        return kg_result
    def data(self,query):
        kg_result = self.neo_graph.data(query)
        return kg_result



