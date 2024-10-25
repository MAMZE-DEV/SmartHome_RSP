


function nextButtonClick(){
    const element = document.getElementById("progress-move");
    if (element) {
        element.classList.add("progress-move-1");
    } else {
        console.error("Element with ID 'progress-move' not found");
    }
}