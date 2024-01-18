const sidebar = document.querySelector('.sidebar');
const toggleBtn = document.querySelector('.toggle-btn');
console.log('toggleBtn', toggleBtn);

toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('active');
});


const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('a').
forEach(link => {
    if(link.href.includes(`${activePage}`))
        link.classList.add('active');

})
