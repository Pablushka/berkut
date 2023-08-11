
<script>

  import { Button } from "sveltestrap";
  import Router from "svelte-spa-router";
  import {push, pop, replace} from 'svelte-spa-router';
  import {onMount} from "svelte";

  let endpoint = "http://127.0.0.1:5000/galleries"
  let galleries = []

  onMount(async () => {
    let response = await fetch(endpoint)
    galleries = await response.json()
    console.log(galleries)
  })

  const openPhotoGallery = (id) => {
    push(`/photo_page/${id}`)
  }


</script>

<div class="anti-pajaro">
  <h1 class="mt-5"><span class="gallery_text">Recuerdos de Eventos Pasados</span></h1>

  <div class="gallerys">
    {#each galleries as {flyer, title, id}}
      <div class="card">
        <div>
          <img class="gallery_photo" on:click={openPhotoGallery(id)} src="/img/galleries/{flyer}" alt={title} />
          <p class="gallery_text">{title}</p>
        </div>
      </div>
    {/each}
    
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
    justify-content: center;
    
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
    text-decoration: underline;
  }

  .anti-pajaro {
    width: 1500px;
    border: solid 3px;
    margin-top: 40px;
    background-color: #ffffffed;
    border-radius: 42px;
  }

</style>
