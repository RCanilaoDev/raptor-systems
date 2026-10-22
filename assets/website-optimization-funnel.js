/* Campaign events never contain form values or personal information. */
(() => {
  const prefix = '/website-optimization/';
  const path = location.pathname;
  const isContact = path === '/contact/' || path === '/contact/index.html';
  const fromOffer = new URLSearchParams(location.search).get('source') === 'website-optimization';
  let active = path.startsWith(prefix) || (isContact && fromOffer);
  try {
    if (path.startsWith(prefix)) sessionStorage.setItem('raptor_optimization_funnel', '1');
    if (isContact && sessionStorage.getItem('raptor_optimization_funnel') === '1') active = true;
  } catch (_) { /* URL attribution still works when storage is unavailable. */ }
  // Record all contact visits, but only attribute campaign events to campaign visitors.
  if (path.startsWith(prefix) || isContact) {
    if (!window.clarity) {
      window.clarity = function () { (window.clarity.q = window.clarity.q || []).push(arguments); };
    }
    if (!document.querySelector('script[src*="clarity.ms/tag/"]')) {
      const script = document.createElement('script');
      script.async = true;
      script.src = 'https://www.clarity.ms/tag/yx5u4ujbkh';
      document.head.appendChild(script);
    }
  }
  if (!active) return;
  const stage = isContact ? 'contact' : path === prefix || path === prefix + 'index.html' ? 'landing' : 'service';
  function track(event, extra = {}) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event, funnel_name: 'website_optimization', funnel_stage: stage, ...extra });
    if (typeof window.clarity === 'function') window.clarity('event', event);
  }
  track('optimization_' + stage + '_view');
  document.addEventListener('click', event => {
    const link = event.target.closest('a');
    if (!link) return;
    const action = link.dataset.contactAction;
    if (['call', 'email', 'text'].includes(action)) {
      track('optimization_contact_click', { contact_method: action });
      return;
    }
    const destination = new URL(link.href, location.href);
    if (destination.origin !== location.origin) return;
    if (destination.pathname === '/contact/') track('optimization_consultation_click');
    else if (destination.pathname === prefix + 'services/') track('optimization_service_click');
  });
  document.addEventListener('raptor:consultation-start', () => track('optimization_form_start'), { once: true });
  // The form adapter emits success only after Web3Forms confirms acceptance.
  // A button click, validation pass, or browser submit event is not a confirmed lead.
  document.addEventListener('raptor:consultation-success', () => track('optimization_form_success'), { once: true });
})();
