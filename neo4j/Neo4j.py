# pip install py2neo -i https://pypi.tuna.tsinghua.edu.cn/simple 第三方库
# neo4j.bat console

from py2neo import Node, Relationship
from py2neo import Graph, Subgraph
from py2neo import Path
from build_node_relation import DataToNeo4j
import pandas as pd
import csv
import xlrd

test_data = pd.read_excel("鞋子.xls", header=0)


def data_extraction():
    # 节点数据抽取

    # 取出商品名称到list
    node_buy_key = []
    for i in range(0, len(test_data)):
        node_buy_key.append(test_data['商品'][i])
    # 取出商品价格到list
    node_sell_key = []
    for i in range(0, len(test_data)):
        node_sell_key.append(test_data['店铺'][i])

    # 去重
    node_buy_key = list(set(node_buy_key))
    node_sell_key = list(set(node_sell_key))

    # value抽出作node
    node_list_value = []
    for i in range(0, len(test_data)):
        for n in range(1, len(test_data.columns)):
            node_list_value.append(test_data[test_data.columns[n]][i])

    # 去重
    node_list_value = list(set(node_list_value))

    # 将list中全部转换为string
    node_list_value = [str(i) for i in node_list_value]

    return node_buy_key, node_sell_key, node_list_value


def relation_extraction():

    links_dict = {}
    sell_list = []
    money_list = []
    buy_list = []

    # 遍历数据采集数据
    for i in range(0, len(test_data)):
        money_list.append(test_data[test_data.columns[1][i]])  # 店铺
        sell_list.append(test_data[test_data.columns[2][i]])  # 价格
        buy_list.append(test_data[test_data.columns[0][i]])  # 商品

    sell_list = [str(i) for i in sell_list]
    money_list = [str(i) for i in money_list]
    buy_list = [str(i) for i in buy_list]

    # 整合数据
    links_dict['buy'] = buy_list
    links_dict['money'] = money_list
    links_dict['sell'] = sell_list

    df_data = pd.DataFrame(links_dict)
    print(df_data)
    return df_data


create_data = DataToNeo4j()
create_data.create_node(data_extraction()[0], data_extraction()[1])
create_data.create_relation(relation_extraction())

""" test_graph = Graph("http://localhost:7474/browser/",
                   auth=("neo4j", "zyt260019"), name="neo4j")
test_graph.delete_all() """

""" # 定义node
node_1 = Node('英雄', name='张无忌')
node_2 = Node('派别', name='明教')

# 存入图数据库
test_graph.create(node_1)
test_graph.create(node_2)

# 增加关系
node_1_to_node_2 = Relationship(node_1, "教主", node_2)
test_graph.create(node_1_to_node_2)
 """
