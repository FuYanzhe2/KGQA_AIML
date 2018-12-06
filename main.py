#coding:utf-8
import os
import aiml

from KGQA import query_Template as q_T
from KGQA import word_seg as seg
# The Kernel object is the public interface to
# the AIML interpreter.

word_Seg = seg.jieba_seg()
q_Template = q_T.query_Template()
# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
fyz_bot = aiml.Kernel()
print("The current path : "+os.path.split(os.path.realpath(__file__))[0])
fyz_bot.learn(os.path.split(os.path.realpath(__file__))[0]+"/Template/std-startup.xml")

"""
fyz_bot.learn(os.path.split(os.path.realpath(__file__))[0] + "/Template/bye.aiml")
fyz_bot.learn(os.path.split(os.path.realpath(__file__))[0] + "/Template/tools.aiml")
fyz_bot.learn(os.path.split(os.path.realpath(__file__))[0] + "/Template/bad.aiml")
fyz_bot.learn(os.path.split(os.path.realpath(__file__))[0] + "/Template/funny.aiml")
fyz_bot.learn(os.path.split(os.path.realpath(__file__))[0] + "/Template/OrdinaryQuestion.aiml")
fyz_bot.learn(os.path.split(os.path.realpath(__file__))[0] + "/Template/Common conversation.aiml")
"""
# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
fyz_bot.respond("load fyz bot")

# Loop forever, reading user input from the command
# line and printing responses.
print(u"你好我是Chimp wood:\n")
while True:
    input_message = raw_input("Enter your message >>")
    if len(input_message)>60:
        print fyz_bot.respond(u"句子长度过长")
        continue

    elif input_message.strip() == '':
        print fyz_bot.respond(u"无")
        continue
    if input_message == 'q':
        exit()
    else:
        input_message = word_Seg.wordSegment(input_message)
        #print(input_message.encode('utf-8'))
        response = fyz_bot.respond(input_message)
        if response == "":
            ans = fyz_bot.respond(u'找不到答案')
        #response以#调用电影知识库问答
        elif response[0]=="%":
            query_list = response.replace(" ","").split("%")
            response = q_Template.kg_query_api(query_list)
            print(response)
        #号开头说明没有匹配到答案
        elif response.__contains__("NoMatchingTemplate"):
            pass
        else:
            print(response)
        #开始从neo4j中搜寻答案



















