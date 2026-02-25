# CM_BASE Ontology - Chinese Medicine Base

- [CM\_BASE Ontology - Chinese Medicine Base](#cm_base-ontology---chinese-medicine-base)
  - [Initial Ontology](#initial-ontology)
  - [](#)

## Initial Ontology

Create one RDF/OWL file called [cm_base.rdf](cm_base.rdf)

Ontology IRI: http://www.semanticweb.org/v0cn037/ontologies/2026/1/cm_base

![initial_ontology](img/initial_ontology.png)

Add `cm` as PREFIX into below SPARQL query headers:

```SQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX cm: <http://www.semanticweb.org/v0cn037/ontologies/2026/1/cm_base#>
SELECT ?subject ?object
	WHERE { ?subject rdfs:subClassOf ?object }
```

## 