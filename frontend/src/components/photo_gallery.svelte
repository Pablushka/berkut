<script>
  import { onMount } from "svelte";
  import NewPhoto from "../components/new_photo.svelte";

  export let gallery = null;

  let containerPhoto;
  let new_photos = [];
  let new_photo;
  let blank_photo;

  onMount(() => {
    if (gallery != null) {
      console.log("PhotoGallery:", gallery);
      gallery.photos
        .filter((p) => p.type === "photo")
        .forEach((photo) => {
          console.log(photo.image);
          new_photos.push(
            new NewPhoto({
              target: containerPhoto,
              props: { src: `/img/galleries/${gallery.id}/${photo.image}` },
            })
          );
        });
    }

    // blank_photo.$on("photoLoaded", onPhotoLoaded);
  });

  const onPhotoLoaded = () => {
    blank_photo = new NewPhoto({
      target: containerPhoto,
      props: {},
    });

    blank_photo.$on("photoLoaded", onPhotoLoaded);
  };

  const newPhoto = () => {
    new_photo = new NewPhoto({
      target: containerPhoto,
      props: {},
    });
  };
</script>

<div class="contenedor_img">
  <div bind:this={containerPhoto} id="containerPhoto" class="photo_card" />
  <div>
    <button on:click={newPhoto}>Add Foto</button>
  </div>
</div>

<style>
  .photo_card {
    margin: 10px;
    padding: 10px;
    position: relative;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    font-size: 30px;
  }

  .contenedor_img {
    width: 80%;
    height: 705px;
    overflow-y: auto;
    margin-right: 20px;
  }

  button {
    background-color: #084298;
    font-size: 20px;
    border: ridge;
    color: white;
    padding: 10px 20px;
    text-align: center;
    display: inline-block;
    margin-bottom: 25px;
  }
</style>
