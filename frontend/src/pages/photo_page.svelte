
<script>
  import { Button, Carousel, CarouselControl, CarouselItem, Styles } from 'sveltestrap';
  //import fm_01 from "../../public/img/galleries/1/1.jpg";
  import {push, pop, replace} from 'svelte-spa-router';
  import {onMount} from "svelte";

  export let params = {}
  
  console.log (params)
  const gallery_id = params.gallery_id
  
  let endpoint =`http://127.0.0.1:5000/gallery/${gallery_id}/photo`
  let photos = []

  let items = []

  onMount(async () => {
    let response = await fetch(endpoint)
    photos = await response.json()
    console.log(`/img/galleries/${gallery_id}/${photos[0].image}`)
    items = photos.map((photo) => {
      return `/img/galleries/${gallery_id}/${photo.image}`
    })
  })

  let activeIndex = 0

  const openCarousel = (index) => {
    let carousel_container = document.getElementById("carousel")
    let gallery_container = document.getElementById("gallery")
    carousel_container.classList.remove("ocultadito")
    carousel_container.classList.add("show-carousel")
    gallery_container.classList.add("ocultadito")
    activeIndex = index
    console.log(index)
  }

  const closeCarousel = () => {
    let carousel_container = document.getElementById("carousel")
    let gallery_container = document.getElementById("gallery")
    carousel_container.classList.add("ocultadito")
    gallery_container.classList.remove("ocultadito")
  }

</script>

<div class ="show-carousel ocultadito" id="carousel">
  <Carousel {items} bind:activeIndex>
    <div class="carousel-inner">
      {#each items as item, index}
        <CarouselItem bind:activeIndex itemIndex={index}>
          <img src={item} class="d-block w-100" alt={`${item} ${index + 1}`} />
        </CarouselItem>
      {/each}
    </div>
  
    <div class="d-flex justify-content-between p-2">
      <Button on:click={() => activeIndex = Math.max(activeIndex - 1, 0)}>
        Back
      </Button>
      <Button on:click={closeCarousel}>
        Gallery
      </Button>
      <Button on:click={() => activeIndex = Math.min(activeIndex + 1, items.length - 1)}>
        Next
      </Button>
    </div>
  </Carousel>
</div>

<div class="anti-pajaro" id="gallery">
  <h1 class="mt-5"><span class="gallery_text">Feria Medieval del Sur</span></h1>
  <div class="gallerys">

    {#each photos as {image, gallery_id}, index}
      <div>
        <div>
          <img class="gallery_photo" on:click={() => openCarousel(index)} src="/img/galleries/{gallery_id}/{image}" alt="la foto no sale AHHHHHHH"/>
        </div>
      </div>
    {/each}

      <!-- <img class="gallery_photo" on:click={openCarousel} src={fm_01} alt="Natalia Cesario" /> -->

  </div>
</div>


<style>
  .gallery_photo {
    border-radius: 3%;
    max-width: 300px;
    margin: 10px;
    border: 10px;
    border-style: outset;
    border-color: #8f8f8f;
  }

  .gallerys {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    align-items: center;
  }
  
  .gallery_text {
    font-family: PR Viking;
    font-size: 50pt;
    text-align: center;
  }
  
  .anti-pajaro {
    width: 1100px;
    border: solid 1px;
    margin-top: 40px;
    background-color: #ffffffed;
    border-radius: 42px;
  }

  .ocultadito {
    display: none !important;
  }

  .show-carousel {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding-top: 10px;
    width: 1200px;
  }
  
</style>
  