//  import * as THREE from 'https://cdn.skypack.dev/three@v0.149.0/build/three.module.js';
 import * as THREE from "{%static 'three/'%}";

    let camera, scene, renderer, vrButton;

    init();
    animate();

    function init() {
      scene = new THREE.Scene();

      camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
      );
      camera.position.z = 5;

      const geometry = new THREE.BoxGeometry();
      const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
      const cube = new THREE.Mesh(geometry, material);
      scene.add(cube);

      renderer = new THREE.WebGLRenderer();
      renderer.setSize(window.innerWidth, window.innerHeight);
      document.body.appendChild(renderer.domElement);

      // Add VR button
      vrButton = new THREE.XRButton(renderer);
      document.body.appendChild(vrButton);

      // Handle resize events
      window.addEventListener('resize', onWindowResize, false);
    }

    function animate() {
      renderer.setAnimationLoop(render);
    }

    function render() {
      // Update your scene here

      renderer.render(scene, camera);
    }

    function onWindowResize() {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();

      renderer.setSize(window.innerWidth, window.innerHeight);
    }