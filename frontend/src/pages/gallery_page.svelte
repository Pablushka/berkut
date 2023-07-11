
<script>
  import avellaneda_viaja_en_el_tiempo from "../../public/img/eventos/avellaneda_viaja_en_el_tiempo.jpg";
  import f_m_malvinas_argentinas from "../../public/img/eventos/f_m_malvinas_argentinas.jpg";
  import f_m_del_sur from "../../public/img/eventos/f_m_del_sur.jpg";

  import { Button } from "sveltestrap";
  import Router from "svelte-spa-router";
  import fm_del_sur from "./fm_del_sur.svelte";
  import {push, pop, replace} from 'svelte-spa-router';

  const openPhotoGallery = () => {
    push('/fm_del_sur')
  }

</script>

<div class="anti-pajaro">
  <h1 class="mt-5"><span class="gallery_text">Recuerdos de Eventos Pasados</span></h1>

  <div class="gallerys">
    <div class="card">
      <div>
        <img class="gallery_photo" on:click={openPhotoGallery} src={f_m_del_sur} alt="f_m_del_sur" />
        <p class="gallery_text">Feria Medieval Del Sur, Agosto 2022</p>
      </div>
    </div>

    <div class="card">
      <div>
        <button class="image-button"><img class="gallery_photo" src={avellaneda_viaja_en_el_tiempo} alt="avellaneda_viaja_en_el_tiempo" /></button>
        <p class="gallery_text">Avellaneda Viaja En El Tiempo, Mayo 2023</p>
      </div>
    </div>

    <div class="card">
      <div>
        <button class="image-button"><img class="gallery_photo" src={f_m_malvinas_argentinas} alt="f_m_malvinas_argentinas" /></button>
        <p class="gallery_text">Feria Medieval Malvinas Argentinas, Julio 2023 (proximamente)</p>
      </div>
    </div>
    
  </div>

</div>

<style>
  .gallery_photo {
    border-radius: 3%;
    height: 250px;
  }

  .gallerys {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    
  }

  .gallerys .card {
    max-width: 300px;
    margin: 10pt;
    text-align: center;
    background-color: rgba(255, 255, 255, 0);
    border-radius: 20px;
    padding: 10px;
    border: 0px;
  }

  .gallerys .card p {
    text-align: center;
    font-size: 1em;
  }

  .gallery_text {
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

  .image-button {
    padding: 0px;
  }

</style>
