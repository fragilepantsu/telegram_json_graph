import json
import networkx
import networkx as nx
from collections import Counter


G = nx.Graph()

file = ''

with open(file, 'r', encoding='utf8') as jsonfile:
     data = json.load(jsonfile)
     messages = data['messages']
     print('File', file, 'loaded.')

def FindAllUsers():
        users = set()
        for node in messages:
            users.add(node.get('from'))
            print('User', node.get('from'), 'discovered!')
        users.remove(None)
        return users


def FindUserNeighbours(user):
    ids = set()
    neighbours = set()
    for i in messages:
        if i.get('from') == user:
           ids.add(i.get('reply_to_message_id'))



    for i in messages:
        if i.get('id') in ids:
            if i.get('from') in neighbours:
                pass
            else:
                neighbours.add(i.get('from'))
                print('Neighbour',i.get('from'),'for', user, 'discovered!')
        else:
            pass


    return neighbours


def CreateNeighboursDict():
    for i in FindAllUsers():
        if i is None:
            pass
        else:
            for r in FindUserNeighbours(i):
                if r is None:
                    pass
                else:
                    if r == i:
                        pass
                    else:
                        w = CountUserRepliesTo(i, r)
                        print('Adding edges:', i, r, w)
                        G.add_edge(i, r, weight=w)
                        # G.add_edge(i, r)

def CountUserMessages(user):
    counter = set()
    for i in messages:
        if i.get('from') == user:
            if i.get('from') is None:
                pass
            else:
                counter.add(i.get('from'))
    return counter


def CountAllUsersMessages():
    counted = set()
    for i in FindAllUsers():
        counted.add(CountUserMessages(i))
    return counted

def CountUserRepliesTo(user, ruser):
    ids = set()
    counted = []
    for i in messages:
        if i.get('from') == user:
            if i.get('reply_to_message_id') in ids:
                pass
            else:
                ids.add(i.get('reply_to_message_id'))

    for i in messages:
        if i.get('id') in ids:
                counted.append(i.get('from'))
        else:
            pass
    out = Counter(counted)
    ruser = out.get(ruser)
    return ruser



CreateNeighboursDict()
# remove_nodes = ['user1', 'user2']
# G.remove_nodes_from(remove_nodes)
# nx.draw_networkx(G, node_size=300, node_color='#73a7fa', edge_color='#e8e8e8', with_labels=True, font_size=5)
print('------------------ FINISHED ------------------')
networkx.write_gexf(G, 'vorovannie.gexf')
print('Exported')
