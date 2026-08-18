# Raptor Entity Graph Registry

Version: 16.08  
Canonical pages: 39  
Defined entity nodes: 103  
Relationship edges: 370

## Persistent Entities

- Organization: `https://raptorconsultinggroup.com/#organization`
- WebSite: `https://raptorconsultinggroup.com/#website`
- Person: `https://raptorconsultinggroup.com/about/ricardo-canilao/#person`
- Logo: `https://raptorconsultinggroup.com/#logo`

## Entity Counts

- AboutPage: 1
- Article: 5
- BreadcrumbList: 35
- CollectionPage: 8
- ContactPage: 1
- ImageObject: 1
- ItemList: 2
- Organization: 1
- Person: 1
- ProfilePage: 1
- Service: 18
- WebPage: 28
- WebSite: 1

## Governance

- One canonical ID represents each entity across the site.
- Organization and WebSite definitions are identical wherever embedded.
- The full Person definition lives on Ricardo Canilao’s ProfilePage; other pages reference its ID.
- Service entities use their canonical service URL plus `#service`.
- Case studies use their canonical URL plus `#article`.
- Page and breadcrumb IDs use `#webpage` and `#breadcrumb`.
- Structured data must describe visible content and must not invent an entity, result, rating, review, or offer.
- Graph validation is required after any URL, navigation, content-role, or schema change.
