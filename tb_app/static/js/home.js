window.addEventListener('scroll', () => {
    let content = document.querySelector('.ft-box');
    let contentPosition = content.getBoundingClientRect().top;
    let screenPosition = window.innerHeight;
    if (contentPosition < screenPosition) {
        let benefits = document.getElementsByClassName("ft-box")
        for (let i = 0; i < benefits.length; i++) {
            benefits[i].style.opacity = 1
            benefits[i].style.marginTop = "0px"
        }
    }
})