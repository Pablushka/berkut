<script>
  import ale from '../../public/img/ale.png'
  import jonny from '../../public/img/jonny.png'
  import maga from '../../public/img/maga.png'
  import mati_p from '../../public/img/mati_p.png'
  import victor from '../../public/img/victor.png'
  import trini from '../../public/img/trini.png'
</script>

<h1 class="mt-5">Integrantes del grupo</h1>
<h2>Un vistazo a los miembros</h2>

<div class="members">

  <div class="card">
    <div>
      <img class="member_photo" src={trini} alt="Natalia Cesario">
    </div>
    <div>
      <h3>Trini</h3>
      <p>Druida del grupo, lectora de la fortuna</p>
    </div>
    
  </div>

  <div class="card">
    <div>
      <img class="member_photo" src={ale} alt="Natalia Cesario">
    </div>
    <div>
      <h3>Alejandra</h3>
      <p>Encargada de redes sociales</p>
    </div>
  </div>

  <div class="card">
    <div>
      <img class="member_photo" src={jonny} alt="Natalia Cesario">
    </div>
    <div>
      <h3>Jonny</h3>
      <p>Jarl, encargado de relaciones publicas</p>
    </div>
  </div>

  <div class="card">
    <div>
      <img class="member_photo" src={maga} alt="Natalia Cesario">
    </div>
    <div>
      <h3>Magali</h3>
      <p>Modista principal del grupo</p>
    </div>
  </div>

  <div class="card">
    <div>
      <img class="member_photo" src={mati_p} alt="Natalia Cesario">
    </div>
    <div>
      <h3>Matias M</h3>
      <p>Guerrero encargado de lanzas</p>
    </div>
  </div>

  <div class="card">
    <div>
      <img class="member_photo" src={victor} alt="Natalia Cesario">
    </div>
    <div>
      <h3>Victor</h3>
      <p>Maestro carpintero</p>
    </div>
  </div>

</div>

<style>
  .member_photo {
    width: 200px;
    border-radius: 10%;
  }

  .members {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;

  }

  .members .card {
    width: 500px;
    min-height: 300px;
    margin: 10pt;
    padding: 10pt;
    text-align: center;
    background-color: #ffffffbe;
    border-radius: 45px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
  }

  .members .card p {
    text-align: left;
    font-size: 1em;
  }

  .member_titel{
    
  }

  .member_text {
    font-size: large;
  }

</style>