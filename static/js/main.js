/* ============================================================
   ZedAds – main.js
   ============================================================ */

// Mobile nav toggle
function toggleMenu() {
  const nav = document.querySelector('.nav-links');
  const btnNav = document.querySelector('.btn-nav');
  if (nav) {
    nav.style.display = nav.style.display === 'flex' ? 'none' : 'flex';
    nav.style.flexDirection = 'column';
    nav.style.position = 'absolute';
    nav.style.top = '68px';
    nav.style.left = '0';
    nav.style.right = '0';
    nav.style.background = 'rgba(13,13,13,0.98)';
    nav.style.padding = '1rem 2rem';
    nav.style.borderBottom = '1px solid #2e2e2e';
    nav.style.zIndex = '200';
  }
}

// Dashboard: filter cards by text search
function filterCards(query) {
  const cards = document.querySelectorAll('.listing-card');
  const q = query.toLowerCase().trim();
  cards.forEach(card => {
    const title = card.dataset.title || '';
    card.style.display = (q === '' || title.includes(q)) ? '' : 'none';
  });
}

// Dashboard: filter by tag
function filterTag(el, tag) {
  // Update active state
  document.querySelectorAll('.ftag').forEach(t => t.classList.remove('active'));
  el.classList.add('active');

  const cards = document.querySelectorAll('.listing-card');
  cards.forEach(card => {
    if (tag === '' || card.dataset.tag === tag) {
      card.style.display = '';
    } else {
      card.style.display = 'none';
    }
  });
}

// Remove duplicate filter tags
document.addEventListener('DOMContentLoaded', () => {
  const filterContainer = document.querySelector('.filter-tags');
  if (filterContainer) {
    const seen = new Set();
    filterContainer.querySelectorAll('.ftag').forEach(tag => {
      const text = tag.textContent.trim();
      if (text === 'All') { seen.add(text); return; }
      if (seen.has(text)) {
        tag.remove();
      } else {
        seen.add(text);
      }
    });
  }

  // Scroll animation for cards
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.cat-card, .listing-card, .feat-card, .value-card, .team-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    observer.observe(el);
  });
});
