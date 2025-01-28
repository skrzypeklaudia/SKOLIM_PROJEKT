document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');

    menuToggle.addEventListener('click', () => {
        sidebar.classList.toggle('hidden');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const registerButton = document.getElementById('registerButton');
    const registrationModal = document.getElementById('registrationModal');

    // Tworzenie tła modalnego
    const modalOverlay = document.createElement('div');
    modalOverlay.id = 'modalOverlay';
    document.body.appendChild(modalOverlay);

    // Otwieranie modalnego okna
    registerButton.addEventListener('click', function() {
        modalOverlay.style.display = 'block';
        registrationModal.style.display = 'block';
    });

    // Zamknięcie modalnego okna
    modalOverlay.addEventListener('click', function() {
        modalOverlay.style.display = 'none';
        registrationModal.style.display = 'none';
    });
});
function toggleDetails(index) {
    const details = document.getElementById(`details-${index}`);
    if (details.classList.contains('visible')) {
        details.classList.remove('visible');
    } else {
        details.classList.add('visible');
    }
}
