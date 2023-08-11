<script>
    const input = document.createElement('input');
    input.type = 'file';
    input.style.display = 'none';
    document.body.appendChild(input);

    const myDiv = document.getElementById("myDiv");
    myDiv.addEventListener('click', function() {
        input.click();
    });

    input.onchange = function(e) { 
        let file = e.target.files[0]; 
        let reader = new FileReader();
        reader.readAsDataURL(file); 

        reader.onload = function(readerEvent) {
            let content = readerEvent.target.result; 
            let myImg = document.getElementById("myImg");
            myImg.setAttribute('src', content);
        }
    };
</script>

<div id="myDiv">Click me to select an image</div>
<img id="myImg" src="" alt="Selected will be displayed here"/>
<h1> esta es la pag de admin de photos</h1>