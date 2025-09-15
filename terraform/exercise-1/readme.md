# Load-Balanced Web Server Environment (exercise-1)

## Overview

This Terraform project builds a simple load-balanced web server environment on AWS using:

* An Internet-facing Application Load Balancer (ALB)
* Two EC2 instances running **nginx** (user-data installs nginx and serves a "Hello SuperOps" page)
* Target group and listener to route HTTP(80) traffic to the instances
* VPC, subnets (two AZs), route table, Internet Gateway, security groups, and related networking resource `s

> **Goal:** `curl` the ALB DNS should return a "Hello World / Hello SuperOps" page. If one instance is removed, the ALB should continue to serve traffic from the remaining instance.

---

## Files in this repo

* `main.tf` — Terraform resources and infrastructure
* `variables.tf` — input variables
* `outputs.tf` — useful outputs (ALB DNS, target group ARN, listener ID)
* `userdata.sh` — EC2 userdata script that installs nginx and serves a static page

---

## Prerequisites

* Terraform
* An AWS account with suitable privileges
* AWS credentials configured as environment variables

---

## What to configure before running

1. Configure your AWS credentials as env variables in windows. You can use below command.

    ```bash
    setx AWS_ACCESS_KEY_ID "access_key"
    setx AWS_SECRET_ACCESS_KEY "secret_key"
    setx AWS_DEFAULT_REGION "aws_region"
    ```

2. Adjust variables in `variables.tf` (VPC/ subnet names, region if required)

---

## Deploy

```bash
# from repository root
terraform init
terraform plan
terraform apply
```

If prompted for variables, pass them via `-var` or create a `terraform.tfvars` file.

---

## Verify

1. Get the ALB DNS from Terraform output or AWS console:

```bash
terraform output -raw load_balancer_dns
```

2. `curl` the ALB DNS to confirm page:

```bash
curl http://<ALB_DNS_NAME>
# expected: Hello SuperOps from <instance-hostname>
```

3. Failover test:

* **Terminate one instance from AWS console** and re-run `curl` to ensure the ALB serves from the remaining instance.


## Destroy

```bash
terraform destroy
```

> Always run `terraform destroy` to avoid unexpected charges.

---