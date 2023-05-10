# pip install py2neo -i https://pypi.tuna.tsinghua.edu.cn/simple 第三方库
# neo4j.bat console

from py2neo import Node, Relationship
from py2neo import Graph, Subgraph
from py2neo import Path
from build_node_relation import DataToNeo4j
import pandas as pd
import csv
import xlrd

test_graph = Graph("http://localhost:7474/browser/",
                   auth=("neo4j", "zyt260019"), name="neo4j")
test_graph.delete_all()

""" def data_extraction():
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
    return df_data """

node_1 = Node("商品", name='HLA海澜之家短袖T恤男夏新疆棉微弹圆领数码印花t恤男')
node_2 = Node("价格", name='88')
node_3 = Node("店铺", name='海澜之家京东自营旗舰店')
node_4 = Node("材质", name='棉')
node_5 = Node("面料", name='纯棉')
node_6 = Node("类型", name='休闲风简约风')
node_7 = Node("品牌", name='海澜之家（HLA）')

test_graph.create(node_1)
test_graph.create(node_2)
test_graph.create(node_3)
test_graph.create(node_4)
test_graph.create(node_5)
test_graph.create(node_6)
test_graph.create(node_7)

node_12 = Relationship(node_1, "价格", node_2)
node_13 = Relationship(node_1, "店铺", node_3)
node_14 = Relationship(node_1, "材质", node_4)
node_15 = Relationship(node_1, "面料", node_5)
node_16 = Relationship(node_1, "类型", node_6)
node_17 = Relationship(node_1, "品牌", node_7)

test_graph.create(node_12)
test_graph.create(node_13)
test_graph.create(node_14)
test_graph.create(node_15)
test_graph.create(node_16)
test_graph.create(node_17)
""" node_11 = Node
node_12 = Node
node_13 = Node
node_14 = Node
node_15 = Node
node_16 = Node
node_17 = Node """
