<script>
  import ale from "../../public/img/ale.png";
  import jonny from "../../public/img/jonny.png";
  import maga from "../../public/img/maga.png";
  import mati_p from "../../public/img/mati_p.png";
  import victor from "../../public/img/victor.png";
  import trini from "../../public/img/trini.png";
  import mati_b from "../../public/img/mati_b.png";
  import mati_s from "../../public/img/mati_s.png";
  import nati from "../../public/img/nati.png";
  import nico from "../../public/img/nico.png";
  import pablo_a from "../../public/img/pablo_a.png";
</script>

<div class="anti-pajaro">
  <h1 class="mt-5"><span class="member_text">Integrantes del grupo</span></h1>
  <h2 class="member_text">Un vistazo a los miembros</h2>

  <div class="members">
    <div class="card">
      <div>
        <img class="member_photo" src={trini} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Trini</h3>
        <p class="member_text">Druida, lectora de la fortuna</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={ale} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Alejandra</h3>
        <p class="member_text">Encargada de redes sociales</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={jonny} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Jonny</h3>
        <p class="member_text">Jarl, encargado de relaciones publicas</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={maga} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Magali</h3>
        <p class="member_text">Modista principal del grupo</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={mati_p} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Matias M</h3>
        <p class="member_text">Guerrero encargado de lanzas</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={victor} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Victor</h3>
        <p class="member_text">Maestro carpintero</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={mati_b} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Matias B</h3>
        <p class="member_text">Locutor oficial del grupo</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={mati_s} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Matias S</h3>
        <p class="member_text">Segundo jarl, encargado de armas</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={nati} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Natalia</h3>
        <p class="member_text">Segunda modista del grupo</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={nico} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Nicolas</h3>
        <p class="member_text">Encargado de la cocina</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={pablo_a} alt="Natalia Cesario" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_titel">Pablo A</h3>
        <p class="member_text">Guerrero encargado de armas</p>
      </div>
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
    width: 550px;
    min-height: 300px;
    margin: 10pt;
    text-align: center;
    background-color: rgba(255, 255, 255, 0);
    border-radius: 45px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
  }

  .members .card p {
    text-align: center;
    font-size: 1.5em;
  }

  .member_titel {
    font-family: Viking-Normal;
  }

  .member_text {
    font-family: PR Viking;
    font-size: 50pt;
    text-align: center;

  }

  .contenedor_member_text {
    width: 50%;
  }

  .anti-pajaro {
    border: solid 3px;
    margin-top: 40px;
    background-color: #ffffffed;
    border-radius: 42px;
  }
</style>
