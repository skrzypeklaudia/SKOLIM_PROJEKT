document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');

    menuToggle.addEventListener('click', () => {
        sidebar.classList.toggle('hidden');
    });
});