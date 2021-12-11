# telegram_json_graph
Graph generator from JSON exported from telegram 

# Description
The script creates a graph based on JSON exported from Telegram. Each user is a node, the edges are a reply to another user. The weight of an edge is the number of responses.

In the script body it is possible to enable graph output in pycharm for example and filter weight analysis if it is not required. The analysis of the number of responses takes considerable time.

# Usage
In the line "file = ''" specify the relative path to result.json.
The line " remove_nodes = ['user1', 'user2']" is responsible for removing vertices from the graph results. When uncommenting it you should also uncomment the line "G.remove_nodes_from(remove_nodes)".

By default, the script saves the result for Gephi in the line " networkx.write_gexf(G, 'FILE NAME.gexf') "

# License & Distribution
You can use this script however you want without attribution or source. I guess if you open a huge corporation to create telegram chat graphs, I won't sue you for using this code. I don't care.

