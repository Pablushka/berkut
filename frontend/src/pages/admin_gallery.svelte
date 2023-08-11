<script>
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
    let formLabel = "";

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
            .then((data) => {
                console.log("Success:", data);
                document.getElementById("flyer").style.cursor = "pointer";
                document.getElementById("title").innerText = gallery.title;
            })

            .catch((error) => {
                console.error("Error:", error);
            }); 
    }

    var input = document.createElement('input');
    input.type = 'file';
    input.style.display = 'none';
    document.body.appendChild(input);

    var myDiv = document.getElementById("flyer");
    myDiv.addEventListener('click', function() {
        input.click();
    });

    input.onchange = function(e) { 
        var file = e.target.files[0]; 
        var reader = new FileReader();
        reader.readAsDataURL(file); 

        reader.onload = function(readerEvent) {
            var content = readerEvent.target.result; 
            var myImg = document.getElementById("myImg");
            myImg.setAttribute('src', content);
        }
    };


  
</script>

<div class="anti-pajaro">
    <h1 id="title" class="titel">New Gallery</h1>
    <div class="contenedor">
        <div class="flyer_card">
<!--quiero que acá se suban los flyers de galeria-->
            <div id="flyer">PUSH Flyer</div>
            <img id="myImg" width="150px" src="" alt="Sin foto"/>
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
<!--quiero que los botones hagan la carga, editen y eliminen en DB-->
            <div>
                <button on:click={()=> saveGallery()}>Cargar</button>
                <button>Editar</button>
                <button>Eliminar</button>
            </div>
        </div>
        <div class="contenedor_img">
            <div class="photo_card">
<!--quiero que el primer div sea el que haga el push de la foto y 
se muestren las fotos dentro de la galeria si esta ya existe-->
                <div class="img"><h2>PUSH Photo</h2></div>
            </div>
            <!--este dive es opcional 
                <div>
                <button>Cargar</button>
                <button>Editar</button>
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
    .titel {
        font-family: Viking-Normal;
        margin: 15px;
        text-decoration: underline;
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
        height: 710px;
    }

    .photo_card{
        margin: 10px;
        padding: 10px;
        position: relative;
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
    }

    .img{
        border-radius: 45px;
        text-align: center;
        border:solid 1px;
        padding-top: 75px;
        width: 200px;
        height: 200px;
        margin: 10px;
        cursor: pointer;

    }

    #flyer{
        border-radius: 45px;
        text-align: center;
        border:solid 1px;
        padding-top: 75px;
        width: 200px;
        height: 200px;
        margin: 10px;
        cursor:not-allowed;
    }

    button{
        background-color: rgba(0, 15, 128, 0.892);
        font-size: 20px;
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        display: inline-block;
        margin-bottom:25px;
    }
</style>