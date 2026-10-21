# Website optimization campaign

## Routes

- Landing: `/website-optimization/`
- Service details: `/website-optimization/services/`
- Consultation: `/contact/?source=website-optimization#consultation`

No links were added to shared navigation, footer menus, or the homepage. Existing navigation on the new pages is retained. The pages remain indexable; absence from navigation does not mean private or noindex. No prices appear on the campaign pages.

## Offer

Website optimization and enhanced SEO service pages. The initial consultation defines each client's scope. Six-month engagement; ongoing service is optional. No ranking or lead guarantees.

## Measurement implemented

The campaign pages and contact page load `assets/website-optimization-funnel.js`. Existing GTM container: GTM-TZVZGCSP. Funnel attribution uses session storage and a fixed URL source value; no form values or personal information are sent as event properties. Normal noncampaign contact visits do not create campaign events.

Data layer events: `optimization_landing_view`, `optimization_service_view`, `optimization_contact_view`, `optimization_service_click`, `optimization_consultation_click`, `optimization_contact_click` (contact_method: call/email/text).

These are data layer hooks. GA4 reporting requires matching GTM event tags; it is not automatically configured by this code. Clarity custom events are forwarded only when Clarity is already loaded. No placeholder project ID or duplicate Clarity loader is installed.

## Remaining integration

1. Obtain the actual Clarity project ID and inspect the GTM workspace before installing its tag once across the funnel routes. Configure the desired masking and consent behavior in the real project.
2. Choose or supply a real form endpoint/delivery integration. Current contact page uses call/text/email and has no form backend. Do not use a mailto action or submit-button click as a successful form submission.
3. Add a short consultation form: name, email, website, optional phone, and brief goal. Validate fields, display delivery errors, prevent duplicate sends, and confirm server acceptance before the success state.
4. After confirmed delivery only, dispatch `new CustomEvent('raptor:consultation-success')`. The listener emits `optimization_form_success` once per page. Never send field values to Clarity or analytics.
5. In GTM, map the events to GA4 and mark only confirmed form success as the form lead conversion. Track contact clicks separately. Build the Clarity funnel using the three page routes and confirmed success event.
6. Test successful and failed deliveries, keyboard/mobile use, event order, and masking with the actual configured services before treating the funnel as fully operational.
