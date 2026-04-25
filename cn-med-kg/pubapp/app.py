import streamlit as st
from neo4j import GraphDatabase
# import pandas as pd
from pyvis.network import Network

# --- CONFIG ---
NEO4J_URI = st.secrets["NEO4J_URI"]
NEO4J_USER = st.secrets["NEO4J_USER"]
NEO4J_PASSWORD = st.secrets["NEO4J_PASSWORD"]

# Neo4j connection
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def query_graph(tx):
    query = """
    MATCH (n)-[r]->(m)
    RETURN n, r, m LIMIT 1000
    """
    return list(tx.run(query))

# --- UI ===
st.title("Traditional Medicine Knowledge Graph")

st.markdown("Expore using Neo4j")

def build_graph(data):
    net = Network(height="900px", width="100%", directed=True)

    for record in data:
        n = record["n"]
        m = record["m"]
        r = record["r"]

        net.add_node(n.id, label=n.get("name", str(n.id)))
        net.add_node(m.id, label=m.get("name", str(m.id)))
        net.add_edge(n.id, m.id, label=type(r).__name__)

    return net

with driver.session() as session:
    result = session.execute_read(query_graph)

net = build_graph(result)

# Save and display
net.save_graph("graph.html")

with open("graph.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=600)