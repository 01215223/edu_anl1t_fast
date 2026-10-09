#!/usr/bin/env bash
# Buduje PDF z problem-set-01-odpowiedzi.md (wersja z odpowiedziami).
#
# Wymagania: pandoc (>= 3.x) oraz typst, np.:
#     pip install pypandoc_binary typst
#     # albo systemowo:  apt install pandoc  +  https://typst.app
#
# Użycie:  ./build-odpowiedzi-pdf.sh
set -euo pipefail

cd "$(dirname "$0")"

SRC=problem-set-01-odpowiedzi.md
OUT=problem-set-01-odpowiedzi.pdf
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

PANDOC=${PANDOC:-$(python3 -c 'import pypandoc;print(pypandoc.get_pandoc_path())' 2>/dev/null || command -v pandoc)}

# 1. Wariant pod Typst: \lvert/\rvert -> | (czysty Markdown zostaje bez zmian),
#     oraz tabela "Ściągawka" -> lista punktowana (tabele łamiące się przez
#     strony potrafią w Typst-ie nachodzić na siebie).
python3 - "$SRC" "$TMP/odp.md" <<'PY'
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
src = src.replace(r"\lvert", "|").replace(r"\rvert", "|")
ROW = re.compile(r"^\|\s*([0-9]+(?:\.[0-9]+)?)\s*\|\s*(.*?)\s*\|\s*$")
HEADER = re.compile(r"^\|\s*#\s*\|\s*Odpowied[zź]\s*\|\s*$")
lines, out, i = src.split("\n"), [], 0
while i < len(lines):
    if HEADER.match(lines[i]):
        i += 1                        # nagłówek tabeli — pomijamy
        i += 1                        # linia oddzielająca |---|---| — pomijamy
        items = []
        while i < len(lines) and (m := ROW.match(lines[i])):
            items.append(f"- **{m.group(1)}** — {m.group(2)}")
            i += 1
        out += [""] + items + [""]    # puste linie: lista nie może skleić się z akapitem
    else:
        out.append(lines[i])
        i += 1
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out))
PY

# 2. Markdown -> Typst -> PDF
"$PANDOC" "$TMP/odp.md" -o "$TMP/odp.typ" --to=typst --standalone --toc \
    -V title="Powtórzenie ze szkoły średniej — odpowiedzi"
python3 - "$TMP/odp.typ" "$OUT" <<'PY'
import typst, sys
data = typst.compile(sys.argv[1], format="pdf")
open(sys.argv[2], "wb").write(data)
print(f"{sys.argv[2]}: {len(data)} B")
PY
