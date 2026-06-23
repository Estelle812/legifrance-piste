# /// script
# dependencies = [
#   "fastmcp",
#   "httpx[socks]",
# ]
# ///
"""
Serveur MCP Légifrance — mode HTTP pour déploiement Render
Les clés PISTE sont gérées côté serveur via variables d'environnement.
"""

import os
import time
import httpx
from fastmcp import FastMCP

OAUTH_URL = "https://oauth.piste.gouv.fr/api/oauth/token"
API_BASE  = "https://api.piste.gouv.fr/dila/legifrance/lf-engine-app"

CLIENT_ID     = os.environ.get("PISTE_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("PISTE_CLIENT_SECRET", "")
PORT          = int(os.environ.get("PORT", 8000))

mcp = FastMCP("Légifrance PISTE")

_token_cache: dict = {"token": None, "expires_at": 0}


def get_token() -> str:
    now = time.time()
    if _token_cache["token"] and now < _token_cache["expires_at"] - 30:
        return _token_cache["token"]
    r = httpx.post(OAUTH_URL, data={
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "openid",
    }, timeout=10)
    r.raise_for_status()
    data = r.json()
    _token_cache["token"] = data["access_token"]
    _token_cache["expires_at"] = now + data.get("expires_in", 3600)
    return _token_cache["token"]


def lf_post(path: str, payload: dict) -> dict:
    token = get_token()
    r = httpx.post(f"{API_BASE}{path}", json=payload, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }, timeout=15)
    r.raise_for_status()
    return r.json()


@mcp.tool()
def search_code(query: str, code: str = "LEGITEXT000006070721", max_results: int = 5) -> str:
    """
    Recherche dans un code juridique français.

    Args:
        query: Termes de recherche (ex: "responsabilité civile", "bail commercial")
        code: Identifiant Légifrance du code (défaut = Code civil).
              Code civil=LEGITEXT000006070721, Code du travail=LEGITEXT000006072050,
              Code de commerce=LEGITEXT000005634379, Code pénal=LEGITEXT000006070719
        max_results: Nombre de résultats (1-10, défaut : 5)
    """
    payload = {
        "recherche": {
            "champs": [{"typeChamp": "ALL", "criteres": [{"typeRecherche": "EXACTE", "valeur": query}]}],
            "filtres": [{"facette": "TEXT_LEGAL_STATUS", "valeur": "VIGUEUR"}],
            "pageNumber": 1, "pageSize": max_results,
            "operateur": "ET", "typePagination": "DEFAUT",
        },
        "fond": "CODE_DATE",
    }
    data = lf_post("/search", payload)
    results = data.get("results", [])
    if not results:
        return f"Aucun résultat pour « {query} »."
    lines = [f"Résultats pour « {query} » ({len(results)} trouvé(s)) :\n"]
    for r in results:
        titles = r.get("titles", [{}])
        title = titles[0].get("title", "Sans titre") if titles else "Sans titre"
        cid   = titles[0].get("id", "") if titles else ""
        lines.append(f"  • {title}")
        if cid:
            lines.append(f"    ID : {cid}")
            lines.append(f"    Lien : https://www.legifrance.gouv.fr/codes/article_lc/{cid}")
        sections = r.get("sections", [])
        if sections:
            extraits = sections[0].get("extracts", [])
            if extraits:
                texte = extraits[0].get("values", [""])[0]
                if texte:
                    lines.append(f"    Extrait : {texte[:250]}…")
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def search_jurisprudence(query: str, max_results: int = 5) -> str:
    """
    Recherche dans la jurisprudence judiciaire française.

    Args:
        query: Termes de recherche (ex: "préjudice moral", "licenciement abusif")
        max_results: Nombre de résultats (1-10, défaut : 5)
    """
    payload = {
        "recherche": {
            "champs": [{"typeChamp": "ALL", "criteres": [{"typeRecherche": "EXACTE", "valeur": query}]}],
            "filtres": [], "pageNumber": 1, "pageSize": max_results,
            "operateur": "ET", "typePagination": "DEFAUT",
        },
        "fond": "JURI",
    }
    data = lf_post("/search", payload)
    results = data.get("results", [])
    if not results:
        return f"Aucune jurisprudence trouvée pour « {query} »."
    lines = [f"Jurisprudence pour « {query} » ({len(results)} résultat(s)) :\n"]
    for r in results:
        titles = r.get("titles", [{}])
        title = titles[0].get("title", "Sans titre") if titles else "Sans titre"
        cid   = titles[0].get("id", "") if titles else ""
        lines.append(f"  • {title}")
        if cid:
            lines.append(f"    ID : {cid}")
        sections = r.get("sections", [])
        if sections:
            extraits = sections[0].get("extracts", [])
            if extraits:
                texte = extraits[0].get("values", [""])[0]
                if texte:
                    lines.append(f"    Extrait : {texte[:300]}…")
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def get_article(article_id: str) -> str:
    """
    Récupère le texte complet d'un article par son identifiant Légifrance.

    Args:
        article_id: Identifiant de l'article (ex: "LEGIARTI000006419280")
    """
    data = lf_post("/consult/getArticle", {"id": article_id})
    article = data.get("article", {})
    if not article:
        return f"Article introuvable : {article_id}"
    import re
    num   = article.get("num", "")
    titre = article.get("context", {}).get("titreTxt", "")
    texte = re.sub(r"<[^>]+>", "", article.get("texteHtml", article.get("texte", ""))).strip()
    return (
        f"Article {num} — {titre}\n"
        f"ID : {article_id}\n"
        f"Lien : https://www.legifrance.gouv.fr/codes/article_lc/{article_id}\n\n"
        f"{texte}"
    )


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=PORT)
