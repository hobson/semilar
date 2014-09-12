from py2neo import neo4j

graph_db = neo4j.GraphDatabaseService()
print(graph_db.neo4j_version)

import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')


import progressbar as pb

N = 150000
for N, ln in enumerate(wn.all_lemma_names()):
    pass

widgets = [pb.Counter(), ' / %d rows: ' % N, pb.Percentage(), ' ', pb.RotatingMarker(), ' ', pb.Bar(),' ', pb.ETA()]
pbar = pb.ProgressBar(widgets=widgets, maxval=N).start()

# # create a single node
# alice, = graph_db.create({"name": "Alice"})

# # create multiple nodes
# people = graph_db.create(
#     {"name": "Alice", "age": 33}, {"name": "Bob", "age": 44},
#     {"name": "Carol", "age": 55}, {"name": "Dave", "age": 66},
# )

# # create two nodes with a connecting relationship
# alice, bob, rel = graph_db.create(
#     {"name": "Alice"}, {"name": "Bob"},
#     (0, "KNOWS", 1, {"since": 2006})
# )

# # create a node plus a relationship to pre-existing node
# ref_node = graph_db.get_reference_node()
# alice, rel = graph_db.create(
#     {"name": "Alice"}, (ref_node, "PERSON", 0)
# )

lemma_index = graph_db.get_or_create_index(neo4j.Node, "Lemmas")
synonym_index = graph_db.get_or_create_index(neo4j.Relationship, "Is-Synonymous-With")
senses_index = graph_db.get_or_create_index(neo4j.Node, "Senses")
synonym_index = graph_db.get_or_create_index(neo4j.Relationship, "Is-A-Sense-Of")

for i, ln in enumerate(wn.all_lemma_names()):
    pbar.update(i)
    g_lemma, = graph_db.create({'name': str(ln)})
    syns = wn.synsets(ln)
    for syn in syns:
        #g_syn = graph_db.create(name=syn, )
        print syn
        #lemma_rel = wn.rel((syn,'Is-A-Sense-Of',g_lemma))
    # ref_node = graph_db.get_reference_node()
pbar.finish()


