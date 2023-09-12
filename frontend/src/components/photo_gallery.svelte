<script>
  import NewPhoto from "../components/new_photo.svelte";

  export let photoList = [];

  console.log("PhotoGallery: ", photoList);

  let containerPhoto;
  let new_photo;

  console.log("PhotoGallery:", photoList);

  if (photoList != null && photoList.length != 0) {
    photoList.forEach((photo) => {
      new_photo = new NewPhoto({
        target: containerPhoto,
        props: { src: photo.image },
      });

      //   containerPhoto.appendChild(new_photo);
    });
  }

  const onPhotoLoaded = () => {
    let blankPhoto = NewPhoto;
    containerPhoto.appendChild(blankPhoto);
  };

  const newPhoto = () => {
    new_photo = new NewPhoto({
      target: containerPhoto,
      props: {},
    });
  };
</script>

<div class="contenedor_img">
  <div bind:this={containerPhoto} id="containerPhoto" class="photo_card">
    <NewPhoto on:photoLoaded={() => onPhotoLoaded()} />
  </div>
  <div>
    <button on:click={() => newPhoto()}>Add Foto</button>
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
