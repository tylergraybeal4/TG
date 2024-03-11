// Initialize scene, camera, and renderer
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight); // Set renderer size to match window size
document.body.appendChild(renderer.domElement);

// Create a material for the main color (blue with 75% opacity)
var materialMain = new THREE.MeshPhongMaterial({ color: 0x0000ff }); // Using MeshPhongMaterial for better lighting

// Create a cube
var geometry = new THREE.BoxGeometry();
var cube = new THREE.Mesh(geometry, materialMain);
scene.add(cube);

// Add ambient light to the scene
var ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // Color white, intensity 0.5
scene.add(ambientLight);

// Adjust camera aspect ratio to match renderer size
window.addEventListener('resize', function () {
    var width = window.innerWidth;
    var height = window.innerHeight;
    renderer.setSize(width, height);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
});

camera.position.z = 5;

// Animation loop
function animate() {
    requestAnimationFrame(animate);

    // Rotate the cube
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    renderer.render(scene, camera);
}
animate();
