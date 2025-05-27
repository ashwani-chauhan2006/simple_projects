document.addEventListener('DOMContentLoaded', () => {
    const scene = document.querySelector('.scene');
    const morning = document.querySelector('.morning');
    const evening = document.querySelector('.evening');
    const night = document.querySelector('.night');
    const sun = document.querySelector('.sun');
    const moon = document.querySelector('.moon');
    const stars = document.querySelector('.stars');
    const ocean = document.querySelector('.ocean');
    const beach = document.querySelector('.beach');
    const palmTree = document.querySelector('.palm-tree');

    // Create stars
    for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.opacity = Math.random();
        stars.appendChild(star);
    }

    window.addEventListener('scroll', () => {
        const scrollPercent = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight);
        
        // Morning to Evening transition (0-0.5 scroll)
        if (scrollPercent <= 0.5) {
            const morningToEvening = scrollPercent * 2;
            morning.style.opacity = 1 - morningToEvening;
            evening.style.opacity = morningToEvening;
            
            // Move sun
            sun.style.top = `${20 + morningToEvening * 30}%`;
            sun.style.left = `${20 + morningToEvening * 60}%`;
            sun.style.transform = `scale(${1 - morningToEvening * 0.5})`;
            sun.style.opacity = 1;

            // Keep beach visible during day
            ocean.style.opacity = 1;
            beach.style.opacity = 1;
            palmTree.style.opacity = 1;
        }
        
        // Evening to Night transition (0.5-1 scroll)
        if (scrollPercent >= 0.5) {
            const eveningToNight = (scrollPercent - 0.5) * 2;
            evening.style.opacity = 1 - eveningToNight;
            night.style.opacity = eveningToNight;
            
            // Show moon and stars
            moon.style.opacity = eveningToNight;
            stars.style.opacity = eveningToNight;
            
            // Move moon
            moon.style.top = `${20 + eveningToNight * 30}%`;
            moon.style.right = `${20 + eveningToNight * 60}%`;
            
            // Make sun invisible during night
            sun.style.opacity = 0;

            // Fade out beach elements during night
            ocean.style.opacity = 1 - eveningToNight;
            beach.style.opacity = 1 - eveningToNight;
            palmTree.style.opacity = 1 - eveningToNight;
        }
    });
}); 