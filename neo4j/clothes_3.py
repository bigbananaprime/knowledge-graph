# pip install py2neo -i https://pypi.tuna.tsinghua.edu.cn/simple 第三方库
# neo4j.bat console

from py2neo import NodeMatcher
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

node_1 = Node("商品", name='红蜻蜓短袖t恤女夏季新款韩版洋气时尚百搭显瘦女装夏装打底圆领上衣衫')
node_2 = Node("价格", name='89')
node_3 = Node("店铺", name='红蜻蜓服饰旗舰店')
node_4 = Node("材质", name='棉')
node_5 = Node("面料", name='纯棉')
node_6 = Node("类型", name='宽松型袖型')
node_7 = Node("品牌", name='红蜻蜓（RED DRAGONFLY）')

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

node_21 = Node("商品", name='红蜻蜓t恤女短袖2023年夏季新款女装修身打底格子百搭女士上衣服衫')
node_22 = Node("价格", name='89')
node_23 = Node("店铺", name='红蜻蜓女装旗舰店')
node_24 = Node("材质", name='其他')
node_25 = Node("面料", name='其他')
node_26 = Node("类型", name='甜美风')
node_27 = Node("品牌", name='红蜻蜓（RED DRAGONFLY）')

test_graph.create(node_21)
test_graph.create(node_22)
test_graph.create(node_23)
test_graph.create(node_27)

node_121 = Relationship(node_21, "价格", node_2)
node_131 = Relationship(node_21, "店铺", node_3)
node_141 = Relationship(node_21, "材质", node_24)
node_151 = Relationship(node_21, "面料", node_25)
node_161 = Relationship(node_21, "类型", node_26)
node_171 = Relationship(node_21, "品牌", node_7)

test_graph.create(node_121)
test_graph.create(node_131)
test_graph.create(node_141)
test_graph.create(node_151)
test_graph.create(node_161)
test_graph.create(node_171)

# 定义查询
nodes = NodeMatcher(test_graph)
# 单节点查询
node_single = nodes.match(
    "商品", name='红蜻蜓短袖t恤女夏季新款韩版洋气时尚百搭显瘦女装夏装打底圆领上衣衫').first()
print('单节点查询：\n', node_single)
# 多节点查询
node_hero = nodes.match("商品").all()
print('查询结果的数据类型', type(node_hero))

i = 0
for node in node_hero:
    print('label查询第{}个为：{}'.format(i, node))
    i += 1

node_name = node.match(name='红蜻蜓短袖t恤女夏季新款韩版洋气时尚百搭显瘦女装夏装打底圆领上衣衫').all()
print("查询结果", node_name)
