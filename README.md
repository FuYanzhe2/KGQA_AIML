# KGQA_AIML
#编译环境：python2.7 windows

#Chatbot1.0实现功能：
1.简单人机对话
2.基于电影知识图谱的知识问答

原理：AIML人工智能标记语言（模板方式）

相关包：

1.pip install aiml
	注意：直接安装英文包，在进行模板匹配时先分词再转为utf-8模式进行模板匹配，
    不需要安装pyaiml的中文版，否则在模板匹配时，arsi命令是以单个字的模式进行匹配的，会增加写模板的难度
2.pip install jieba
	导入词典，从mysql数据库中获得
3.pip install py2neo
	neo4j图数据库的访问借口

目录结构：
QA
    KGQA
        __init__.py
        kg_query.py
        query_Template.py
        word_seg.py
    Template
        AIML启动文件和相关模板文件
        kg.aiml知识图谱查询模板
    dictionary
    cfg.info
    main.py
    mysql2neo4j.py.................................将mysql导入neo4j，不要用手工导，数据格式不好调，会出错
    Readme.txt.................................工程说明文档
    Cyphter.txt................................图数据库查询语句

功能：
KGQA支持查询的问题（提问模式不唯一）：
（1）.单人电影查询：
    章子怡演过什么电影？
（2）.双人电影查询：
    周星驰和巩俐合作过什么电影？
（3）.电影评分查询：
    夜宴这部电影多少分？
（4）.电影介绍查询：
    功夫讲的什么
（5）.电影上映日期查询
（6）.电影主要演员查询

代码详细说明及实现原理见博客：https://www.jianshu.com/p/e7d100cd87b1

