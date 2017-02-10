##SPARQL
# https://query.wikidata.org/bigdata/namespace/wdq/sparql?query=
##DESCRIPTION
# This query extracts from Wikipathways all simple interactions. These are relationships between one input and one output pathway element
##DATATYPES
# Geneproducts, Proteins
##MENU_LABEL
# Physically interacts with

SELECT ?source ?sourceLabel ?target ?targetLabel ?source_geneId ?source_uniprotId
?target_geneId ?target_uniprotId ?source_pubchemId ?target_pubchemId
WHERE
{
?source
wdt: P129 ?target.
    OPTIONAL
{?source
wdt: P351 ?source_geneId}
OPTIONAL
{?source
wdt: P352 ?source_uniprotId}
OPTIONAL
{?source
wdt: P661 ?source_pubchemId}
OPTIONAL
{?target
wdt: P351 ?target_geneId}
OPTIONAL
{?target
wdt: P352 ?target_uniprotId}
OPTIONAL
{?target
wdt: P661 ?target_pubchemId}
SERVICE
wikibase: label
{bd: serviceParam wikibase: language "en"}
}
