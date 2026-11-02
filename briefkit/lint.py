import re

REQUIRED = {"goal": "goal", "pass/fail": "pass/fail", "proof type": "proof type", "risk class": "risk class", "forbidden": "forbidden"}
RISKS = {"low", "auth", "payments", "migration", "public-api", "infra"}


def sections(text: str) -> dict[str, str]:
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^#{1,6}\s+(.*?)\s*$", line)
        if m:
            cur = m.group(1).strip().lower()
            out[cur] = ""
        elif cur is not None:
            out[cur] += line + "\n"
    return out


def lint(text: str) -> list[tuple[bool, str]]:
    secs = sections(text)
    res = []
    for key in REQUIRED:
        ok = any(h.startswith(key) for h in secs)
        res.append((ok, f"section '{key}' present"))
    ok = bool(re.search(r"^\s*[-*]\s+\[[ xX]\]\s+\S", text, re.M))
    res.append((ok, "acceptance criteria has >=1 checkbox"))
    body = next((v for h, v in secs.items() if h.startswith("risk class")), "")
    words = set(re.findall(r"[a-z-]+", body.lower()))
    found = words & RISKS
    res.append((bool(found), f"risk class in {sorted(RISKS)}" + (f" (found: {', '.join(sorted(found))})" if found else "")))
    return res
