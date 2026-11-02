# briefkit

Lint Orchestrator briefs: 5 must-haves, AC checkboxes, risk class, forbidden areas. Python 3.11+, stdlib only.

## Usage
```bash
python -m briefkit examples/good-brief.md   # exit 0
python -m briefkit examples/bad-brief.md    # exit 1
```

## Rules
Required sections (markdown headings, case-insensitive): `Goal`, `Pass/Fail`, `Proof type`, `Risk class`, `Forbidden`.
- Acceptance criteria contain at least one `- [ ]` / `- [x]` checkbox.
- Risk class is one of `low, auth, payments, migration, public-api, infra`.

## Test
```bash
python -m unittest discover tests
```

## License
MIT
