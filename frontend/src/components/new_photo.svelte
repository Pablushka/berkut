<script>
  import { createEventDispatcher } from "svelte";
  import HacerMierdaIcon from "../../public/img/icons/hacer_mierda_rojo.png";
  import { get_current_component } from "svelte/internal";

  export let src = "";

  let inputPhoto;
  let photoImg;

  const my_component = get_current_component();

  const dispatch = createEventDispatcher();

  const newPhoto = (e) => {
    let file = e.target.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = function (readerEvent) {
      let content = readerEvent.target.result;
      photoImg.setAttribute("src", content);
    };

    dispatch("photoLoaded", {});
  };

  const selectPhoto = () => {
    inputPhoto.click();
  };

  const deletePhoto = () => {
    my_component.$destroy();
  };
</script>

<div id="photoDiv" class="photo-div" on:click={() => selectPhoto()}>
  <div class="delete-icon-container">
    <img
      class="delete-icon"
      on:click={() => deletePhoto()}
      src={HacerMierdaIcon}
      alt="eliminar"
    />
  </div>
  <input
    class="input-file"
    bind:this={inputPhoto}
    on:change={newPhoto}
    type="file"
    name="file"
    style="display: none;"
  />
  <img bind:this={photoImg} class="photoImg" {src} alt="Elige una IMAGEN" />
</div>

<style>
  .delete-icon-container {
    position: absolute;
    float: right;
  }

  .delete-icon {
    width: 60px;
    height: 60px;
  }

  .delete-icon:hover {
    width: 70px;
    height: 70px;
  }

  .photoImg {
    border-radius: 45px;
    width: 100%;
    height: 100%;
    object-fit: cover;
    background-position: center;
    background-size: contain;
  }

  #photoDiv {
    border-radius: 45px;
    text-align: center;
    border: solid 1px;
    width: 200px;
    height: 200px;
    margin: 10px;
    cursor: pointer;
    background-position: center;
    background-size: contain;
  }

  .ocultadito {
    display: none;
  }
</style>
