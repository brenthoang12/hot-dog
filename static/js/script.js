// variable for user image input
const dropArea = document.getElementById('drop-area');
const inputFile = document.getElementById('input-file');
const imageView = document.getElementById('img-view');

// variable for model operation
const run = document.getElementById('run');
const clear = document.getElementById('clear');
const modelReturn = document.getElementById('modelReturn');





// user image input
inputFile.addEventListener("change", uploadImage);

function uploadImage() {
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    imageView.style.backgroundImage = `url(${imgLink})`;
    imageView.textContent = "";
}

dropArea.addEventListener("dragover", function(e){
    e.preventDefault();
});

dropArea.addEventListener("drop", function(e){
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
    uploadImage();
});


// model operation

run.addEventListener('click', function() {
    // if (yesModel.style.display === 'none') {
    modelReturn.style.display = 'block';
    // } else {
    //     yesModel.style.display = 'none';
    // }
});

clear.addEventListener('click', function() {
    modelReturn.style.display = 'none';
});