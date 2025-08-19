:root {
  --md-primary-fg-color: #ffffff;
  --md-primary-bg-color: #ffffff;
  --md-default-fg-color: #111827;
  --md-default-fg-color--light: #374151;
  --md-default-fg-color--lighter: #6b7280;
  --md-accent-fg-color: #6b7280;
  --md-typeset-a-color: #374151;
}

.md-header, .md-tabs { box-shadow: inset 0 -1px 0 #e5e7eb; }
.md-sidebar__scrollwrap { border-right: 1px solid #f3f4f6; }
.md-nav__title { font-weight: 700; }

/* Style the built-in disclosure arrow */
.md-nav__item--nested > .md-nav__link::after {
  color: #6b7280;
  font-size: 0.7rem;
  transform: rotate(0deg);
  transition: transform .2s;
}
.md-nav__item--active > .md-nav__link::after { transform: rotate(90deg); }

/* Subtle active/hover */
.md-nav__link--active, .md-nav__link:focus, .md-nav__link:hover { color: #111827; }
.md-nav__item .md-nav__link--active { font-weight: 600; }
.md-typeset h1, .md-typeset h2, .md-typeset h3 { color: #111827; }
.md-typeset a:hover { text-decoration: underline; }

.md-nav__title {
  margin-bottom: 1rem;
}
/* Line only above AtScale */
.md-nav__link[href$="atscale/"] {
  border-top: 1px solid #e5e7eb;
  margin-top: 0.75rem;
  padding-top: 0.5rem;
  font-weight: 600;
}

/* Bold main collapsible sections in the sidebar */
.md-nav__item--nested > .md-nav__link {
  font-weight: 700;   /* stronger emphasis */
  color: #111827;     /* dark text */
}

/* Keep children normal */
.md-nav__item--nested .md-nav__link {
  font-weight: 400;
}

/* Optional: add separator line above each top-level section */
.md-nav__list > .md-nav__item--nested {
  border-top: 1px solid #e5e7eb;
  margin-top: 0.5rem;
  padding-top: 0.5rem;
}

/* Hide the default MkDocs Material footer */
.md-footer {
  display: none !important;
}

****************8888

site_name: MA Analytics Runbook
site_description: Runbook for AtScale & related tools

theme:
  name: material
  language: en
  features:
    # removed: navigation.sections  (so top-level groups collapse)    
    - navigation.indexes          # click "AtScale" to open atscale/index.md
    - navigation.instant
    - toc.integrate
    - content.code.copy
  palette:
    - scheme: default
      primary: blue       
      accent: blue-grey
  font:
    text: system-ui
    code: ui-monospace
  icon:
    logo: material/book-outline

extra_css:
  - css/brand.css

nav:
  # (no "Overview" here — homepage is still docs/index.md)
  - AtScale:
      # NOTE: do NOT list atscale/index.md here — navigation.indexes will
      # automatically use it when you click "AtScale"
      - Architecture: atscale/architecture.md
      - Onboarding:
          - Business Users: atscale/onboarding/business-users.md
          - Developers: atscale/onboarding/developer.md
      - BI Connectivity:
          - Power BI: atscale/bi-connectivity/powerbi.md
          - Tableau: atscale/bi-connectivity/tableau.md
          - Excel: atscale/bi-connectivity/excel.md
      - Superset:
          - Overview: atscale/superset/index.md
          - Architecture: atscale/superset/architecture.md
          - Onboarding: atscale/superset/onboarding.md
      - FAQs: atscale/faqs.md
      - Release Notes: atscale/release-notes.md
      - Support: atscale/support.md

