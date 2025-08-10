# Government Enterprise AtScale Platform

This is the main landing page for the Government Enterprise AtScale Platform (GEAP).

## What is AtScale
AtScale is a semantic layer that enables governed metrics and dimensional modeling on top of cloud data platforms, and connects to BI tools like Excel, Power BI, and Tableau.

**Vendor Official Link:** https://www.atscale.com/

## Sourcing
PIF #: **PIF22098**  <!-- update if needed -->

## Contact Details
| Role                      | Name                      | Email                               |
|--------------------------|---------------------------|-------------------------------------|
| Delivery Manager         | Melbin Rethin Dhasan      | Melbin.RethinDhasan@cignahealthcare.com |
| Product Owner / Team Lead| Mark Isaacson             | Mark.Isaacson@cignaHealthcare.com   |
| Developer                | Harika Irrinki            | Harika.Irrinki@cignaHealthcare.com  |
| Developer                | Venkata Jagadeesh Chappidii | VenkataJagadeesh.Chappidii@cignaHealthcare.com |

> For Sev-1/Sev-2 issues, see **[Support](support.md)**.

## Glossary of Terms
1. **Semantic Layer** – A governed business layer that maps enterprise dimensions/measures to physical data.
2. **Aggregate** – Pre-computed summary table AtScale manages to accelerate queries.
3. **Cube** – A modeled dataset (dimensions, hierarchies, measures) published by AtScale.
4. **GEAP** – Government Enterprise AtScale Platform.

## Links to Child Pages
- **Onboarding**  
  - [Business Users](onboarding/business-users.md)  
  - [Developers / Data Engineers](onboarding/developers-data-engineers.md)
- **BI Connectivity**  
  - [Excel](connectivity/excel.md)  
  - [Power BI](connectivity/powerbi.md)  
  - [Tableau](connectivity/tableau.md)
- **Architecture & Accounts**  
  - [Architecture Overview](architecture/index.md)  
  - [AWS Account Details](architecture/aws-account-details.md)
- **Operational Docs**  
  - [Release Notes](release-notes/2025-08.md)  
  - [Known Issues](known-issues.md)  
  - [FAQs](faqs.md)  
  - [Support](support.md)

## Links to the GEAP AtScale Environments
- **DEV:** https://atscale.gov-solutions-dev.aws.zilverton.com:10500/login
- **TEST:** https://atscale.gov-solutions-test.aws.zilverton.com:10500/login
- **PROD:** https://atscale.gov-solutions.aws.zilverton.com:10500/login

**************
Subpage stubs (copy/paste)
onboarding/business-users.md

# Onboarding – Business Users

## Access
Join these Okta groups for read access to published cubes:
- `O_ATSCALE_READ_DEV`
- `O_ATSCALE_READ_TEST`
- `O_ATSCALE_READ`

## How to Log In
Use the environment links on the main page. Sign in with SSO.

## BI Connectivity
- [Excel](../connectivity/excel.md)
- [Power BI](../connectivity/powerbi.md)
- [Tableau](../connectivity/tableau.md)

onboarding/developers-data-engineers.md

# Onboarding – Developers / Data Engineers

## Access
Join Okta groups per environment:
- Designer: `O_ATSCALE_DESIGNER_DEV`, `O_ATSCALE_DESIGNER_TEST`, `O_ATSCALE_DESIGNER`
- Analyst:  `O_ATSCALE_ANALYST_DEV`,  `O_ATSCALE_ANALYST_TEST`,  `O_ATSCALE_ANALYST`
- Admin:    `O_ATSCALE_ADMIN_DEV`,    `O_ATSCALE_ADMIN_TEST`,    `O_ATSCALE_ADMIN`
- Read:     `O_ATSCALE_READ_DEV`,     `O_ATSCALE_READ_TEST`,     `O_ATSCALE_READ`

## Working in AtScale
1. **Create Project & Cube:** *Projects → New Project → Add New Cube*
2. **Cube Canvas:** Define dimensions, measures, calculated fields.
3. **Cube Matrix:** Manage relationships across dimensions/measures.
4. **Data Preview:** Validate logic before publish.
5. **Publish:** Select data source, finalize settings.
6. **Monitor:**  
   - **Queries** tab for inbound/outbound query usage  
   - **Aggregates** tab for usage/freshness of aggregates


connectivity/excel.md

# BI Connectivity – AtScale via Excel
1. Install AtScale Excel add-in (if required) or connect via OLAP.
2. Connect to server: use ENV URL (DEV/TEST/PROD).
3. Select published cube and drag fields into PivotTable.
4. Performance tips: use filters, avoid unconstrained grand totals.


connectivity/powerbi.md

# BI Connectivity – AtScale via Power BI
1. Get Data → **AtScale** (or OLE DB/SQL if connector not present).
2. Server: ENV URL, select cube.
3. Publish report to workspace; set refresh credentials (SSO where supported).


connectivity/tableau.md


# BI Connectivity – AtScale via Tableau
1. Connect → **AtScale**.
2. Server: ENV URL, sign in via SSO.
3. Choose cube → build workbook → publish to Server.


architecture/index.md

# Architecture Overview
- AtScale hosted in secure VPC behind a firewall.
- Uses NLB/ALB, NAT, and NAS services for routing and shared storage.
- Backups, configuration files, and logs are managed via S3 buckets.
- AtScale VMs are hosted in Zilverton Data Center.


support.md


# Support

For any issues, submit a ServiceNow ticket:

Choose **“AtScale”** under **Strategic Analytics Applications**  
ServiceNow: https://zilvertondev.service-now.com/sp?id=sc_cat_item&sys_id=37dc48ca87e36114dcf663973cbb351c


release-notes/2025-08.md

# Release Notes – 2025-08

## CHG0032026
- **Type:** New feature / defect fix / enhancement
- **Description:** (add change summary)
- **Prod status:** (date)


known-issues.md

# Known Issues (WIP)
- List any active issues impacting users, with workarounds/status.


faqs.md

# FAQs
- **Who gets access to cubes?** Business users via read groups; developers via designer/admin groups.
- **How do I request a new metric?** Open a ticket and tag the AtScale team; include business definition and data source.


