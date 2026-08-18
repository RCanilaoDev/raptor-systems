# Raptor Insights Article Specification

Status: Approved implementation framework  
Applies to: Future articles beneath Search, Commerce, and Web Operations

## Publication Gate

An article is published only when it is grounded in firsthand experience, a verified technical condition, a documented operating decision, or a defensible analysis. Generic articles created only to fill a publishing calendar do not qualify.

## Required Content

1. Problem or operating context
2. Why the condition matters
3. What was inspected or observed
4. Decision or method used
5. Evidence and its limits
6. Practical lesson
7. Related service, system, and evidence links
8. Author connection to Ricardo Canilao

## Search Ownership Rule

- Commercial service pages own broad transactional intent.
- Insights own narrower informational and problem-based intent.
- An article must not reuse a service page's primary title, H1, or core keyword target.
- Canonicals are self-referencing. Articles are not canonicalized to service pages merely because they link to them.

## URL Pattern

- `/insights/search/{article-slug}/`
- `/insights/commerce/{article-slug}/`
- `/insights/web-operations/{article-slug}/`

## Required Schema

- `Article` with persistent `#article` ID
- `WebPage` with persistent `#webpage` ID
- `BreadcrumbList`
- `author` → `https://raptorconsultinggroup.com/about/ricardo-canilao/#person`
- `publisher` → `https://raptorconsultinggroup.com/#organization`
- `isPartOf` → the appropriate Insights category
- `datePublished` and `dateModified` based on real publication history
- `headline`, `description`, `inLanguage`, and canonical URL

## Breadcrumb Pattern

Home > Insights > Category > Article

## Verification

Before publication, validate the visible claims, internal links, canonical, heading hierarchy, metadata, Article graph, author relationship, image treatment, mobile layout, and distinction from the related commercial page.
