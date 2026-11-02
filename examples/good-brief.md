# Brief: add /health endpoint

## Goal
Expose GET /health returning {"ok": true}.

## Acceptance criteria
- [ ] GET /health returns 200
- [ ] Body is {"ok": true}

## Pass/Fail
Pass when raw HTTP against preview returns 200 with the body above.

## Proof type
raw_http

## Risk class
low

## Forbidden
Do not touch auth/, billing/, or migrations/.
