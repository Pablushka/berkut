<script>

</script>
<div class="anti-pajaro">
    <h1 class="titel">esta es la pag de admin gallery</h1>
    <div class="card">
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

    <div class="card">
        <div class="img"><h2>PUSH Photo</h2></div>
        <div class="img"><h2>Photo</h2></div>
        <div class="img"><h2>Photo</h2></div>
        <div class="img"><h2>Photo</h2></div>
        <div class="img"><h2>Photo</h2></div>
        <div class="img"><h2>Photo</h2></div>
        <div>
            <button>Cargar</button>
            <button>Editar</button>
            <button>Eliminar</button>
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
    
    .titel {
        font-family: Viking-Normal;
        margin: 15px;
    }
    
    .card {
        width: 550px;
        min-height: 300px;
        margin: 10pt;
        background-color: rgba(255, 255, 255, 0);
        border-radius: 45px;
        display: inline-flex;
        font-family: PR Viking;
        font-size: 25pt;
        text-align: center;
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
    }
</style>