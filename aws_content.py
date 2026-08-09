"""Content for AWS_Interview_Theory.docx.

Resume-aligned: ECS, ECR, App Runner, IAM, ALB are on Sanket's resume, so those
get extra depth - interviewers probe what the resume claims. 3-YOE level,
simple English, CLI/config example per topic.
Run:  python build_docx.py aws
"""

DOC_TITLE = "AWS / Cloud Interview Theory Notes"
DOC_SUBTITLE = "Resume-aligned (ECS, ECR, App Runner, IAM, ALB)  |  3-YOE depth  |  Sanket Kolhe"

CONTENT = [
    {
        "phase": "AWS Phase 1 - Core Concepts",
        "topics": [
            {
                "title": "A1.1  What is AWS - Regions, AZs, Shared Responsibility",
                "what": "AWS is the largest cloud platform - on-demand compute, storage and services, organized into regions made of isolated availability zones.",
                "points": [
                    "Cloud value: no upfront hardware, pay per use, scale up/down in minutes, managed services replace ops work.",
                    "Region = a geographic area (ap-south-1 is Mumbai); AZ = one or more isolated data centers inside it, with independent power/network.",
                    "High availability = running across multiple AZs - an AZ failure does not take the app down. Multi-region is for disaster recovery and global latency.",
                    "Data residency: choosing the region controls where data physically lives (matters for Indian fintech/compliance).",
                    "Shared responsibility model (asked often): AWS secures the cloud (hardware, network, hypervisor); WE secure what is in it (IAM, security groups, patching, data encryption, app code).",
                    "Interact via console, CLI, SDKs (boto3 in Python) and IaC (Terraform/CloudFormation).",
                ],
                "example": "aws configure   # keys + region\naws ec2 describe-availability-zones \\\n  --region ap-south-1\n# ap-south-1a, ap-south-1b, ap-south-1c",
                "answer": "AWS gives on-demand infrastructure and managed services, organized as regions containing isolated AZs - high availability means spreading across AZs, like Mumbai's three. The shared responsibility model splits security: AWS secures the infrastructure, we secure IAM, network rules, data and code. I work with it via CLI, boto3 and CI/CD.",
            },
            {
                "title": "A1.2  IAM - Users, Roles, Policies",
                "what": "IAM controls who can do what in the account - identities (users, roles) get JSON policies granting specific actions on specific resources.",
                "points": [
                    "User = a person/long-term credential; Group = users sharing policies; Role = an identity ASSUMED temporarily - by services, apps or people - with auto-rotating credentials.",
                    "Policy = JSON: Effect (Allow/Deny), Action (s3:GetObject), Resource (ARN), optional Condition. Explicit Deny always wins.",
                    "The key practice: ROLES for apps, never access keys in code. An ECS task role or EC2 instance profile gives the app S3/DB access with no stored secrets - this is what interviewers want to hear.",
                    "Least privilege: grant the minimum actions on the minimum resources - s3:GetObject on one bucket, not s3:* on *.",
                    "Root account: enable MFA, create an admin IAM user, never use root day-to-day, never make root access keys.",
                    "Identity-based policies attach to identities; resource-based (bucket policies) attach to resources; both evaluate together.",
                    "My use: task roles for ECS services, a CI role for Jenkins deploys, scoped user for local dev.",
                ],
                "example": "{\n  \"Effect\": \"Allow\",\n  \"Action\": [\"s3:GetObject\",\n             \"s3:PutObject\"],\n  \"Resource\":\n    \"arn:aws:s3:::mailflow-media/*\"\n}\n# attach to an ECS task ROLE, not keys",
                "answer": "IAM identities get JSON policies - action, resource, effect, with explicit deny winning. The practice that matters: applications use roles (ECS task roles, instance profiles) with temporary auto-rotated credentials, never embedded access keys; humans get least-privilege users with MFA, and root stays locked away. I scope policies to exact actions on exact ARNs.",
            },
            {
                "title": "A1.3  EC2",
                "what": "EC2 is a virtual server - we pick the instance type, an AMI image, attach storage and security groups, and manage it ourselves.",
                "points": [
                    "Instance types: t-family burstable (t3.micro dev), m general, c compute-heavy, r memory-heavy - sized as vCPU + RAM.",
                    "AMI = the machine image (OS + preinstalled stack) an instance boots from; custom AMIs bake our app for fast scaling.",
                    "EBS = network-attached persistent disk, survives stop/start, snapshots to S3 for backup; instance-store is ephemeral.",
                    "Security group = stateful instance-level firewall: allow inbound 443 from anywhere, 22 from office IP only; return traffic auto-allowed.",
                    "Key pairs for SSH - better: SSM Session Manager (no open port 22, audited access) - modern answer.",
                    "User data script runs at first boot (install docker, join cluster).",
                    "EC2 vs managed: EC2 = full control + full patching burden; that trade is why containers/serverless exist.",
                ],
                "example": "aws ec2 run-instances \\\n  --image-id ami-0abcd1234 \\\n  --instance-type t3.small \\\n  --key-name prod-key \\\n  --security-group-ids sg-0123 \\\n  --user-data file://install-docker.sh",
                "answer": "EC2 is IaaS: pick instance family and size, boot from an AMI, attach EBS volumes and a stateful security-group firewall. I know burstable vs compute vs memory families, user-data bootstrap scripts, SSM Session Manager over open SSH, and the trade-off - full control but full patching responsibility, which is why my deployments moved to ECS.",
            },
            {
                "title": "A1.4  S3",
                "what": "S3 is durable object storage - files as objects in globally-unique buckets, accessed by key over HTTP, with storage classes for cost.",
                "points": [
                    "Object storage, not a filesystem: key -> object (up to 5TB) + metadata; 'folders' are just key prefixes.",
                    "11 nines durability - data is replicated across AZs automatically.",
                    "Storage classes: Standard (hot), Standard-IA (infrequent), Glacier tiers (archive) - lifecycle rules auto-move objects (logs to IA at 30 days, Glacier at 90, delete at 365).",
                    "Security: buckets are private by default; Block Public Access stays ON; access via IAM/bucket policies; encryption at rest is default now.",
                    "Presigned URLs: temporary signed links for upload/download - THE pattern for user files (browser uploads direct to S3, app never proxies bytes).",
                    "Versioning protects against overwrite/delete; replication copies cross-region.",
                    "Uses: media files (Django/FastAPI uploads), static hosting, backups, data lake for analytics.",
                ],
                "example": "url = s3.generate_presigned_url(\n  \"put_object\",\n  Params={\"Bucket\": \"mailflow-media\",\n          \"Key\": f\"uploads/{fname}\"},\n  ExpiresIn=300)\n# browser PUTs directly to S3",
                "answer": "S3 stores objects by key in private-by-default buckets with eleven-nines durability, tiered storage classes and lifecycle rules moving data to IA and Glacier over time. My working patterns: IAM-scoped access with Block Public Access on, presigned URLs so clients upload directly without proxying through the app, and versioning for accident protection.",
            },
            {
                "title": "A1.5  VPC Basics",
                "what": "A VPC is our private network in AWS - subnets split it across AZs, route tables and gateways control traffic, SGs and NACLs filter it.",
                "points": [
                    "VPC = an isolated network with a CIDR range (10.0.0.0/16); everything (EC2, ECS, RDS) lives inside one.",
                    "Public subnet: route to an Internet Gateway - load balancers and NAT live here. Private subnet: no direct internet - app containers and databases live here. Standard layout: public + private per AZ.",
                    "NAT Gateway lets private resources reach OUT (pip install, external APIs) while nothing reaches in.",
                    "Security group: stateful, instance-level, allow-only rules - primary tool. NACL: stateless subnet-level allow/deny - rarely customized; the SG-vs-NACL contrast is a favorite question.",
                    "The security pattern: ALB's SG open to the world; app SG allows only from ALB's SG; DB SG allows 5432 only from app SG - SG-referencing chains, no CIDRs.",
                    "VPC endpoints reach S3/AWS APIs privately without internet transit.",
                ],
                "example": "VPC 10.0.0.0/16\n  public-a  10.0.1.0/24  (ALB, NAT)\n  private-a 10.0.11.0/24 (ECS tasks)\n  private-b 10.0.12.0/24 (RDS)\nDB SG: allow 5432 from app-SG only",
                "answer": "A VPC is the private network: public subnets hold the ALB and NAT gateway, private subnets hold app containers and the database, which reach out through NAT but accept nothing inbound. Security groups are stateful allow-lists chained by reference - ALB to app to DB - while NACLs are stateless subnet filters that mostly stay default. That layered layout is my standard deployment.",
            },
            {
                "title": "A1.6  Pricing Model",
                "what": "AWS bills pay-per-use - compute by time, storage by GB-month, data transfer OUT by GB - with discounts for commitment and interruption tolerance.",
                "points": [
                    "On-demand: full price, no commitment - default for unpredictable loads.",
                    "Reserved/Savings Plans: 1-3 year commitment for up to ~70% off - for steady baseline load.",
                    "Spot: spare capacity ~90% off, reclaimable with 2-minute notice - batch jobs, CI runners, fault-tolerant workers; never the only copy of stateful services.",
                    "Data transfer: IN free, OUT to internet billed - and cross-AZ transfer costs too; a favorite surprise-bill source.",
                    "NAT Gateway hourly + per-GB is the classic silent cost; idle provisioned resources (unused EIPs, oversized RDS) are the other.",
                    "Free tier covers t-micro instances, small RDS, S3/Lambda allowances - enough for demos.",
                    "Guardrails: billing alerts + budgets on day one; tags per project/env make bills explainable.",
                ],
                "example": "aws budgets create-budget ... \\\n  --budget '{\"BudgetLimit\":\n    {\"Amount\":\"50\",\"Unit\":\"USD\"},\n    \"TimeUnit\":\"MONTHLY\",\n    \"BudgetType\":\"COST\"}'",
                "answer": "Compute bills by time, storage by GB-month, and egress by GB - transfer out and cross-AZ traffic are the classic surprises, NAT Gateway the classic silent cost. On-demand for spiky load, Savings Plans for the steady baseline, Spot at ~90% off for interruptible work like batch and CI. I set budgets and billing alarms on day one and tag everything.",
            },
        ],
    },
]
