FINAL CAPSTONE - ARCHITECT THE 2030 ORGANIZATION

Student:
Mohammed Imad Uddin

Student ID:
F00611260


Cornerstone Relief International (CRI) is a 600-person relief and development
organization with field offices on four continents and a nine-person
headquarters IT team.

The design uses a hybrid, privacy-first AI architecture. Approved external
APIs may be used for low-sensitivity work, while restricted beneficiary
case-note RAG remains on a private controlled inference lane.

Human approval is required for irreversible, security-sensitive,
privacy-sensitive, financially material, or high-blast-radius actions.


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

Restricted beneficiary case notes are never sent to public consumer chatbots.

Private RAG uses identity-scoped retrieval and has no arbitrary outbound
egress.

Financial changes require out-of-band verification using trusted contact
information and a second named human approval.

Irreversible actions and security-boundary changes are not performed
unattended.

Each governed control has a named human owner, an artifact, and a gate or
review cadence.


AI HONESTY

The use of AI tools in the drafting, research aid, calculations and
configuration support. Final architecture, security, automation, cost and more
governance decisions were reviewed and accepted by the student.
