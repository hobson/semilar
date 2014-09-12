#semblance
# quantify the semantic proximity (similarity) between (of) two words


# export NEO4J_ROOT=/home/hobs/src/neo4j-community-2.1.4
# $NEO4J_ROOT/bin/neo4j console

# cd /home/hobs/src
# git clone git@github.com:neo4j-contrib/gremlin-plugin.git
# cd /home/hobs/src/gremlin-plugin
# mvn clean package
# unzip target/neo4j-gremlin-plugin-2.1-SNAPSHOT-server-plugin.zip -d $NEO4J_ROOT/plugins/gremlin-plugin
# cd $NEO4J_ROOT
# bin/neo4j restart



import nltk
from nltk.corpus import wordnet as wn

from bulbs.model import Node, Relationship
from bulbs.property import String, Integer, DateTime
from bulbs.utils import current_datetime
from bulbs.neo4jserver import Graph

nltk.download('wordnet')

# wn.synsets('dog')
# len(wn.all_lemma_names())  # 140k words


class Lemma(Node):
    element_type = "lemma"
    name = String(nullable=False)

g = Graph()
g.add_proxy("lemma", Lemma)


# >>> g.add_proxy("knows", Knows)
# >>> james = g.people.create(name="James")
# >>> julie = g.people.create(name="Julie")
# >>> g.knows.create(james, julie)

import progressbar as pb

N = 150000
for N, ln in enumerate(wn.all_lemma_names()):
    pass

widgets = [pb.Counter(), '%d rows: ' % N, pb.Percentage(), ' ', pb.RotatingMarker(), ' ', pb.Bar(),' ', pb.ETA()]
pbar = pb.ProgressBar(widgets=widgets, maxval=N).start()

for i, ln in enumerate(wn.all_lemma_names()):
    pbar.update(i)
    lemma = g.lemma.create(name=str(ln))
    #Lemma(ln).save()
pb.finish()

# class Knows(Relationship):

#     label = "knows"

#     created = DateTime(default=current_datetime, nullable=False)

# >>> from people import Person, Knows
# >>> from bulbs.neo4jserver import Graph

# >>> g = Graph()
# >>> g.add_proxy("people", Person)
# >>> g.add_proxy("knows", Knows)

# >>> james = g.people.create(name="James")
# >>> julie = g.people.create(name="Julie")
# >>> g.knows.create(james, julie)