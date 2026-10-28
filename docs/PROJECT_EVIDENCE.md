# Portfolio evidence standards

Every project link in this profile is a separate repository with its own implementation scope. A green CI badge proves the automated checks passed, not production deployment. A deployable Terraform stack is not the same as an executed `terraform apply`, and a recovery simulation is not proof of a real RTO/RPO.

## How to evaluate the work

1. **Implementation:** inspect actual Terraform resources, Helm/Kubernetes manifests, Python/TypeScript automation, or Jenkins/Ansible scripts.
2. **Control boundaries:** review least-privilege access, managed secrets, CI approval gates, audit trails and rollback/restore procedures.
3. **Repeatability:** run documented tests; examine GitHub Actions results and reproducible local fixtures.
4. **Operations:** verify incident runbooks, failure injection, policy enforcement and state recovery steps.
5. **Deployment evidence:** distinguish local, CI, sandbox deployed, and continuously operated platforms with evidence links rather than broad claims.

## Representative engineering paths

- **Cloud platform delivery:** Azure Enterprise Landing Zone, GCP Enterprise Landing Zone, Kubernetes GitOps and Ansible-managed Linux.
- **AI-assisted operations:** Cloud DevOps MCP Server and AWS AIOps/Systems Manager automation with human remediation controls.
- **Reliability and delivery:** Terraform State Recovery, Jenkins Pipeline, Event-Driven Serverless and Multi-Region DR designs with optional AWS implementation examples.

The goal of this profile is to make architecture decisions and actual implementation easy to inspect. It is not a claim that each example is currently deployed in production.
