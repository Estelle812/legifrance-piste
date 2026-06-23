---
description: |
  Guide de configuration des clés PISTE pour le plugin Légifrance. Déclencher quand :
  l'utilisateur dit "configurer piste", "setup piste", "mes clés piste", "je n'ai pas de clé",
  "comment avoir accès à légifrance", "le plugin ne fonctionne pas", "erreur clés manquantes",
  ou quand une erreur de clés PISTE est détectée.
---

# Setup PISTE — Configuration guidée

Guide l'utilisateur pas à pas pour obtenir et configurer ses clés PISTE.

## Étape 1 — Vérifier si uv est installé

Demander à l'utilisateur d'ouvrir un terminal et de taper :
```
uv --version
```

Si la commande n'est pas reconnue, lui donner la commande d'installation selon son OS :
- **Windows** : `winget install astral-sh.uv`
- **Mac/Linux** : `curl -LsSf https://astral.sh/uv/install.sh | sh`

Préciser que `uv` remplace `pip` et gère automatiquement les dépendances Python — pas besoin de rien installer d'autre.

## Étape 2 — Créer un compte PISTE

Diriger vers : **https://piste.gouv.fr**

Instructions :
1. Cliquer sur **"S'inscrire"** (en haut à droite)
2. Remplir le formulaire (nom, email, organisme)
3. Valider l'email de confirmation
4. Se connecter

## Étape 3 — S'abonner à l'API Légifrance

Une fois connecté sur piste.gouv.fr :
1. Aller dans **"Catalogue des API"** (menu principal)
2. Chercher **"Légifrance"**
3. Cliquer sur l'API → **"S'abonner"**
4. Choisir l'environnement **"Production"**
5. Valider — l'abonnement est gratuit et quasi-immédiat

## Étape 4 — Récupérer les clés

1. Aller dans **"Mes applications"** (menu utilisateur en haut à droite)
2. Cliquer sur l'application créée automatiquement lors de l'abonnement
3. Copier le **Consumer Key** (= `client_id`) et le **Consumer Secret** (= `client_secret`)

## Étape 5 — Configurer Claude Desktop

Expliquer à l'utilisateur d'ouvrir ce fichier dans un éditeur de texte :
- **Windows** : `C:\Users\<votre-nom>\AppData\Roaming\Claude\claude_desktop_config.json`
- **Mac** : `~/Library/Application Support/Claude/claude_desktop_config.json`

Localiser le bloc `"legifrance"` et remplir les deux valeurs :

```json
"env": {
  "PISTE_CLIENT_ID": "coller_votre_consumer_key_ici",
  "PISTE_CLIENT_SECRET": "coller_votre_consumer_secret_ici"
}
```

Sauvegarder le fichier, puis **redémarrer Claude Desktop**.

## Étape 6 — Tester

Proposer à l'utilisateur de tester avec une question simple :
> *"Que dit l'article 1382 du Code civil ?"*

Si ça fonctionne, le setup est terminé. Si une erreur apparaît, vérifier que :
- Les clés sont bien copiées sans espace avant/après
- Le fichier JSON est valide (pas de virgule manquante)
- Claude Desktop a bien été redémarré
