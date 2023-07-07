
<script>
  import avellaneda_viaja_en_el_tiempo from "../../public/img/eventos/avellaneda_viaja_en_el_tiempo.jpg";
  import f_m_malvinas_argentinas from "../../public/img/eventos/f_m_malvinas_argentinas.jpg";
</script>

<div class="anti-pajaro">
  <h1 class="mt-5"><span class="member_text">Recuerdos de Eventos Pasados</span></h1>

  <div class="members">
    <div class="card">
      <div>
        <img class="member_photo" src={avellaneda_viaja_en_el_tiempo} alt="Natalia Cesario" />
        <p class="member_text">Avellaneda Viaja En El Tiempo, Mayo 2023</p>
      </div>
    </div>
  </div>

  <div class="members">
    <div class="card">
      <div>
        <img class="member_photo" src={f_m_malvinas_argentinas} alt="Natalia Cesario" />
        <p class="member_text">Feria Medieval Malvinas Argentinas, julio 2023</p>
      </div>
    </div>
  </div>

</div>

<style>
  .member_photo {
    width: 200px;
    border-radius: 3%;
  }

  .members {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    
  }

  .members .card {
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
    font-size: 1em;
  }

  .member_text {
    font-family: PR Viking;
    font-size: 50pt;
    text-align: center;
  }

  .anti-pajaro {
    width: 1500px;
    border: solid 3px;
    margin-top: 40px;
    background-color: #ffffffed;
    border-radius: 42px;
  }

</style>
