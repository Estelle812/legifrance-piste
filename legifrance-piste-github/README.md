# Légifrance PISTE — Plugin Claude

> Recherche juridique en temps réel dans Légifrance, directement depuis Claude Desktop.

**Français** | [English](#english)

---

## Ce que ça fait

Connecte Claude à l'API Légifrance via la passerelle [PISTE](https://piste.gouv.fr) du gouvernement français. Posez vos questions juridiques en langage naturel — Claude interroge Légifrance et vous retourne les textes officiels à jour.

**Outils disponibles :**
- `search_code` — recherche dans n'importe quel code juridique (Code civil, Code du travail, Code pénal, Code de commerce…)
- `search_jurisprudence` — recherche dans la jurisprudence judiciaire
- `get_article` — texte complet d'un article par son identifiant Légifrance

**Exemples de questions :**
- *"Que dit le Code civil sur la responsabilité contractuelle ?"*
- *"Quels articles sur le licenciement pour faute grave ?"*
- *"Cherche de la jurisprudence sur le préjudice moral"*
- *"Donne-moi le texte de l'article 1231-1 du Code civil"*

---

## Installation

### 1. Télécharger le plugin

👉 Télécharger [`legifrance-piste.plugin`](https://github.com/Estelle812/legifrance-piste/releases/latest/download/legifrance-piste.plugin)

puis dans Claude Desktop :
Settings → Capabilities → Plugins → Install from file
Sélectionne le fichier .plugin téléchargé.

### 2. Installer `uv` (gestionnaire Python, une seule fois)

| OS | Commande |
|----|----------|
| Windows | `winget install astral-sh.uv` |
| Mac/Linux | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

`uv` installe automatiquement les dépendances Python au premier lancement — rien d'autre à faire.

### 3. Configurer les clés PISTE

Après installation, tapez dans Claude :

> **"setup piste"**

Claude vous guide pas à pas pour créer votre compte PISTE gratuit et configurer vos clés.

---

## Prérequis

- [Claude Desktop](https://claude.ai/download) installé
- Un compte gratuit sur [piste.gouv.fr](https://piste.gouv.fr) avec abonnement à l'API Légifrance

---

## Avertissement

Les résultats sont fournis à titre informatif et ne constituent pas un conseil juridique. Consultez un professionnel du droit pour toute décision importante.

---

## Contribuer

Les contributions sont bienvenues ! Ouvrez une issue ou une pull request.

---

---

<a name="english"></a>

# Légifrance PISTE — Claude Plugin

> Real-time French legal research in Légifrance, directly from Claude Desktop.

## What it does

Connects Claude to the Légifrance API via the French government's [PISTE](https://piste.gouv.fr) gateway. Ask legal questions in plain language — Claude queries Légifrance and returns up-to-date official texts.

**Available tools:**
- `search_code` — search any French legal code (Civil Code, Labour Code, Penal Code, Commercial Code…)
- `search_jurisprudence` — search judicial case law
- `get_article` — full text of an article by its Légifrance ID

**Example queries:**
- *"What does the Civil Code say about contractual liability?"*
- *"Which articles cover dismissal for serious misconduct?"*
- *"Find case law on moral damages"*

## Installation

### 1. Download the plugin

👉 Download [`legifrance-piste.plugin`](https://github.com/Estelle812/legifrance-piste/releases/latest/download/legifrance-piste.plugin)

then in Claude Desktop:
Settings → Capabilities → Plugins → Install from file
Select the downloaded .plugin file.

### 2. Install `uv` (Python runtime, once only)

| OS | Command |
|----|---------|
| Windows | `winget install astral-sh.uv` |
| Mac/Linux | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

### 3. Set up PISTE credentials

After installing the plugin, type in Claude:

> **"setup piste"**

Claude will walk you through creating a free PISTE account and configuring your API keys.

## Requirements

- [Claude Desktop](https://claude.ai/download) installed
- Free account on [piste.gouv.fr](https://piste.gouv.fr) with Légifrance API subscription

## Disclaimer

Results are provided for informational purposes only and do not constitute legal advice.

## License

MIT © Estellou
