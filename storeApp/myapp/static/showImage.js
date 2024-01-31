document.getElementById('input').addEventListener('change', handleFileSelect);

function handleFileSelect(event) {
    const fileInput = event.target;

    if (fileInput.files.length > 0) {
        const selectedFile = fileInput.files[0];
        console.log(selectedFile);
        let reader = new FileReader();
        reader.onload = function (e) { 
            let img = document.createElement('img');
            img.src = e.target.result;
            img.width = 320;
            img.height = 320;
            img.onload = () => {
                const showImage = document.getElementById('showImage');
                showImage.innerHTML = '';
                showImage.appendChild(img);
                // predictImg(img);
            }
            console.log(img);
        };
        reader.readAsDataURL(selectedFile);
        // console.log(selectedFile);
       
    }
    
} 