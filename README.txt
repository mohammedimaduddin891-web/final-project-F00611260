FINAL CAPSTONE - ARCHITECT THE 2030 ORGANIZATION

Student:
Mohammed Imad Uddin

Student ID:
F00611260


Cornerstone Relief International (CRI) is a 600 person, relief and development organization.
Continental continents and 28 countries.Main headquarters staff of nine and staff at 48 countries and their field offices around the world.
continents.

A hybrid architecture with privacy-first AI is used for the design. Low-sensitivity work
may be based on approved external API's. Restricted Beneficiary Case note RAG is still pending.
on a private controlled inferred lane. It requires human judgement to be applied to:
indelible, secure, private, monetary sensitive and
high-blast-radius actions.


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


REAL VALIDATION EVIDENCE

Cost model:
output/estate-cost.txt

Actual workload:
500M tokens/month
400M input / 100M output

Actual API examples from the supplied course-price model:
claude-haiku-4-5:  $900/month
claude-sonnet-4-6: $2,700/month
gpt-5.5:           $5,000/month
gemini-3-flash:    $500/month

Illustrative self-host node:
8xH100
$22,000/month
1.5B-token monthly capacity
3.0x headroom at the 500M-token workload
$44.00/1M tokens at the measured workload

Actual theoretical crossover results:
claude-haiku-4-5:  12.22B tokens/month
claude-sonnet-4-6: 4.07B tokens/month
gpt-5.5:           2.20B tokens/month
gemini-3-flash:    22.00B tokens/month

Every crossover is above the supplied node's 1.5B-token monthly capacity.

Autonomy validation:
tiers: ['act', 'approve', 'observe', 'recommend']
AUTONOMY LADDER PASS

YAML validation:
code/inference-platform.yaml: YAML PASS
code/autonomy-ladder.yaml: YAML PASS

Governance validation:
10 controls

Required-document validation:
PASS for all eight required documents.

Reference-file validation:
PASS for all four adapted reference files.

Final shell validation:
CAPSTONE NORMAL TIER EVIDENCE PASS


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
    print(f"{name}: YAML PASS")
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

print(
    "AUTONOMY LADDER PASS"
    if required <= tiers
    else "AUTONOMY LADDER FAIL"
)
PY


SAFETY AND DESIGN POSITION

The guard position is optional and designed to protect the worker's safety.

Only consumer case notes that have been restricted are fed into the public consumer chatbots.

Private RAG only supports identity scoped retrieval and no arbitrary outbound egress.

Financial changes must be verified by an out-of-band number that is known, and there must be two names.
human approvals.

There are no irreversible and security-boundary actions that are unattended.

Each governed control has a human named owner, an artefact and a gate or
cadence.


AI HONESTY

The use of AI tools in the drafting, research aid, calculations and
configuration support. Final architecture, security, automation, cost and more
governance decisions were reviewed and accepted by the student.
