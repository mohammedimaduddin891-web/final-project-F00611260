FINAL CAPSTONE - ARCHITECT THE 2030 ORGANIZATION

Student:
Mohammed Imad Uddin

Student ID:
F00611260

Tier:
Normal


SCENARIO

Cornerstone Relief International (CRI)

600-person relief organization

Nine-person headquarters IT team

Field offices on four continents


REQUIRED DOCUMENTS

architecture.docx
ai-strategy.txt
automation-plan.txt
security-plan.txt
cost-analysis.txt
governance.txt
REPORT.docx
agent-log.txt


ADAPTED REFERENCE FILES

code/inference-platform.yaml
code/autonomy-ladder.yaml
code/governance-checklist.txt
code/estate_cost.py


RUN COST MODEL

source "$HOME/capstone-venv/bin/activate"

python3 code/estate_cost.py |
  tee output/estate-cost.txt


VALIDATE PYTHON

python3 -m py_compile \
  code/estate_cost.py


VALIDATE YAML

python3 - <<'PY'
import yaml

from pathlib import Path

for name in [
    "code/inference-platform.yaml",
    "code/autonomy-ladder.yaml",
]:

    yaml.safe_load(
        Path(name).read_text(
            encoding="utf-8"
        )
    )

    print(
        f"{name}: YAML PASS"
    )
PY


CHECK AUTONOMY TIERS

python3 - <<'PY'
import yaml

from pathlib import Path

data = yaml.safe_load(
    Path(
        "code/autonomy-ladder.yaml"
    ).read_text(
        encoding="utf-8"
    )
)

tiers = {
    action["tier"]
    for action in data["actions"]
}

print(
    "tiers:",
    sorted(tiers)
)

required = {
    "observe",
    "recommend",
    "approve",
    "act",
}

if required <= tiers:

    print(
        "AUTONOMY LADDER PASS"
    )

else:

    print(
        "AUTONOMY LADDER FAIL"
    )
PY


SAFETY AND DESIGN POSITION

Restricted beneficiary case notes never go to public consumer chatbots.

Private RAG uses identity-scoped retrieval and no arbitrary outbound egress.

Financial changes require known-number out-of-band verification and two human
approvals.

Irreversible and security-boundary actions are not unattended.

Every governed control has:

a named human owner;
an artifact;
a gate or cadence.


AI HONESTY

AI was used for drafting, research organization, sizing math, and configuration
scaffolding.

The student owns the architecture and governance judgments and must be able to
defend them during the live session.
