<script>
  import { onMount } from "svelte/internal";
  import { Form, FormGroup, Input, Label } from "sveltestrap";
  import PhotoGallery from "../components/photo_gallery.svelte";

  export let params = {};

  let formLabel = "";
  let photitos;
  let gallery = null;
  let action = "Crear"

  console.log(params); 

  const getFullGallery = async (gallery_id) => {
    if (gallery_id == null) {
      return null;
    }

    let endpoint = `http://127.0.0.1:5000/gallery/${gallery_id}`;
    let response = await fetch(endpoint);
    return await response.json();
  };

  const saveGallery = () => {
    let title = document.getElementById("field_title").value;
    let date = document.getElementById("field_date").value;

    let gallery = {
      title: title,
      date: date,
      flyer: "",
    };

    if (!validate()) {
      return;
    }

    fetch("http://127.0.0.1:5000/gallery", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(gallery),
    })
      .then((response) => response.json())
      .then((new_gallery) => {
        console.log("Success:", new_gallery);
        document.getElementById("myImg").style.cursor = "pointer";
        document.getElementById("title").innerText = gallery.title;
        uploadImg(new_gallery.id, "flyer");
        document.getElementById("myButton").disabled = true;
        document.getElementById("myButton").style.cursor = "not-allowed";
        uploadImg(new_gallery.id, "photo");
      })

      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const validate = () => {
    let flyer = document.getElementById("myImg");
    let title = document.getElementById("field_title");
    let date = document.getElementById("field_date");

    if (flyer.naturalWidth <= 0) {
      alert("No se puede crear galeria sin flyer");
      return false;
    }

    if (title.value === "") {
      alert("No puede crear galeria sin titulo");
      return false;
    }
    if (!(title.value.length >= 10 && title.value.length <= 100)) {
      alert(
        "El titulo de la galeria no puede ser menos a 15 caracteres ni mayor a 100"
      );
      return false;
    }

    if (date.value === "") {
      alert("No puede crear galeria sin fecha");
      return false;
    }

    return true;
  };

  const upload = (formData, gallery_id, type) => {
    fetch(`http://127.0.0.1:5000/upload/${type}/${gallery_id}`, {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("success", data);
      });
  };

  const uploadImg = (gallery_id, type) => {
    let form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("enctype", "multipart/form-data");
    form.setAttribute(
      "action",
      `http://127.0.0.1:5000/upload/${type}/${gallery_id}`
    );

    form.onsubmit = (e) => {
      e.preventDefault();
    };

    let fileInput;

    if (type === "flyer") {
      fileInput = document.getElementById("myFlyer");
      form.appendChild(fileInput);
      document.body.appendChild(form);
      let formData = new FormData(form);
      upload(formData, gallery_id, type);
    } else {
      let photo_list = Array.from(
        document.getElementsByClassName("input-file")
      );
      photo_list.forEach((input) => {
        form.appendChild(input);
        let formData = new FormData(form);
        upload(formData, gallery_id, type);
        form.removeChild(input);
      });
    }
  };

  onMount(async () => {
    let input = document.createElement("input");
    input.id = "myFlyer";
    input.type = "file";
    input.name = "file";
    input.style.display = "none";
    document.body.appendChild(input);
    gallery = await getFullGallery(params.id);
    console.log ("params.id", params.id)

    if (params.id){
      action = "Editar"
    } 

    if (gallery == null) {
      photitos = [];
    } else {
      photitos = gallery.photos;
    }

    console.log("galeria", photitos);

    input.onchange = function (e) {
      let file = e.target.files[0];
      let reader = new FileReader();
      reader.readAsDataURL(file);

      reader.onload = function (readerEvent) {
        let content = readerEvent.target.result;
        let myImg = document.getElementById("myImg");
        myImg.setAttribute("src", content);
      };
    };
  });

  const selectFlyer = () => {
    let input = document.getElementById("myFlyer");
    input.click();
  };
</script>

<div class="page-container anti-pajaro">
  <h1 id="title" class="title">{gallery?.title ?? "Sin título aún"}</h1>
  <div class="contenedor">
    <div class="flyer_card">
      <div id="myDiv" on:click={() => selectFlyer()}>
        <img
          id="myImg"
          width="150px"
          src="/img/galleries/{gallery?.flyer}"
          alt={gallery?.title}
        />
      </div>
      <div>
        <Form>
          <input value="" id="field_id" type="hidden" name="id" />

          <FormGroup style={formLabel}>
            <Label for="field_title">Titulo</Label>
            <Input
              type="text"
              value={gallery?.title}
              id="field_title"
              name="title"
            />
          </FormGroup>

          <FormGroup style={formLabel}>
            <Label for="field_date">Fecha</Label>
            <Input
              type="date"
              value={gallery?.date.split("-")[2] +
                "-" +
                gallery?.date.split("-")[1] +
                "-" +
                gallery?.date.split("-")[0]}
              id="field_date"
              name="date"
            />
          </FormGroup>
        </Form>
      </div>
      <div>
        <button id="myButton" on:click={() => saveGallery()}
          >{action} Galeria</button
        >
      </div>
    </div>

    {#await getFullGallery(params.id) then gallery}
      <PhotoGallery {gallery} />
    {/await}
  </div>
</div>

<style>
  .anti-pajaro {
    border: solid 3px;
    margin-top: 40px;
    background-color: #ffffffed;
    border-radius: 42px;
    height: 800px;
  }

  .contenedor {
    display: flex;
    position: relative;
    background-color: rgba(255, 255, 255, 0);
    flex-direction: row;
    border-radius: 42px;
    height: 88%;
  }

  .flyer_card {
    align-items: center;
    display: flex;
    flex-direction: column;
    padding: 16px;
    background-color: rgba(54, 52, 52, 0.163);
    justify-content: space-evenly;
    border-radius: inherit;
    font-size: 30px;
    height: 695px;
    margin-left: 10px;
  }

  #myImg {
    border-radius: 45px;
    width: 100%;
    height: 100%;
    object-fit: cover;
    background-position: center;
    background-size: contain;
  }

  #myDiv {
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
