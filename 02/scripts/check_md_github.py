"""Checks a Markdown file for constructs that GitHub renders badly.

Checks (conservative, based on GitHub's MathJax-based math rendering and GFM tables):
  * every LaTeX macro is in a common allow-list (GitHub rejects some macros, e.g. \\operatorname,
    \\text, \\,, \\big; the exact list is not published, so only very common macros are allowed);
  * no raw '<' or '>' inside math (they are escaped to &lt; / &gt; by GitHub);
  * no '|' inside math on a table row (GFM splits the row at every '|');
  * every '$$' display block starts on its own line and is preceded by a blank line;
  * dollar signs are balanced on each line (outside code spans and display blocks);
  * no unescaped '_' or '*' in plain text outside math and code (they would start emphasis/subscripts).

Usage: python check_md_github.py FILE.md [FILE.md ...]
Exits with status 1 if any problem is found.
"""
import re
import sys

ALLOWED = {
    # structure and sizes
    "left", "right", "big", "Big", "bigl", "bigr", "dfrac", "tfrac", "frac", "sqrt", "cdot", "qquad", "quad",
    "dots", "ldots", "cdots",
    # relations and operators
    "le", "ge", "lt", "gt", "leq", "geq", "neq", "approx", "in", "notin", "subset", "subseteq",
    "to", "mapsto", "iff", "implies", "pm", "mp", "setminus", "cup", "cap", "infty", "cdot",
    # Greek and sets
    "pi", "theta", "alpha", "beta", "gamma", "delta", "varepsilon", "epsilon", "lambda", "mu", "sigma",
    "mathbb", "mathrm", "mathbf", "text",
    # functions
    "sin", "cos", "tan", "cot", "sec", "csc", "log", "ln", "exp", "lim",
    "arcsin", "arccos", "arctan", "arccot", "sinh", "cosh", "tanh",
    "max", "min", "sup", "inf", "det",
}
# Macros that are known to be rejected by GitHub or are not in the allow-list above
# are reported. Escaped braces/backslashes are not macros.
MACRO = re.compile(r"\\([A-Za-z]+)")
# Spacing and escaped symbols that GitHub may reject; reported explicitly.
SUSPECT = {"operatorname", "text", "big", "Big", "bigl", "bigr", "quad", "qquad", ",", ";", "!"}


def split_math(line):
    """Return (text_outside_math, math_spans) for a single line (inline $...$ only)."""
    outside, spans, pos = [], [], 0
    for m in re.finditer(r"(?<!\\)\$(.+?)(?<!\\)\$", line):
        outside.append(line[pos:m.start()])
        spans.append(m.group(1))
        pos = m.end()
    outside.append(line[pos:])
    return "".join(outside), spans


def check_file(path):
    problems = []
    lines = open(path, encoding="utf-8").read().split("\n")
    in_display = False
    in_code = False
    prev_blank = True
    for i, line in enumerate(lines, 1):
        where = f"{path}:{i}"
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            prev_blank = False
            continue
        if in_code:
            continue
        if stripped == "$$":
            if not in_display and not prev_blank:
                problems.append(f"{where}: '$$' block not preceded by a blank line")
            in_display = not in_display
            prev_blank = False
            continue
        if in_display:
            math_text = line
            # display math content
            _check_math(math_text, where, problems)
            prev_blank = False
            continue

        if re.search(r"\$\$.+\$\$", line):
            problems.append(f"{where}: '$$...$$' on one line (put the formula on its own lines)")
        outside, spans = split_math(line)
        if line.count("$") % 2:
            problems.append(f"{where}: unbalanced '$' on this line")
        for s in spans:
            _check_math(s, where, problems)
        if line.lstrip().startswith("|") and any("|" in s for s in spans):
            problems.append(f"{where}: '|' inside math in a table row (split by GFM)")
        plain = re.sub(r"`[^`]*`", "", outside)
        if re.search(r"(?<![\\\w])_|(?<!\*)\*(?!\*)", plain.replace("**", "")):
            # bare underscore or asterisk outside math: check it is not part of an emphasis pair
            if re.search(r"(?<![\w])_\w|\w_(?!\w)", plain):
                problems.append(f"{where}: '_' outside math may be read as emphasis")
        prev_blank = stripped == ""
    if in_display:
        problems.append(f"{path}: unclosed '$$' block")
    return problems


def _check_math(text, where, problems):
    if re.search(r"[<>]", text):
        problems.append(f"{where}: raw '<' or '>' in math (use \\lt / \\gt)")
    for name in MACRO.findall(text):
        if name in SUSPECT or name not in ALLOWED:
            problems.append(f"{where}: macro \\{name} is not in the allow-list")
    for sym in re.findall(r"\\([,;!:])", text):
        problems.append(f"{where}: spacing command \\{sym} (not in the allow-list)")


def main(paths):
    problems = []
    for p in paths:
        problems += check_file(p)
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s) found in {len(paths)} file(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
