import streamlit as st
from PIL import Image


# config

FULLNAME = "Koffi"
PROFESSIONAL_TITLE = "Data Scientist"
PAGE_TITLE = f"{FULLNAME} - {PROFESSIONAL_TITLE}"
ABOUT = "Junior Data Scientist specializing in Knowledge Graphs and Linked Data"
EMAIL = "email@example.com"
LOCATION = "Cotonou, République du Bénin"
SOCIAL_LINK = {
    "linkedin": "https://www.example.com",
    "github": "https://www.example.com",
    "youtube": "https://www.example.com",
}
PROFILE_PICTURE = "assets/profile_placeholder.png"


# configurer streamlit
st.set_page_config(page_title=PAGE_TITLE)


# header: photo, contact, about
col1, col2 = st.columns(2)

with col1:
    st.image(PROFILE_PICTURE, width=300)

with col2:
    st.title(FULLNAME)
    st.write(ABOUT)
    st.write(f"Email: {EMAIL}")
    for social_key in SOCIAL_LINK.keys():
        st.write(f"{social_key}: {SOCIAL_LINK[social_key]}")


# projets
st.title("Projets")
st.markdown("""
- **Projet 1: Knowledge Graph for E-commerce**  
  Création d'un graphe de connaissances pour améliorer la gestion des produits et des utilisateurs, augmentant les recommandations de 25% et réduisant le taux d'abandon des paniers de 30%.

- **Projet 2: Data-Driven Insights for Marketing**  
  _URL_: [Voir le projet](https://github.com/example/project2)  
  Développement de modèles de recommandation personnalisée et de tableaux de bord pour optimiser les campagnes marketing, augmentant les ventes de 15% et le taux de conversion de 10%.

- **Projet 3: Data Integration for Healthcare**  
  _URL_: [Voir le projet](https://github.com/example/project3)  
  Intégration des données de santé pour améliorer la gestion des informations des patients, facilitant les diagnostics et la coordination des soins tout en réduisant les risques de santé publique.
""")

# compétence
st.title("Compétences")

st.subheader("Compétences Techniques")
st.markdown("""
- Knowledge Graph Engineering (RDF, OWL, SPARQL)
- Linked Data and Semantic Web Technologies
- Data Wrangling & ETL (Python, Pandas, RDFLib)
- Graph Databases (Neo4j, GraphDB)
- Data Visualization & Reporting (Tableau, Power BI)
""")


# experiences
st.title("Expériences")
st.markdown("""

### Junior Data Scientist  
*SemanticAI Solutions* | Berlin, Germany | Jan 2024 - Present  
- Developed and maintained Knowledge Graphs for enterprise data integration, enabling advanced semantic search and reasoning capabilities.  
- Designed SPARQL queries and automated ETL pipelines to extract and transform structured and unstructured data into linked data formats.  
- Collaborated with cross-functional teams to apply ontology modeling (OWL, RDF) and align datasets with industry-standard vocabularies.

### Data Science Intern  
*LinkedData Innovations* | Amsterdam, Netherlands | Jul 2023 - Dec 2023  
- Assisted in building domain-specific knowledge graphs and linking them with external open data sources using Linked Data principles.  
- Worked on data quality assessment and enrichment for graph datasets, ensuring consistency and interoperability across systems.  
- Supported the development of data visualization dashboards to communicate insights from graph analytics to non-technical stakeholders.

### Data Analyst Trainee  
*NeoData Insights* | Remote | Feb 2023 - Jun 2023  
- Performed exploratory data analysis on relational datasets and contributed to the migration process toward graph-based databases (Neo4j).  
- Created technical documentation and user guides for internal tools used in knowledge graph construction and querying.  
- Participated in workshops on Linked Data principles and Semantic Web technologies, strengthening hands-on technical skills.
""")


# certifications
st.title("Certifications")
st.markdown("""
- **Certification en Data Science** | _Université ABC_ | _2022_  
  Python, Visualization & Reporting (Tableau, Power BI), Base de la Data Science

- **Certification Machine Learning** | _Coursera (offerte par Stanford)_ | _2021_  
  Machine Learning, Implementation d'algorithmes de régression et réseaux de neurones

- **Certification en Graphes de Connaissances** | _Udemy_ | _2023_  
  Graphes de connaissances, RDF, SPARQL, GraphDB
""")





# blogs et derniers articles
