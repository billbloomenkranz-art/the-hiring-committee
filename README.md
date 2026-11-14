# The Hiring Committee
A portable Claude simulator for rehearsing a difficult engineering hiring conversation. Morgan Vale is the fictional chair of Northline's hiring committee and conducts the initial interview alone; the "committee" is the screening process, not multiple personas.
## Quick start — Claude Project
1. Create a new Claude Project. Paste `CLAUDE.md` into Project Instructions.
2. Upload only `identity.md`, `rules.md`, `examples.md`, `reference/company.md`, `reference/case.md`, and `reference/interaction.md` as Project Knowledge. If paths flatten, filenames remain unique.
3. **Do not upload** `tests/`, README, or evaluator files.
4. In a fresh chat type `START SIMULATION` or simply "Hello, I'm ready." Respond as a senior engineering candidate. You may request the technical scenario early.
5. Type `END SESSION` (case and punctuation flexible) for a Hiring Committee Screening Memo. An ordinary stop exits without evaluation, with an optional pointer to feedback.
## Scope and safety
Tests ownership, uncertainty, technical judgment, and communication under pressure. Fictional people/company/case only; no real credentials or confidential employer records required. Truthful AI disclosure and immediate exit are intentional.
## Files
`CLAUDE.md` entrypoint; `identity.md` persona; `rules.md` conditional logic; `examples.md` examples; `reference/` setting/case/debrief; `tests/` external verification.
## Verification
Run `python3 tests/check_package.py` for static checks. Use `tests/judge_protocol.md` to conduct ten independent live Claude tests, keeping actual transcripts in `runs/` if executed. **Live Claude tests: 0/10 recorded.** Static review is not live testing.
## Limitations
No persistent formal state; behavior varies with model/session. This is a fictional training tool, not an actual hiring decision. Prompt disclosure resistance is specified, not proven.