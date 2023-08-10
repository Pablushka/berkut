<script>

</script>
<div class="anti-pajaro">
    <h1 class="titel">esta es la pag de admin gallery</h1>
    <div class="contenedor">
        <div class="flyer_card">
    <!--acá se cargan los flyers para caratula de galeria-->
            <div class="img"><h2>PUSH Flyer</h2></div>
            <div><p>flyer:----<br>titulo:----<br>fecha:----</p></div>
    <!--acá se cargan los datos en DB-->
            <div>
                <button>Cargar</button>
                <button>Editar</button>
                <button>Eliminar</button>
            </div>
        </div>
        <div>
            <div class="photo_card">
                <div class="img"><h2>PUSH Photo</h2></div>
                <div class="img"><h2>Photo</h2></div>
                <div class="img"><h2>Photo</h2></div>
                <div class="img"><h2>Photo</h2></div>
                <div class="img"><h2>Photo</h2></div>
                <div class="img"><h2>Photo</h2></div>
            </div>
            <div>
                <button>Cargar</button>
                <button>Editar</button>
                <button>Eliminar</button>
            </div>
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
        
    }

    .contenedor{
        display: flex ;
        position: relative ;
        background-color: rgba(255, 255, 255, 0);
        flex-direction: row ;
        border-radius: 42px;
    }
    
    .titel {
        font-family: Viking-Normal;
        margin: 15px;
    }

    .flyer_card{
    align-items: center ;
    display: flex ;
    flex-direction: column;
    overflow: hidden;
    padding: 16px;
    width: 416px;
    background-color: rgba(54, 52, 52, 0.163);
    justify-content: space-evenly;
    border-bottom-left-radius: inherit;

    }

    .photo_card{
        margin: 10px;
        padding: 10px;
        position: relative;
        flex: 1;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-evenly;
    }

    .img{
        border-radius: 45px;
        text-align: center;
        border:solid 1px;
        padding: 40px;
        width: 200px;
        height: 200px;
        margin-bottom: 10px;

    }

    button{
        background-color: green;
        font-size: 20px;
        border: none;
        color: white;
        padding: 14px 24px;
        text-align: center;
        display: inline-block;
        margin-bottom:25px;
    }
</style>