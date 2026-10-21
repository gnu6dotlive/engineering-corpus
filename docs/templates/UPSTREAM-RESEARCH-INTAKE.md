# Upstream research intake

Use this template when an external project changes something that may affect a local research or product rail.

## 1. Upstream fact

- Project:
- Exact revision / release:
- Date observed:
- Source:
- What actually changed:

## 2. Local evidence

- Owning repository:
- Contract / quest / gate:
- Exact local revision / artifact:
- Hardware/profile:
- Existing evidence:

## 3. Non-claims

State explicitly what the upstream change does **not** prove locally. Do not turn a vendor estimate, paper result, source-level capability or unrelated benchmark into a local qualification.

## 4. Smallest falsifiable experiment

- Hypothesis:
- Inputs / fixture:
- Control:
- Measurements:
- Oracle:
- Failure conditions:

## 5. Decision

Choose one:

- `ADOPT-CANDIDATE` — evidence supports a bounded implementation trial.
- `RESEARCH-ONLY` — useful donor, no implementation authorization.
- `BLOCKED` — missing artifact, hardware, provenance or oracle.
- `REJECTED` — evidence contradicts the local contract/hypothesis.
- `NO-IMPACT` — upstream change is real but does not materially affect the local rail.

## 6. Authority

Name the component that owns the decision. External technology does not silently acquire authority over a local contract.

## 7. Follow-up

Link the owning repository's issue/PR and record the next review trigger.
