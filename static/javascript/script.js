let currentIndex = 0;

function showImage(index) {
    const images = document.querySelectorAll('.carousel-images img');
    if (index >= images.length) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = images.length - 1;
    } else {
        currentIndex = index;
    }
    const offset = -currentIndex * 100;
    document.querySelector('.carousel-images').style.transform = `translateX(${offset}%)`;
}

function changeImage(direction) {
    showImage(currentIndex + direction);
}

// Auto slide every 3 seconds
setInterval(() => {
    changeImage(1);
}, 3000);

document.addEventListener('DOMContentLoaded', () => {
    showImage(currentIndex);
});