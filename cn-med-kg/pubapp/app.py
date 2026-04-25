import streamlit as st
from neo4j import GraphDatabase
import pandas as pd

# --- CONFIG ---
NEO4J_URI = st.secrets["NEO4J_URI"]
NEO4J_USER = st.secrets["NEO4J_USER"]
NEO4J_PASSWORD = st.secrets["NEO4J_PASSWORD"]

# --- CONNECTION ---
@st.cache_resource
def get_driver():
    return GraphDatabase.driver(
        NEO4J_URI,
        auth = (NEO4J_USER, NEO4J_PASSWORD)
    )

driver = get_driver()

# --- QUERY FUNCTION ---
def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return [r.data() for r in result]

# --- UI ===
st.title("Traditional Medicine Knowledge Graph")

st.markdown("Expore using Neo4j")

# --- USER INPUT ---
query = st.text_area(
    "Enter Cypher Query:",
    "MATCH (n)-[r]->(m) RETURN n,r,m LIMIT 25"
)

if st.button("Run Query"):
    data = run_query(query)
    st.write("### Results")
    st.json(data)