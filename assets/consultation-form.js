(() => {
  const form = document.getElementById('consultation-form');
  if (!form) return;
  const result = document.getElementById('consultation-result');
  const button = form.querySelector('button[type="submit"]');
  let pending = false;
  let complete = false;
  form.addEventListener('input', () => {
    document.dispatchEvent(new CustomEvent('raptor:consultation-start'));
  }, { once: true });
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (pending || complete || !form.reportValidity()) return;
    if (form.elements.botcheck.checked) return;
    pending = true;
    button.disabled = true;
    button.textContent = 'Sending…';
    form.setAttribute('aria-busy', 'true');
    result.textContent = 'Sending your request…';
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 20000);
    try {
      const payload = Object.fromEntries(new FormData(form));
      const response = await fetch(form.action, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(payload),
        signal: controller.signal
      });
      const data = await response.json();
      if (!response.ok || data.success !== true) throw new Error('Submission not confirmed');
      complete = true;
      form.reset();
      result.textContent = 'Thank you. Your consultation request has been received. Raptor will follow up using the contact details you provided.';
      button.textContent = 'Request received';
      document.dispatchEvent(new CustomEvent('raptor:consultation-success'));
    } catch (error) {
      result.textContent = error.name === 'AbortError'
        ? 'We couldn’t confirm delivery in time. Your details are still here. Please check your connection and try again, or call or email Raptor.'
        : 'We couldn’t confirm your request was received. Your details are still here. Please try again, or call or email Raptor.';
      button.textContent = 'Try Again';
    } finally {
      clearTimeout(timeout);
      pending = false;
      button.disabled = complete;
      form.removeAttribute('aria-busy');
      result.focus();
    }
  });
})();
