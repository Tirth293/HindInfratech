/* ============================================================
   HIND INFRATECH — Custom Admin JS
   ============================================================ */

(function () {
  'use strict';

  // ── SIDEBAR ACTIVE STATE ──────────────────────────────────
  function setActiveSidebarItem() {
    var path = window.location.pathname;
    document.querySelectorAll('.sidebar-nav-item').forEach(function (el) {
      var href = el.getAttribute('href');
      if (!href) return; // skip logout button

      var isActive = false;
      if (href === '/admin/' && path === '/admin/') {
        isActive = true;
      } else if (href !== '/admin/' && path.startsWith(href)) {
        isActive = true;
      }
      if (isActive) {
        el.classList.add('active');
      }
    });
  }

  // ── MOBILE SIDEBAR TOGGLE ─────────────────────────────────
  function initMobileSidebar() {
    var btn     = document.getElementById('sidebar-toggle-btn');
    var sidebar = document.getElementById('admin-sidebar');
    var overlay = document.getElementById('sidebar-overlay');
    if (!btn || !sidebar) return;

    btn.addEventListener('click', function () {
      sidebar.classList.toggle('open');
      if (overlay) overlay.classList.toggle('show');
    });
    if (overlay) {
      overlay.addEventListener('click', function () {
        sidebar.classList.remove('open');
        overlay.classList.remove('show');
      });
    }
  }

  // ── STATUS BADGES IN LIST VIEW ────────────────────────────
  function colorizeStatusCells() {
    document.querySelectorAll('#result_list td').forEach(function (td) {
      var text = td.textContent.trim().toLowerCase();
      if (text === 'completed') {
        td.innerHTML = '<span class="badge badge-completed">✓ Completed</span>';
      } else if (text === 'ongoing') {
        td.innerHTML = '<span class="badge badge-ongoing">● Ongoing</span>';
      }
    });
  }

  // ── IMAGE THUMBNAILS IN LIST VIEW ─────────────────────────
  function enhanceImageCells() {
    document.querySelectorAll('#result_list td').forEach(function (td) {
      var img = td.querySelector('img');
      if (img && !img.style.width) {
        img.style.cssText = 'width:80px;height:56px;object-fit:cover;border-radius:6px;border:1.5px solid #E5E7EB;display:block;';
      }
    });
  }

  // ── FADE-IN ANIMATION FOR PANELS ─────────────────────────
  function animateCards() {
    document.querySelectorAll('.card-panel, .change-form fieldset').forEach(function (el, i) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(10px)';
      setTimeout(function () {
        el.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
      }, i * 55 + 60);
    });
  }

  // ── CONFIRM DELETE ────────────────────────────────────────
  function setupDeleteConfirm() {
    document.querySelectorAll('a.deletelink').forEach(function (a) {
      a.addEventListener('click', function (e) {
        if (!window.confirm('Are you sure you want to delete this item? This cannot be undone.')) {
          e.preventDefault();
        }
      });
    });
  }

  // ── IMAGE PREVIEW ON UPLOAD (change form) ────────────────
  function initImagePreview() {
    var fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(function (input) {
      input.addEventListener('change', function () {
        var file = input.files[0];
        if (!file || !file.type.startsWith('image/')) return;

        var reader = new FileReader();
        reader.onload = function (e) {
          // Find nearest existing preview img or create one
          var previewContainer = input.closest('.form-row, fieldset');
          if (!previewContainer) return;

          var existingPreview = previewContainer.querySelector('.upload-preview-img');
          if (!existingPreview) {
            existingPreview = document.createElement('img');
            existingPreview.className = 'upload-preview-img';
            existingPreview.style.cssText =
              'max-width:280px;max-height:180px;border-radius:8px;border:2px solid #E5E7EB;' +
              'margin-top:10px;display:block;object-fit:cover;';
            input.parentNode.insertBefore(existingPreview, input.nextSibling);
          }
          existingPreview.src = e.target.result;
        };
        reader.readAsDataURL(file);
      });
    });
  }

  // ── INIT ─────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', function () {
    setActiveSidebarItem();
    initMobileSidebar();
    colorizeStatusCells();
    enhanceImageCells();
    animateCards();
    setupDeleteConfirm();
    initImagePreview();
  });

})();
