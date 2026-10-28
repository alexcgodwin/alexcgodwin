"""Offline GitHub profile integrity: titles, links, assets and claim boundaries."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
README=(ROOT/'README.md').read_text(encoding='utf-8')
required={
 'cloud-platform-ansible','jenkins-ci-pipeline','cloud-app-gitops',
 'multi-region-disaster-recovery-platform','event-driven-serverless-platform',
 'aws-aiops-ssm-automation-platform','terraform-enterprise-state-recovery-lab',
 'terraform-module-validation-testing','azure-enterprise-landing-zone',
 'cloud-devops-mcp-server','gcp-enterprise-landing-zone'
}
missing=[r for r in sorted(required) if f'https://github.com/alexcgodwin/{r}' not in README]
if missing:raise SystemExit('Portfolio entries missing: '+', '.join(missing))
for relative in re.findall(r'<img[^>]+src="(\./assets/[^"?]+)',README):
 if not (ROOT/relative).is_file():raise SystemExit('Missing local image '+relative)
if '9.5/10' in README or 'senior-level project' in README.lower():
 raise SystemExit('Do not display self-awarded ratings')
print(f'Profile passed: {len(required)} critical projects and all local illustrations present')
