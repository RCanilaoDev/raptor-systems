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

Clarity is installed directly by the shared campaign script using the supplied project ID. It loads on both campaign routes and Contact; the code checks for an existing tag to avoid inserting a second one. Do not add another Clarity tag in GTM. Campaign events are attributed only to visitors who entered the funnel. GA4 still requires matching GTM event tags.

## Consultation form

Web3Forms receives the supplied public access key in the browser form, as required by its integration. Name, email, website and message are required; phone is optional. The form includes a honeypot, explicit labels, masking, native validation, timeout/error feedback, and a pending/completed submission lock. Failed requests preserve entries. Only an HTTP-success response with `success: true` fires `optimization_form_success`; submit clicks and validation passes do not.

`optimization_form_start` is emitted on the first form input for campaign visitors. The success state remains on the Contact page. Without JavaScript, the form posts to Web3Forms and uses its confirmation page; custom success tracking requires JavaScript.

## Verification and dashboard work

JavaScript syntax and mocked response handling checked for success, rejection, and duplicate submission behavior. A real delivery has not been sent. Browser visual QA and live recording verification remain. Verify receipt with a clearly labeled test after deployment. Configure the funnel in the Clarity dashboard as landing route, service route, Contact route, and `optimization_form_success`. Configure GA4/GTM event mappings separately if desired. Existing GTM container: GTM-TZVZGCSP.
