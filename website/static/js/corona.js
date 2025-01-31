const openMenu = document.getElementById('open-menu');
const navLinks = document.getElementById('nav-links');

openMenu.addEventListener('click', () => {
    navLinks.classList.toggle('nav-open');
});