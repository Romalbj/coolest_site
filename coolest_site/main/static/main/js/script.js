const sidebar = document.querySelector('.sidebar');
const toggleBtn = document.querySelector('.toggle-btn');
console.log('toggleBtn', toggleBtn);

toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('active');
});