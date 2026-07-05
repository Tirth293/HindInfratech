/* ============================================================
   HIND INFRATECH — Main JavaScript
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ── 1. SMOOTH SCROLL ── */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        var navbar = document.querySelector('.navbar');
        var navCollapse = document.getElementById('navMenu');
        var navbarHeight = navbar ? navbar.offsetHeight : 0;
        var scrollTarget = target.id === 'home' ? target : (target.querySelector('.section-label') || target);
        var targetTop = scrollTarget.getBoundingClientRect().top + window.pageYOffset - navbarHeight - 12;
        window.scrollTo({ top: Math.max(targetTop, 0), behavior: 'smooth' });
        /* close mobile navbar if open */
        if (navCollapse && navCollapse.classList.contains('show')) {
          var toggler = document.querySelector('.navbar-toggler');
          if (toggler) toggler.click();
        }
      }
    });
  });

  /* ── 2. NAVBAR ACTIVE STATE ON SCROLL ── */
  var sections  = document.querySelectorAll('section[id]');
  var navLinks  = document.querySelectorAll('.navbar-nav .nav-link');

  function updateActiveNav() {
    var scrollY = window.scrollY;
    var navbar = document.querySelector('.navbar');
    var offset = (navbar ? navbar.offsetHeight : 0) + 24;
    var current = '';
    sections.forEach(function (sec) {
      if (scrollY >= sec.offsetTop - offset) current = sec.id;
    });
    navLinks.forEach(function (link) {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) link.classList.add('active');
    });
  }

  window.addEventListener('scroll', updateActiveNav);
  updateActiveNav();

  /* ── 3. PROJECT FILTER TABS ──
     Handled in templates/index.html (combined with the Show More /
     Show Less control), so it isn't duplicated here. */

  /* ── 4. SCROLL FADE-UP ANIMATION ── */
  var fadeEls = document.querySelectorAll('.fade-up');

  var fadeObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        fadeObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  fadeEls.forEach(function (el) { fadeObserver.observe(el); });

  /* ── 5. COUNTER ANIMATION (stats section) ── */
  var statsSection = document.querySelector('.stats-section');
  var counted      = false;

  function animateCounters() {
    document.querySelectorAll('.stat-card .num').forEach(function (el) {
      var raw    = el.getAttribute('data-target') || el.textContent;
      var numMatch = raw.match(/\d+/);
      if (!numMatch) return;
      var target  = parseInt(numMatch[0]);
      var suffix  = raw.replace(/\d+/, '');
      var current = 0;
      var step    = Math.ceil(target / 50);
      var timer   = setInterval(function () {
        current = Math.min(current + step, target);
        el.innerHTML = current + (suffix.trim() ? '<span>' + suffix + '</span>' : '');
        if (current >= target) clearInterval(timer);
      }, 30);
    });
  }

  if (statsSection) {
    var statsObserver = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting && !counted) {
        counted = true;
        animateCounters();
      }
    }, { threshold: 0.3 });
    statsObserver.observe(statsSection);
  }

  /* ── 6. CONTACT FORM SUBMISSION ── */
  var submitBtn = document.getElementById('submitBtn');
  if (submitBtn) {
    submitBtn.addEventListener('click', submitForm);
  }

  function submitForm() {
    var name    = document.getElementById('f-name').value.trim();
    var phone   = document.getElementById('f-phone').value.trim();
    var service = document.getElementById('f-service').value.trim();
    var message = document.getElementById('f-message').value.trim();

    if (!name || !phone || !message) {
      showError('Please fill in Name, Phone, and Message fields.');
      return;
    }

    var inquiryText = [
      'New inquiry from Hind Infratech website',
      '',
      'Name: ' + name,
      'Phone / WhatsApp: ' + phone,
      'Service Required: ' + (service || 'Not specified'),
      'Project Details: ' + message
    ].join('\n');
    var whatsappUrl = 'https://wa.me/919825373697?text=' + encodeURIComponent(inquiryText);

    /* show success toast */
    var toast = document.getElementById('toastMsg');
    if (toast) {
      toast.classList.add('show');
      setTimeout(function () { toast.classList.remove('show'); }, 4000);
    }

    window.location.href = whatsappUrl;

    /* reset form */
    ['f-name','f-phone','f-service','f-message'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.value = '';
    });
  }

  function showError(msg) {
    var toast = document.getElementById('errorToast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'errorToast';
      toast.style.cssText =
        'position:fixed;bottom:100px;right:28px;z-index:9999;' +
        'background:#dc2626;color:#fff;padding:14px 22px;border-radius:10px;' +
        'font-weight:600;font-size:14px;display:flex;align-items:center;gap:10px;' +
        'box-shadow:0 8px 24px rgba(220,38,38,0.4);' +
        'transform:translateY(80px);opacity:0;transition:all 0.35s;pointer-events:none;';
      document.body.appendChild(toast);
    }
    toast.innerHTML = '<i class="ph ph-x-circle" style="font-size:20px;"></i>' + msg;
    toast.style.transform = 'translateY(0)';
    toast.style.opacity   = '1';
    setTimeout(function () {
      toast.style.transform = 'translateY(80px)';
      toast.style.opacity   = '0';
    }, 3500);
  }

  /* ── 7. NAVBAR SHRINK ON SCROLL ── */
  var navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', function () {
    if (window.scrollY > 60) {
      navbar.style.boxShadow = '0 4px 20px rgba(27,79,160,0.15)';
    } else {
      navbar.style.boxShadow = '0 2px 12px rgba(27,79,160,0.08)';
    }
  });

  /* ── 8. YEAR IN FOOTER ── */
  var yearEl = document.getElementById('footerYear');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

});
