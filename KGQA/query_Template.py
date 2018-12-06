#coding:utf-8
import kg_query as kg

class query_Template(object):
    def __init__(self):
        self.kg_query = kg.neo4j_graph()

    def __cypher2json(self,cypher_text):
        query_result = self.kg_query.data(cypher_text)
        value = []
        [value.append(item[key].encode('utf-8')) for item in query_result for key in item]
        return value
    def __cooperation_action__(self,query):
        name1 = query[2]
        name2 = query[3]
        cypher_text ="""
        match (n:Movie),(m:Person {{person_name:'{first_name}'}}),(p:Person {{person_name:'{second_name}'}})\
        where (m) -[:ACTIVE_IN]->(n) and (p) -[:ACTIVE_IN]->(n) return n.movie_title
        """.format(first_name=name1,second_name=name2)
        value = self.__cypher2json(cypher_text)
        result ="".join(query[2:])+ "、".join(value)
        return result

    def __single_action__(self,query):
        name = query[2]
        cypher_text ="""
        match (n:Movie),(m:Person {{person_name:'{p_name}'}}) where (m) -[:ACTIVE_IN]->(n) return n.movie_title
        """.format(p_name=name)
        value = self.__cypher2json(cypher_text)
        result ="".join(query[2:])+ "、".join(value)
        return result

    def __request_date__(self,query):
        name = query[2]

        cypher_text ="""
        match (n:Movie {{movie_title:'{movie_name}'}}) return n.movie_release_date
        """.format(movie_name=name)
        value = self.__cypher2json(cypher_text)
        if value==[]:
            result = "没找到答案"
            return result
        else:
            result ="".join(query[2:])+ str(value[0].decode('utf-8').encode('utf-8'))
            return result

    def __request_score__(self,query):
        name = query[2]
        cypher_text ="""
        match (n:Movie {{movie_title:'{movie_name}'}}) return n.movie_rating
           """.format(movie_name=name)
        query_result = self.kg_query.data(cypher_text)
        value = []
        [value.append((item[key])) for item in query_result for key in item]
        if value==[]:
            result = "没找到答案"
            return result
        else:
            result =str(value[0])
            return result

    def __request_introduction__(self,query):
        name = query[2]
        cypher_text ="""
        Match (n:Movie {{movie_title:'{movie_name}'}}) return n.movie_introduction
        """.format(movie_name=name)
        value = self.__cypher2json(cypher_text)
        if value==[]:
            result = "没找到答案"
            return result
        else:
            result =str(value[0].decode('utf-8').encode('utf-8'))
            return result

    def __request_movie_actors__(self,query):
        name = query[2]
        cypher_text ="""
        MATCH (m:Movie {{movie_title:'{movie_name}'}}) , (p:Person) where (p)-[:ACTIVE_IN]-(m) RETURN p.person_name
        """.format(movie_name=name)
        value = self.__cypher2json(cypher_text)
        result ="、".join(value)
        return result

    def kg_query_api(self,query):
        query_index = int(query[1])
        if query_index==0 :
           result = self.__cooperation_action__(query)
        elif query_index==1 :
           result = self.__single_action__(query)
        elif query_index==2 :
           result = self.__request_score__(query)
        elif query_index==3 :
           result = self.__request_introduction__(query)
        elif query_index==4:
           result = self.__request_date__(query)
        elif query_index==5 :
           result = self.__request_movie_actors__(query)
        else:
            result =  "None"
        return result

