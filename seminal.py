
# # install maven
# cd ~/src
# wget http://mirrors.gigenet.com/apache/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.tar.gz
# su -c "tar -zxvf apache-maven-3.0.5-bin.tar.gz -C /opt/"
# cd /opt/apache-maven-3.0.5/
# cat README.txt 
# sudo nano /etc/profile.d/maven.sh
# sudo echo '
# export M2_HOME=/opt/apache-maven-3.0.5
# export M2=$M2_HOME/bin
# PATH=$M2:$PATH 
# ' | sudo tee /etc/profile.d/maven.sh
# mvn -v
# rm ~/src/apache-maven-3.0.5-bin.tar.gz 

# # Install command line REPL for gremlin and neo4j
# cd ~/src
# git clone https://github.com/tinkerpop/gremlin.git /home/hobs/src/gremlin
# cd ../gremlin/
# mvn clean install

# # install gremlin plugin
# cd ~/src
# cd /home/hobs/src
# git clone git@github.com:neo4j-contrib/gremlin-plugin.git
# cd /home/hobs/src/gremlin-plugin
# mvn clean package
# unzip target/neo4j-gremlin-plugin-2.1-SNAPSHOT-server-plugin.zip -d $NEO4J_ROOT/plugins/gremlin-plugin
# NEO4J_ROOT=/home/hobs/src/neo4j-community-2.1.4/
# unzip target/neo4j-gremlin-plugin-2.1-SNAPSHOT-server-plugin.zip -d $NEO4J_ROOT/plugins/gremlin-plugin
# cd $NEO4J_ROOT
# ./bin/neo4j restart


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


