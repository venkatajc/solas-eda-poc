# AtScale Runbook

## 1. Architecture Overview
- AtScale is hosted in a secure VPC behind a firewall.
- Uses Route53, NAT, and NAS services for routing and shared storage.
- AtScale connects with BI tools like Tableau and Power BI.
- Backups, configuration files, and logs are managed via S3 buckets.
- AtScale VMs are hosted in Zilverton Data Center.

---

## 2. Onboarding Steps (by Role)

### ➤ Business User (Read Published Cubes)
- Join OKTA Groups:
  - DEV: `O_ATSCALE_READ_DEV`
  - TEST: `O_ATSCALE_READ_TEST`
  - PROD: `O_ATSCALE_READ`
- Login URLs:
  - DEV: `https://atscale.gov-solutions-dev.aws.zilverton.com:10500/login`
  - TEST: `https://atscale.gov-solutions-test.aws.zilverton.com:10500/login`
  - PROD: `https://atscale.gov-solutions.aws.zilverton.com:10500/login`
- Access: View published cubes only.

### ➤ Developer / Data Engineer
- Join OKTA Groups:
  - Designer: `O_ATSCALE_DESIGNER_DEV`, `O_ATSCALE_DESIGNER_TEST`, `O_ATSCALE_DESIGNER`
  - Analyst: `O_ATSCALE_ANALYST_DEV`, `O_ATSCALE_ANALYST_TEST`, `O_ATSCALE_ANALYST`
  - Admin: `O_ATSCALE_ADMIN_DEV`, `O_ATSCALE_ADMIN_TEST`, `O_ATSCALE_ADMIN`
  - Read: `O_ATSCALE_READ_DEV`, `O_ATSCALE_READ_TEST`, `O_ATSCALE_READ`
- Permissions: Full access to create, model, query, and publish projects.

---

## 3. Working with AtScale

### 🔹 Create Project & Cube
- Navigate to **Projects** → `+ New Project` → `+ Add New Cube`.
- Define name, visibility, and model schema.

### 🔹 Cube Canvas
- Design and organize dimensions, measures, and calculated fields.

### 🔹 Cube Matrix
- Tabular view of dimensions and measures to manage relationships.

### 🔹 Cube Data Preview
- Preview data from cube to validate logic before publishing.

### 🔹 Publish Project
- Click **Publish**, select data source, finalize settings.

### 🔹 View Queries
- Track inbound/outbound query usage from **Queries** tab.

### 🔹 View Aggregates
- Monitor usage and freshness of aggregates from **Aggregates** tab.

---

## 4. Points of Contact

If you have questions or concerns about AtScale login, please contact the AtScale Development Team:

| Name                     | Email Address                                        |
|--------------------------|------------------------------------------------------|
| Melbin Rethin Dhasan     | Melbin.RethinDhasan@CignaHealthcare.com              |
| Mark Isaacson            | Mark.Isaacson@CignaHealthcare.com                   |
| Harika Irinika           | Harika.Irinika@CignaHealthcare.com                  |
| Venkata Jagadeesh Chappidi| VenkataJagadeesh.Chappidi@CignaHealthcare.com       |

---

## 5. References & Links
- [AtScale Documentation](https://documentation.atscale.com/installer/atscale)
- Connectors:
  - [Connect via Excel](#)
  - [Connect via Power BI](#)
  - [Connect via Tableau](#)
