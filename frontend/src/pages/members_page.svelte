<script>
  import sirenowoman from '../../public/img/sirenowoman.jpg'
  import sirenaman from '../../public/img/sirenaman.jpg'
</script>

<h1 class="mt-5">Integrantes del grupo</h1>
<h2>Un vistazo a los miembros</h2>

<div class="members">

  <div>
    <img class="member_photo" src={sirenowoman} alt="Natalia Cesario">
    <h3>Natalia Cesario</h3>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maiores, repellendus dolorem? Autem commodi nesciunt reprehenderit nostrum consequuntur magnam sint? Quisquam tempore provident, quia aut voluptatum quod reiciendis tenetur veritatis delectus!</p>
  </div>

  <div>
    <img class="member_photo" src={sirenaman} alt="Natalia Cesario">
    <p>Natalia Cesario</p> 
  </div>

  <div>
    <img class="member_photo" src={sirenaman} alt="Natalia Cesario">
    <p>Natalia Cesario</p> 
  </div>

  <div>
    <img class="member_photo" src={sirenaman} alt="Natalia Cesario">
    <p>Natalia Cesario</p> 
  </div>

  <div>
    <img class="member_photo" src={sirenaman} alt="Natalia Cesario">
    <p>Natalia Cesario</p> 
  </div>

  <div>
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

  .members div {
    width: 300px;
    min-height: 300px;
    margin: 10pt;
    padding: 10pt;
    text-align: center;
    background-color: #b35837be;
    border-radius: 15px;
  }

  .members div p {
    text-align: left;
    font-size: 1em;
  }

</style>