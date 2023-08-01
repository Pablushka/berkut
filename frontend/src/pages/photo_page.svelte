
<script>
    import { Button, Carousel, CarouselControl, CarouselItem, Styles } from 'sveltestrap';
    //import fm_01 from "../../public/img/galleries/f_m_del_sur/fm_01.jpg";

    const items = [
      fm_01,
  ];

  let activeIndex = 0

  const openCarousel = () => {
    let carousel_container = document.getElementById("carousel")
    let gallery_container = document.getElementById("gallery")
    carousel_container.classList.remove("ocultadito")
    carousel_container.classList.add("show-carousel")
    gallery_container.classList.add("ocultadito")
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

      <img class="gallery_photo" on:click={openCarousel} src={fm_01} alt="Natalia Cesario" /> 
      <img class="gallery_photo" on:click={openCarousel} src={fm_02} alt="Natalia Cesario" />
      <img class="gallery_photo" on:click={openCarousel} src={fm_03} alt="Natalia Cesario" />
      <img class="gallery_photo" on:click={openCarousel} src={fm_04} alt="Natalia Cesario" />
      <img class="gallery_photo" on:click={openCarousel} src={fm_05} alt="Natalia Cesario" />
      <img class="gallery_photo" on:click={openCarousel} src={fm_06} alt="Natalia Cesario" />
      <img class="gallery_photo" on:click={openCarousel} src={fm_07} alt="Natalia Cesario" />
      <img class="gallery_photo" on:click={openCarousel} src={fm_08} alt="Natalia Cesario" />
      <img class="gallery_photo" on:click={openCarousel} src={fm_09} alt="Natalia Cesario" />
      <img class="gallery_photo" on:click={openCarousel} src={fm_10} alt="Natalia Cesario" />

  </div>
</div>


<style>
  .gallery_photo {
    border-radius: 3%;
    max-width: 300px;
    margin: 10px;
  }

  .gallerys {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
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
  