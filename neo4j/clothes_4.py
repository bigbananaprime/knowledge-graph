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

node_1 = Node("商品", name='红蜻蜓短袖t恤女夏季新款韩版洋气时尚百搭显瘦女装夏装打底圆领上衣衫')
node_2 = Node("商品", name='红蜻蜓t恤女短袖2023年夏季新款女装修身打底格子百搭女士上衣服衫')
node_3 = Node("商品", name='红蜻蜓短袖t恤女早春夏季新款T恤女装夏装冰丝打底时尚百搭衫上衣ins潮')
node_4 = Node("商品", name='红蜻蜓纯棉短袖t恤女宽松正肩夏季女装2023年新款韩版半袖体恤夏装上衣')
node_5 = Node("商品", name='红蜻蜓牛仔裤女2023年春夏季新款高腰女装哈伦牛仔裤撞色休闲女士老爹裤')
node_6 = Node("商品", name='红蜻蜓t恤女短袖纯棉宽松小熊女装印花2023年夏季新款女士打底上衣服衫')
node_7 = Node("商品", name='红蜻蜓白色纯棉长袖t恤女春装2023新款时尚长袖女上衣内搭打底衫女士潮')
node_8 = Node("商品", name='红蜻蜓短袖t恤女2023年设计感正肩夏季女装宽松垂感纯棉女士打底上衣衫')
node_9 = Node("商品", name='红蜻蜓2023早春夏季新款纯棉短袖t恤女半袖女装夏款潮韩版宽松女士圆领')
node_10 = Node("商品", name='红蜻蜓t恤女纯棉短袖夏装2023年夏季新款女士上衣小众设计感印花女装衫')
node_11 = Node("商品", name='红蜻蜓短袖t恤女2023年夏季新款爱心印花女装纯棉打底百搭女士上衣衫')
node_12 = Node("商品", name='红蜻蜓短袖t恤女2023年夏季新款爱心印花女装纯棉打底百搭女士上衣衫')
node_13 = Node("商品", name='红蜻蜓短袖t恤女2023年夏季新款爱心印花女装纯棉打底百搭女士上衣衫')
node_14 = Node("商品", name='红蜻蜓短袖t恤女2023年夏季新款爱心印花女装纯棉打底百搭女士上衣衫')
node_15 = Node("商品", name='红蜻蜓短袖t恤女2023年夏季新款爱心印花女装纯棉打底百搭女士上衣衫')
node_16 = Node("品牌", name='红蜻蜓（RED DRAGONFLY）')

test_graph.create(node_1)
test_graph.create(node_2)
test_graph.create(node_3)
test_graph.create(node_4)
test_graph.create(node_5)
test_graph.create(node_6)
test_graph.create(node_7)
test_graph.create(node_8)
test_graph.create(node_9)
test_graph.create(node_10)
test_graph.create(node_11)
test_graph.create(node_12)
test_graph.create(node_13)
test_graph.create(node_14)
test_graph.create(node_15)
test_graph.create(node_16)

node__12 = Relationship(node_16, "商品1", node_2)
node__13 = Relationship(node_16, "商品2", node_3)
node__14 = Relationship(node_16, "商品3", node_4)
node__15 = Relationship(node_16, "商品4", node_5)
node__16 = Relationship(node_16, "商品5", node_6)
node__17 = Relationship(node_16, "商品6", node_7)
node__121 = Relationship(node_16, "商品7", node_8)
node__131 = Relationship(node_16, "商品8", node_9)
node__141 = Relationship(node_16, "商品9", node_10)
node__151 = Relationship(node_16, "商品10", node_11)
node__161 = Relationship(node_16, "商品11", node_12)
node__171 = Relationship(node_16, "商品12", node_13)
node__1211 = Relationship(node_16, "商品13", node_14)
node__1311 = Relationship(node_16, "商品14", node_15)
node__1411 = Relationship(node_16, "商品15", node_1)

test_graph.create(node__12)
test_graph.create(node__13)
test_graph.create(node__14)
test_graph.create(node__15)
test_graph.create(node__16)
test_graph.create(node__17)
test_graph.create(node__121)
test_graph.create(node__131)
test_graph.create(node__141)
test_graph.create(node__151)
test_graph.create(node__161)
test_graph.create(node__171)
test_graph.create(node__1211)
test_graph.create(node__1311)
test_graph.create(node__1411)

""" node_11 = Node
node_12 = Node
node_13 = Node
node_14 = Node
node_15 = Node
node_16 = Node
node_17 = Node """
