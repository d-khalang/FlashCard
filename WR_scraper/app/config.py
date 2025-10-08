from __future__ import annotations


BASE = "https://www.wordreference.com/conj/itverbs.aspx"
HEADERS = {
"User-Agent": "StudyScraper/1.0 (+contact: you@example.com)",
}


# Toggle to raise on missing sections (otherwise only warn to stderr)
STRICT_CHECKS = False


# Expected structure on WordReference Italian conjugations
EXPECTED = {
"indicativo": {"presente", "imperfetto", "passato remoto", "futuro semplice"},
"tempi composti": {"passato prossimo", "trapassato prossimo", "trapassato remoto", "futuro anteriore"},
"congiuntivo": {"presente", "imperfetto", "passato", "trapassato"},
"condizionale": {"presente", "passato"},
"imperativo": {"presente"},
}


# Stable orders for person labels
PERSON_ORDER_DEFAULT = [
"io", "tu", "lui, lei, Lei, egli", "noi", "voi", "loro, Loro, essi"
]
PERSON_ORDER_IMPERATIVE = [
"", "(tu)", "(Lei)", "(noi)", "(voi)", "(Loro)"
]