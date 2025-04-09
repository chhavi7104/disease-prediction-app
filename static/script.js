document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    
    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '300px';  // Optional styling
            img.style.marginTop = '10px';
            
            const preview = document.getElementById('imagePreview');
            preview.innerHTML = '';
            preview.appendChild(img);
        }
        
        reader.readAsDataURL(file);
    }
});