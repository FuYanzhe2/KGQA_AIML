Cypher 语句编号说明

[1].查询演员合作的电影
 cypher_text ="""
        match (n:Movie),(m:Person {{person_name:'{first_name}'}}),(p:Person {{person_name:'{second_name}'}})\
        where (m) -[:ACTIVE_IN]->(n) and (p) -[:ACTIVE_IN]->(n) return n.movie_title
        """.format(first_name=name1,second_name=name2)

[2].查询单个演员合作的作品
cypher_text ="""
        match (n:Movie),(m:Person {{person_name:'{p_name}'}}) where (m) -[:ACTIVE_IN]->(n) return n.movie_title
        """.format(p_name=name)

[3].电影评分
 cypher_text ="""
        match (n:Movie {{movie_title:'{movie_name}'}}) return n.movie_rating
           """.format(movie_name=name)

[4].电影介绍
cypher_text ="""
        Match (n:Movie {{movie_title:'{movie_name}'}}) return n.movie_introduction
        """.format(movie_name=name)

[5].电影上映日期
cypher_text ="""
        match (n:Movie {{movie_title:'{movie_name}'}}) return n.movie_release_date
        """.format(movie_name=name)

[6].电影参演明星
cypher_text ="""
    MATCH (m:Movie {{movie_title:'{movie_name}'}}) , (p:Person) where (p)-[:ACTIVE_IN]-(m) RETURN p.person_name
    """.format(movie_name=name)