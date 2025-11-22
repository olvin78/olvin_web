// Efecto: navbar cambia cuando haces scroll
document.addEventListener('scroll', () => {
    const nav = document.getElementById('mainNavbar');
    if (!nav) return;
    if (window.scrollY > 10) {
        nav.classList.add('nav-scrolled');
    } else {
        nav.classList.remove('nav-scrolled');
    }
});

// Efecto: scroll suave a secciones con data-scroll-target
document.querySelectorAll('[data-scroll-target]').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        const targetSelector = btn.getAttribute('data-scroll-target');
        const target = document.querySelector(targetSelector);
        if (!target) return;
        window.scrollTo({
            top: target.offsetTop - 70,
            behavior: 'smooth'
        });
    });
});



