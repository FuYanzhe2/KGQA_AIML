## KGQA_AIML
编译环境：python2.7 windows

Chatbot1.0实现功能：<br>    
    1.简单人机对话<br>   
    2.基于电影知识图谱的知识问答<br>   

原理：AIML人工智能标记语言（模板方式）

相关包:<br>  
	1.pip install aiml<br>   
	注意：直接安装英文包，在进行模板匹配时先分词再转为utf-8模式进行模板匹配，<br>   
    	不需要安装pyaiml的中文版，否则在模板匹配时，arsi命令是以单个字的模式进行匹配的，会增加写模板的难度<br>   
	
	2.pip install jieba<br>   
	导入词典，从mysql数据库中获得<br> 
	
	3.pip install py2neo<br>   
	neo4j图数据库的访问借口<br>   

功能：<br>   
KGQA支持查询的问题（提问模式不唯一）：<br>   
（1）.单人电影查询：<br>   
    章子怡演过什么电影？<br>   
（2）.双人电影查询：<br>   
    周星驰和巩俐合作过什么电影？<br>   
（3）.电影评分查询：<br>   
    夜宴这部电影多少分？<br>   
（4）.电影介绍查询：<br>   
    功夫讲的什么<br>   
（5）.电影上映日期查询<br>   
（6）.电影主要演员查询<br>   

代码详细说明及实现原理见[博客](https://www.jianshu.com/p/e7d100cd87b1)
