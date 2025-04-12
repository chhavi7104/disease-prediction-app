
function previewImage(event) {
    const file = event.target.files[0];
    
    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '300px';
            img.style.maxHeight = '300px';
            document.getElementById('imagePreview').innerHTML = '';
            document.getElementById('imagePreview').appendChild(img);
        }
        reader.readAsDataURL(file);
    }
}

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    fetch('/scan', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if(data.path) {
            const img = document.createElement('img');
            img.src = '/' + data.path.replace(/\\/g, '/');  // for windows paths
            img.style.maxWidth = '300px';
            img.style.maxHeight = '300px';

            document.getElementById('uploadedImageContainer').innerHTML = `
                <h3>Uploaded Image</h3>
            `;
           
        } else {
            alert(data.error || 'Upload failed');
        }
    })
    .catch(err => {
        console.error(err);
        alert('Something went wrong!');
    });
});
