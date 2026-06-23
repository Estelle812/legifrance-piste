# Légifrance PISTE — Plugin Claude

> Recherche juridique en temps réel dans Légifrance, directement depuis Claude Desktop.

**Français** | [English](#english)

---

## Ce que ça fait

Connecte Claude à l'API Légifrance. Posez vos questions juridiques en langage naturel — Claude interroge Légifrance et vous retourne les textes officiels à jour.

**Outils disponibles :**
- Recherche dans n'importe quel code juridique (Code civil, Code du travail, Code pénal, Code de commerce…)
- Recherche dans la jurisprudence judiciaire
- Texte complet d'un article par son identifiant Légifrance

**Exemples :**
- *"Que dit le Code civil sur la responsabilité contractuelle ?"*
- *"Quels articles sur le licenciement pour faute grave ?"*
- *"Cherche de la jurisprudence sur le préjudice moral"*

---

## Installation

### 1. Télécharger le plugin

👉 [`legifrance-piste.plugin`](https://github.com/Estelle812/legifrance-piste/releases/latest/download/legifrance-piste.plugin)

### 2. Installer dans Claude Desktop

**Settings → Capabilities → Plugins → Install from file**

Sélectionner le fichier `.plugin` téléchargé. C'est tout.

---

## Pour les développeurs — déployer votre propre instance

Ce repo inclut un `render.yaml` pour déployer votre propre serveur sur [Render](https://render.com) :

1. Forkez ce repo
2. Connectez-le à Render (New → Web Service → Connect GitHub)
3. Ajoutez vos variables d'environnement dans le dashboard Render :
   - `PISTE_CLIENT_ID`
   - `PISTE_CLIENT_SECRET`
4. Mettez à jour l'URL dans `.mcp.json` avec votre URL Render
5. Repackagez le plugin avec `zip -r legifrance-piste.plugin . -x "*.DS_Store"`

---

## Avertissement

Résultats fournis à titre informatif. Consultez un professionnel du droit pour toute décision importante.

---

---

<a name="english"></a>

# Légifrance PISTE — Claude Plugin

> Real-time French legal research in Légifrance, directly from Claude Desktop.

## What it does

Connects Claude to the Légifrance API. Ask legal questions in plain language — Claude queries Légifrance and returns up-to-date official texts.

**Examples:**
- *"What does the Civil Code say about contractual liability?"*
- *"Which articles cover dismissal for serious misconduct?"*
- *"Find case law on moral damages"*

## Installation

### 1. Download the plugin

👉 [`legifrance-piste.plugin`](https://github.com/Estelle812/legifrance-piste/releases/latest/download/legifrance-piste.plugin)

### 2. Install in Claude Desktop

**Settings → Capabilities → Plugins → Install from file**

Select the downloaded `.plugin` file. That's it.

## For developers — self-hosting

This repo includes a `render.yaml` for deploying your own instance on [Render](https://render.com).

## Disclaimer

Results are provided for informational purposes only and do not constitute legal advice.

## License

MIT © Estelle812
