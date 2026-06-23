---
description: |
  Recherche juridique dans Légifrance via PISTE. Utiliser quand l'utilisateur mentionne :
  un article de loi, un code juridique (Code civil, Code du travail, Code pénal, Code de commerce...),
  de la jurisprudence, un texte législatif, une recherche juridique, du droit français,
  "que dit la loi sur", "article X du code", "responsabilité", "contrat", "licenciement",
  "infraction", ou toute question de droit.
---

# Skill Légifrance PISTE

Ce plugin connecte Claude à Légifrance en temps réel via la passerelle PISTE.

## Outils disponibles

- `search_code` — recherche dans un code juridique par mots-clés
- `search_jurisprudence` — recherche dans la jurisprudence judiciaire
- `get_article` — récupère le texte complet d'un article par son ID Légifrance

## Comportement attendu

Quand l'utilisateur pose une question juridique :

1. Identifier le code pertinent parmi ceux disponibles (voir références)
2. Appeler `search_code` avec des termes précis du droit français
3. Si la jurisprudence est pertinente, appeler aussi `search_jurisprudence`
4. Si l'utilisateur veut le texte complet d'un article, appeler `get_article` avec l'ID retourné
5. Citer systématiquement les articles avec leur lien Légifrance officiel
6. Préciser la date d'entrée en vigueur

## Codes juridiques principaux et leurs identifiants

Voir `references/codes-juridiques.md` pour la liste complète des identifiants.

## Bonnes pratiques de recherche

- Préférer les termes juridiques précis : "inexécution obligation" plutôt que "non-respect contrat"
- Combiner plusieurs mots-clés pour affiner : "licenciement faute grave procédure"
- Si peu de résultats, essayer des synonymes ou des termes plus généraux
- Toujours indiquer à l'utilisateur la date de vigueur des articles retournés

## Avertissement légal

Rappeler à l'utilisateur que les résultats sont fournis à titre informatif et ne constituent pas un conseil juridique. Pour toute décision importante, recommander de consulter un professionnel du droit.
