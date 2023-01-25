<script>
  import sirenowoman from '../../public/img/sirenowoman.jpg'
  import sirenaman from '../../public/img/sirenaman.jpg'
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
    <img class="member_photo" src={sirenaman} alt="Natalia Cesario">
    <p>Natalia Cesario</p> 
  </div>

  <div class="card">
    <img class="member_photo" src={sirenaman} alt="Natalia Cesario">
    <p>Natalia Cesario</p> 
  </div>

  <div class="card">
    <img class="member_photo" src={sirenaman} alt="Natalia Cesario">
    <p>Natalia Cesario</p> 
  </div>

  <div class="card">
    <img class="member_photo" src={sirenaman} alt="Natalia Cesario">
    <p>Natalia Cesario</p> 
  </div>

  <div class="card">
    <img class="member_photo" src={sirenaman} alt="Natalia Cesario">
    <p>Natalia Cesario</p> 
  </div>

</div>

<style>
  .member_photo {
    width: 200px;
    border-radius: 10%;
    padding: 10pt;
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
    background-color: #b35837be;
    border-radius: 15px;
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