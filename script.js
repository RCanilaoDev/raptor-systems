(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  const servicesDisclosure = document.querySelector('.nav-services');
  const navShell = document.querySelector('.nav-shell');
  if (!toggle || !nav) return;

  /* BUILD 16.26 // ACTIVE PRIMARY NAVIGATION */
  const normalizePath = (value) => {
    const path = new URL(value, window.location.origin).pathname.replace(/\/+$/, '');
    return path || '/';
  };

  const currentPath = normalizePath(window.location.pathname);
  const topLevelLinks = Array.from(nav.children).filter(
    (item) => item.matches('a:not(.nav-cta)')
  );

  let activeItem = null;
  if (currentPath.startsWith('/services')) {
    activeItem = servicesDisclosure ? servicesDisclosure.querySelector('summary') : null;
  } else if (
    currentPath.startsWith('/work/systems') ||
    currentPath.startsWith('/work/hqcp') ||
    currentPath.startsWith('/work/web-production-system')
  ) {
    activeItem = topLevelLinks.find((link) => normalizePath(link.href) === '/work/systems');
  } else if (currentPath.startsWith('/work')) {
    activeItem = topLevelLinks.find((link) => normalizePath(link.href) === '/work');
  } else {
    activeItem = topLevelLinks.find((link) => {
      const linkPath = normalizePath(link.href);
      return linkPath !== '/' && currentPath.startsWith(linkPath);
    });
  }

  if (activeItem) {
    activeItem.classList.add('is-active');
    activeItem.setAttribute('aria-current',
      activeItem.matches('a') && normalizePath(activeItem.href) === currentPath ? 'page' : 'location'
    );
  }

  nav.querySelectorAll('.services-menu a').forEach((link) => {
    if (normalizePath(link.href) !== currentPath) return;
    link.classList.add('is-active');
    link.setAttribute('aria-current', 'page');
  });

  const positionMobileNav = () => {
    if (window.innerWidth > 1220 || !navShell) {
      nav.style.removeProperty('--mobile-nav-top');
      return;
    }
    const shellBottom = navShell.getBoundingClientRect().bottom;
    nav.style.setProperty('--mobile-nav-top', `${Math.max(8, shellBottom + 8)}px`);
  };

  const setOpen = (open) => {
    if (open) positionMobileNav();
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
    nav.classList.toggle('is-open', open);\n    if (navShell) navShell.classList.toggle('mobile-nav-active', open && window.innerWidth <= 1220);
    document.body.classList.toggle('mobile-nav-open', open && window.innerWidth <= 1220);
    if (!open) nav.style.removeProperty('--mobile-nav-top');
    if (!open && servicesDisclosure) servicesDisclosure.open = false;
  };

  let lastToggleAt = -Infinity;

  toggle.addEventListener('click', (event) => {
    event.stopPropagation();

    const now = performance.now();
    if (now - lastToggleAt < 350) {
      event.preventDefault();
      return;
    }

    lastToggleAt = now;
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });

  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });

  document.addEventListener('click', (event) => {
    if (
      toggle.getAttribute('aria-expanded') === 'true' &&
      !nav.contains(event.target) &&
      !toggle.contains(event.target) &&
      !event.target.closest('.site-header')
    ) {
      setOpen(false);
    }
    if (servicesDisclosure && servicesDisclosure.open && !servicesDisclosure.contains(event.target)) {
      servicesDisclosure.open = false;
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      if (servicesDisclosure) servicesDisclosure.open = false;
      setOpen(false);
      toggle.focus();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 1220) setOpen(false);
  }, { passive: true });
})();


(() => {
  const brandStage = document.querySelector('.footer-brand-stage');
  if (!brandStage) return;

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  brandStage.classList.add('footer-logo-reveal');

  if (reducedMotion || !('IntersectionObserver' in window)) {
    brandStage.classList.add('is-visible');
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, {
    threshold: 0.18,
    rootMargin: '0px 0px -8% 0px'
  });

  observer.observe(brandStage);
})();


/* BUILD 15.33 // footer split logo reveal */
(function () {
  const revealNodes = document.querySelectorAll("[data-footer-logo-reveal]");
  if (!revealNodes.length) return;

  const reveal = (node) => node.classList.add("is-visible");

  if (!("IntersectionObserver" in window)) {
    revealNodes.forEach(reveal);
    return;
  }

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      reveal(entry.target);
      obs.unobserve(entry.target);
    });
  }, {
    threshold: 0.25,
    rootMargin: "0px 0px -5% 0px"
  });

  revealNodes.forEach((node) => observer.observe(node));
})();


/* BUILD 15.37 // compact sticky header */
(() => {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const COMPACT_AT = 96;
  let ticking = false;

  const updateHeader = () => {
    header.classList.toggle('is-compact', window.scrollY >= COMPACT_AT);
    ticking = false;
  };

  const requestUpdate = () => {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(updateHeader);
  };

  updateHeader();
  window.addEventListener('scroll', requestUpdate, { passive: true });
})();


/* BUILD 15.48 // footer/header logo handoff */
(() => {
  const header = document.querySelector('.site-header');
  const footerBrand = document.querySelector('.footer-brand-stage');
  if (!header || !footerBrand || !('IntersectionObserver' in window)) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      header.classList.toggle('footer-brand-in-view', entry.isIntersecting);
    });
  }, {
    threshold: 0.20,
    rootMargin: '0px 0px -6% 0px'
  });

  observer.observe(footerBrand);
})();


/* =========================================================
   BUILD 15.62 // CONTACT PRIVACY
   Direct call/text links are generated at runtime so the phone
   number is not exposed as visible text or a tel:/sms: URI in HTML.
   ========================================================= */
(() => {
  const encodedContact = 'KzE3MDI1MjExMTMx';

  const decodeContact = () => {
    try {
      return window.atob(encodedContact);
    } catch (error) {
      return '';
    }
  };

  document.querySelectorAll('[data-contact-action]').forEach((link) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      const number = decodeContact();
      if (!number) return;
      if (link.dataset.contactAction === 'call') {
        window.location.href = `tel:${number}`;
      } else if (link.dataset.contactAction === 'text') {
        window.location.href = `sms:${number}`;
      }
    });
  });
})();
