<script>
    import { each, onMount } from "svelte/internal";
    import {
        Form,
        Button,
        FormGroup,
        FormText,
        Input,
        Label,
        Modal,
        ModalBody,
        ModalFooter,
        ModalHeader,
    } from "sveltestrap";
    import {push} from 'svelte-spa-router';
    import NewPhoto from "../components/new_photo.svelte";

    let formLabel = "";
    let containerPhoto
    let new_photo

    const saveGallery= () =>{
        let title = document.getElementById("field_title").value;
        let date = document.getElementById("field_date").value;
        
        let gallery = {
            title: title,
            date: date,
            flyer:"", 
        };

        fetch("http://localhost:5000/gallery", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(gallery),
        })
            .then((response) => response.json())
            .then((new_gallery) => {
                console.log("Success:", new_gallery);
                document.getElementById("myImg").style.cursor = "pointer";
                document.getElementById("title").innerText = gallery.title;
                uploadFlyer(new_gallery.id);
                document.getElementById("myButton").disabled = true;
                document.getElementById("myButton").style.cursor = "not-allowed";
            })


            .catch((error) => {
                console.error("Error:", error);
            }); 
    }


    const uploadFlyer = (gallery_id) => {
        let form = document.createElement("form");
        form.setAttribute("method", "post");
        form.setAttribute("enctype", "multipart/form-data");
        form.setAttribute("action",`http://127.0.0.1:5000/upload/flyer/${gallery_id}`);

        form.onsubmit = (e) =>{
            e.preventDefault()
        }
        let fileInput = document.getElementById("myFlyer");

        form.appendChild(fileInput);

        document.body.appendChild(form);
        let formData = new FormData(form);
        fetch(`http://127.0.0.1:5000/upload/flyer/${gallery_id}`, {
            method: "POST",
            body: formData,
        }).then(response => response.json()).then(data =>{
            console.log("success", data)
        })
        

    }

    const newPhoto= () =>{
        new_photo = new NewPhoto({
            target: containerPhoto, //document.getElementById("containerPhoto"),
            props: {},
        })
    }
  
    onMount (() => {

        let input = document.createElement('input');
        input.id = 'myFlyer'; 
        input.type = 'file';
        input.name = 'file';
        input.style.display = 'none';
        document.body.appendChild(input);

        
        input.onchange = function(e) { 
            let file = e.target.files[0]; 
            let reader = new FileReader();
            reader.readAsDataURL(file); 
            
            reader.onload = function(readerEvent) {
                let content = readerEvent.target.result; 
                let myImg = document.getElementById('myImg');
                myImg.setAttribute('src', content);
            }
        };

    })
    
    const selectFlyer= () => {
        let input= document.getElementById("myFlyer");
        input.click()
    }

    const onPhotoLoaded = () =>{
        let blankPhoto = NewPhoto
        containerPhoto.appendChild(blankPhoto)
    }


</script>

<div class="anti-pajaro">
    <h1 id="title" class="titel">New Gallery</h1>
    <div class="contenedor">
        <div class="flyer_card">
            <div id="myDiv" on:click={()=> selectFlyer()}><img id="myImg" width="150px" src="" alt="Elige un FLYER"/></div>
            <div>
                <Form>
                    <input value="" id="field_id" type="hidden" name="id" />
            
                    <FormGroup style={formLabel}>
                    <Label for="field_title">Titulo</Label>
                    <Input type="text" value="" id="field_title" name="title" />
                    </FormGroup>
            
                    <FormGroup style={formLabel}>
                    <Label for="field_date">Fecha</Label>
                    <Input type="date" value="" id="field_date" name="date">
                    </Input>
                    </FormGroup>
                </Form>
            </div>
            <div >
                <button id="myButton" on:click={()=> saveGallery()}>Cargar</button>
            </div>
        </div>
        <div class="contenedor_img">
            <div bind:this={containerPhoto} id="containerPhoto" class="photo_card">
<!--quiero que el primer div sea el que haga el push de la foto y 
se muestren las fotos dentro de la galeria si esta ya existe-->
                <NewPhoto on:photoLoaded={()=> onPhotoLoaded}/>   
            </div>
            <!--este dive es opcional -->
                <div>
                    <button on:click={()=> newPhoto()}>Add Foto</button>
                </div>
            <!--    <button>Editar</button>
                <button>Eliminar</button>
            </div> -->
        </div>
    </div>
    
</div>

<style>
    
    .anti-pajaro {
        width: 1500px;
        border: solid 3px;
        margin-top: 40px;
        background-color: #ffffffed;
        border-radius: 42px;
        height: 800px;
        
    }

    .contenedor{
        display: flex ;
        position: relative ;
        background-color: rgba(255, 255, 255, 0);
        flex-direction: row ;
        border-radius: 42px;
        height: 88%;
    }
    
    .contenedor_img{
        width: 80%;
        height:705px;
        overflow-y: auto;
        margin-right: 20px;
    }


    .flyer_card{
        align-items: center ;
        display: flex ;
        flex-direction: column;
        padding: 16px;
        width: 30%;
        background-color: rgba(54, 52, 52, 0.163);
        justify-content: space-evenly;
        border-bottom-left-radius: inherit;
        font-size: 30px;
        height: 695px;
    }

    .photo_card{
        margin: 10px;
        padding: 10px;
        position: relative;
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
        font-size: 30px;
    }

    #myImg, #photoImg{
        border-radius: 45px;
        width: 200px;
        height: 200px;
        background-position: center;
        background-size: contain;
    }

    #myDiv, #photoDiv{
        border-radius: 45px;
        text-align: center;
        border:solid 1px;
        width: 200px;
        height: 200px;
        margin: 10px;
        cursor:pointer;
        background-position: center;
        background-size: contain;
    }

    button{
        background-color: #084298;
        font-size: 20px;
        border: ridge;
        color: white;
        padding: 10px 20px;
        text-align: center;
        display: inline-block;
        margin-bottom:25px;
    }

</style>