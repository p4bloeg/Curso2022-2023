#!/usr/bin/env python
# coding: utf-8

# **Task 06: Modifying RDF(s)**

# In[14]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[15]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")


# Create a new class named Researcher

# In[16]:


ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)


# **TASK 6.1: Create a new class named "University"**
# 

# In[17]:


# TO DO
g.add((ns.University, RDF.type, RDFS.Class))

# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.2: Add "Researcher" as a subclass of "Person"**

# In[18]:


# TO DO
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.3: Create a new individual of Researcher named "Jane Smith"**

# In[24]:


# TO DO
janeURI = ns.JaneSmith

resource = (janeURI, RDF.type, ns.Researcher)

g.add(resource)

# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**

# In[25]:


# TO DO
fullName = Literal("Jane Smith")
name = Literal("Jane")
family = Literal("Smith")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

g.add((janeURI, VCARD.FN, fullName))
g.add((janeURI, VCARD.Given, name))
g.add((janeURI, VCARD.Family, family))
      
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# **TASK 6.5: Add UPM as the university where John Smith works**

# In[26]:


# TO DO
upmURI = ns.UPM
johnURI = ns.JohnSmith
g.add((ns.worksAt, RDF.type, RDF.Property))
g.add((upmURI, RDF.type, ns.University))
g.add((johnURI, ns.worksAt, upmURI))
# Visualize the results
for s, p, o in g:
  print(s,p,o)


# In[ ]:




