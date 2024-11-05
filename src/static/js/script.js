function show_home(){
    console.log("Reached home..!")
}

//function upload_image(){
//    console.log("Upload image..!")
//}

function upload_folder(){
    console.log("Upload image..!")
}

function upload_image() {
    // Simulating an array of image names returned from the function
    const imageNames = ["image1.jpg", "image2.png", "image3.gif", "image4.jpg", "image5.png", "image6.gif", "image7.jpg", "image8.png", "image9.gif", "image10.jpg"];
    displayImageNames(imageNames);
}

// Function to display image names in the #img_fn_list div
//function displayImageNames(imageNames) {
//    const imgListDiv = document.getElementById('img_fn_list');
//    imgListDiv.innerHTML = ""; // Clear any existing content
//
//    // Append each image name as a new div
//    imageNames.forEach(name => {
//        const nameDiv = document.createElement('div');
//        nameDiv.className = "image-name";
//        nameDiv.textContent = name;
//        imgListDiv.appendChild(nameDiv);
//    });
//}

function displayImageNames(imageNames) {
    const imgListDiv = document.getElementById('img_fn_list');
    imgListDiv.innerHTML = ""; // Clear any existing content

    // Append each image name as a new div
    imageNames.forEach(name => {
        const nameDiv = document.createElement('div');
        nameDiv.className = "image-name";
        nameDiv.textContent = name;

        // Add click event listener to log the image name and add selected styling
        nameDiv.addEventListener('click', function() {
            // Clear previous selections
            document.querySelectorAll('.image-name').forEach(el => el.classList.remove('selected'));
            // Set selected style
            nameDiv.classList.add('selected');
            // Log the image name to the console
            console.log("Selected image:", name);
        });

        imgListDiv.appendChild(nameDiv);
    });
}
