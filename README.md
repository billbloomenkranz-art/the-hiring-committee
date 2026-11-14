# The Hiring Committee
A portable Claude simulator for rehearsing a difficult engineering hiring conversation. Morgan Vale is a **fictional** engineering director; Northline Process Systems is a **fictional** employer. No real credentials or confidential engineering records are needed.
## Quick start — Claude Project
1. Create a new Claude Project. Paste the contents of `CLAUDE.md` into **Project Instructions**.
2. Upload only `identity.md`, `rules.md`, `examples.md`, `reference/company.md`, `reference/case.md`, and `reference/interaction.md` as Project Knowledge. If the upload flattens paths, filenames are unique.
3. **Do not upload** `tests/`, this README, or other evaluator material.
4. In a fresh Project chat, type `START SIMULATION`. Respond as a senior project engineer candidate.
5. Type `END SESSION` to request a grounded feedback report. A normal "stop" ends without feedback, and tells you how to request it later.
## Scope
The simulator tests ownership, uncertainty, technical judgment, and communication under commercial pressure. It does not make hiring decisions. It must not request proprietary employer information.
## Files
`CLAUDE.md`: entrypoint; `identity.md`: persona; `rules.md`: conditional behavior; `examples.md`: varied dialogue examples; `reference/`: fictional setting, scenario, exit policy; `tests/`: external verification.
## Verification status
Static checks and independent Claude tests are distinct. Run `python3 tests/check_package.py` for static packaging checks. Use `tests/judge_protocol.md` for live tests and save transcripts. **Live Claude tests: not yet executed.**
## Limitations
The language model retains context within the chat but does not persist a formal state machine. Responses can vary across model versions and sessions. The examples are illustrative, not a deterministic script. This is a fictional training tool, not professional certification.