<script>
  import ale from "../../public/img/members/ale.png";
  import jonny from "../../public/img/members/jonny.png";
  import maga from "../../public/img/members/maga.png";
  import mati_p from "../../public/img/members/mati_p.png";
  import victor from "../../public/img/members/victor.png";
  import trini from "../../public/img/members/trini.png";
  import mati_b from "../../public/img/members/mati_b.png";
  import mati_s from "../../public/img/members/mati_s.png";
  import nati from "../../public/img/members/nati.png";
  import nico from "../../public/img/members/nico.png";
  import pablo_a from "../../public/img/members/pablo_a.png";
</script>

<div class="anti-pajaro">
  <h1 class="mt-5"><span class="title">Integrantes del grupo</span></h1>
  <h2 class="member_text">Un vistazo a los miembros</h2>

  <div class="members">
    <div class="card">
      <div>
        <img class="member_photo" src={trini} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Trini</h3>
        <p class="member_text">Druida, lectora de la fortuna</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={ale} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Alejandra</h3>
        <p class="member_text">Encargada de redes sociales</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={jonny} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Jonny</h3>
        <p class="member_text">Jarl, encargado de relaciones publicas</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={maga} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Magali</h3>
        <p class="member_text">Modista principal del grupo</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={mati_p} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Matias M</h3>
        <p class="member_text">Guerrero encargado de lanzas</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={victor} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Victor</h3>
        <p class="member_text">Maestro carpintero</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={mati_b} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Matias B</h3>
        <p class="member_text">Locutor oficial del grupo</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={mati_s} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Matias S</h3>
        <p class="member_text">Segundo jarl, encargado de armas</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={nati} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Natalia</h3>
        <p class="member_text">Segunda modista del grupo</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={nico} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Nicolas</h3>
        <p class="member_text">Encargado de la cocina</p>
      </div>
    </div>

    <div class="card">
      <div>
        <img class="member_photo" src={pablo_a} alt="Miembro del grupo Berkut" />
      </div>
      <div class="contenedor_member_text">
        <h3 class="member_title">Pablo A</h3>
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

  .member_title {
    font-family: Viking-Normal;
  }

  .member_text {
    font-family: PR Viking;
    font-size: 35pt;
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
