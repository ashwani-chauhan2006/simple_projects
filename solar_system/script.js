document.addEventListener('DOMContentLoaded', () => {
    const planets = document.querySelectorAll('.planet');
    const orbitRadii = [120, 160, 200, 240, 300, 360, 420, 480];
    const orbitSpeeds = [4, 6, 8, 10, 15, 20, 25, 30];
    const solarSystem = document.querySelector('.solar-system');

    // Add mouse move tilt effect
    document.addEventListener('mousemove', (e) => {
        const y = e.clientY / window.innerHeight;
        const rotateX = 60 - (y * 30);
        solarSystem.style.transform = `rotateX(${rotateX}deg) rotateZ(30deg)`;
    });

    planets.forEach((planet, index) => {
        const radius = orbitRadii[index];
        const speed = orbitSpeeds[index];
        
        // Set initial position
        planet.style.transform = `translate(-50%, -50%) translateX(${radius}px)`;
        
        // Create orbit path
        const orbitPath = document.createElement('div');
        orbitPath.className = 'orbit-path';
        orbitPath.style.width = `${radius * 2}px`;
        orbitPath.style.height = `${radius * 2}px`;
        
        // Insert orbit path before the planet
        planet.parentNode.insertBefore(orbitPath, planet);
        
        // Update animation with proper orbit radius
        planet.style.animation = `orbit ${speed}s linear infinite`;
        planet.style.setProperty('--orbit-radius', `${radius}px`);
    });
}); 