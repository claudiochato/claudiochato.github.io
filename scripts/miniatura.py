#!/usr/bin/env python3
"""Guarda em assets/miniaturas/ a miniatura de cada post do Instagram.

  python3 scripts/miniatura.py                    posts de data/links.yaml sem miniatura
  python3 scripts/miniatura.py URL [URL ...]      posts indicados (substitui as existentes)
  python3 scripts/miniatura.py URL --ficheiro F   usa uma imagem guardada à mão
"""
import argparse
import html
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "assets" / "miniaturas"
DADOS = RAIZ / "data" / "links.yaml"

RE_POST = re.compile(r"https://(?:www\.)?instagram\.com/(?:[\w.]+/)?(?:p|reel|tv)/([\w-]+)")
RE_META = re.compile(r"<meta\b[^>]*>", re.I)
RE_EMBED = re.compile(r'<img\b[^>]*class="[^"]*EmbeddedMediaImage[^"]*"[^>]*>', re.I)
RE_ATRIBUTO = r'\b%s="([^"]*)"'
ANFITRIOES = ("cdninstagram.com", "fbcdn.net")
MAX_BYTES = 20 * 1024 * 1024


class Falha(Exception):
    pass


def codigo_do_post(url):
    m = RE_POST.match(url)
    if not m:
        raise Falha(f"não parece um post do Instagram: {url}")
    return m.group(1)


def atributo(tag, nome):
    m = re.search(RE_ATRIBUTO % nome, tag, re.I)
    return html.unescape(m.group(1)) if m else None


def imagem_na_pagina(pagina):
    for tag in RE_META.findall(pagina):
        if atributo(tag, "property") == "og:image":
            return atributo(tag, "content")
    m = RE_EMBED.search(pagina)
    return atributo(m.group(0), "src") if m else None


def anfitriao_permitido(url):
    p = urllib.parse.urlparse(url)
    return p.scheme == "https" and any(
        p.hostname == a or (p.hostname or "").endswith("." + a) for a in ANFITRIOES
    )


def extensao(dados):
    if dados.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if dados.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if dados[:4] == b"RIFF" and dados[8:12] == b"WEBP":
        return ".webp"
    raise Falha("o conteúdo recebido não é uma imagem JPEG, PNG ou WebP")


def obter(url):
    with urllib.request.urlopen(url, timeout=30) as resposta:
        dados = resposta.read(MAX_BYTES + 1)
    if len(dados) > MAX_BYTES:
        raise Falha(f"resposta demasiado grande: {url}")
    return dados


def descarregar(codigo):
    for caminho in (f"p/{codigo}/", f"p/{codigo}/embed/"):
        try:
            pagina = obter(f"https://www.instagram.com/{caminho}").decode("utf-8", "replace")
        except urllib.error.URLError:
            continue
        imagem = imagem_na_pagina(pagina)
        if imagem and anfitriao_permitido(imagem):
            return obter(imagem)
    raise Falha(
        "o Instagram não devolveu a imagem sem sessão iniciada. "
        "Guarda a imagem à mão e usa --ficheiro."
    )


def guardar(codigo, dados):
    ext = extensao(dados)
    PASTA.mkdir(parents=True, exist_ok=True)
    for antiga in PASTA.glob(f"{codigo}.*"):
        antiga.unlink()
    destino = PASTA / f"{codigo}{ext}"
    destino.write_bytes(dados)
    return destino


def urls_em_falta():
    urls = RE_POST.findall(DADOS.read_text(encoding="utf-8"))
    return [c for c in dict.fromkeys(urls) if not any(PASTA.glob(f"{c}.*"))]


def main():
    parser = argparse.ArgumentParser(description="Guarda as miniaturas dos posts do Instagram.")
    parser.add_argument("urls", nargs="*", help="URLs dos posts")
    parser.add_argument("--ficheiro", type=Path, help="imagem local a usar (com um único URL)")
    args = parser.parse_args()

    if args.ficheiro and len(args.urls) != 1:
        parser.error("--ficheiro precisa de exatamente um URL")

    erros = 0
    try:
        codigos = [codigo_do_post(u) for u in args.urls] or urls_em_falta()
    except Falha as e:
        print(f"Erro: {e}", file=sys.stderr)
        return 1
    if not codigos:
        print("Não há miniaturas em falta.")
    for codigo in codigos:
        try:
            dados = args.ficheiro.read_bytes() if args.ficheiro else descarregar(codigo)
            print(f"{codigo}: {guardar(codigo, dados).relative_to(RAIZ)}")
        except (Falha, OSError) as e:
            print(f"{codigo}: {e}", file=sys.stderr)
            erros += 1
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
