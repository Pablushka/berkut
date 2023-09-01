<script>
    // @ts-nocheck
    
    import { onMount } from 'svelte';
    import { Form, Button, FormGroup, FormText, Input, Label, Modal, ModalBody, ModalFooter, ModalHeader } from 'sveltestrap';
    import {bad_words_validator} from '../helpers/admin_helpers.js';
    import {push, pop, replace} from 'svelte-spa-router';
    
    let bad_words = ['culo', 'puto el que lee', 'macri', 'chupito el pame']
    
    let open = false;
    
    let current_gallery = null;
      
    const toggle = () => (open = !open);
      
    const fill = () => {
        
        if (current_gallery == null) {
          
            let date_parts = (new Date()).toLocaleDateString().split('/')
            let today = date_parts[2] + '-' + date_parts[1] + '-' + date_parts[0];
    
            document.getElementById("field_date").value = today;
            return;
        }
    
        let components = current_gallery.date.split("-");    
        let new_date = `${components[2]}-${components[1]}-${components[0]}`;
    
        document.getElementById("field_id").value = current_gallery.id;
        document.getElementById("field_flyer").value = current_gallery.flyer;
        document.getElementById("field_title").value = current_gallery.title;
        document.getElementById("field_date").value = new_date;
    }
    
    // const form_fill = (the_gallery) => {
    //     toggle();
    //     current_gallery = the_gallery;
    // };

    const openEditGallery = (id) => {
        push(`/admin_gallery/${id}`)
    }
    
    let my_galleries=[];

    async function getGalleries() {
    
        let response = await fetch("http://localhost:5000/galleries");
        let galleries = await response.json();
      
        return galleries;
    
    }
    
    onMount(async () => {
        my_galleries = await getGalleries();
    })
    
    const deleteGallery = (id) => {
        let confirmed = confirm(
            "¿Está usted seguro que quiere hacer mierda la galeria?"
        );

        if (!confirmed) {
            return;
        }

        confirmed = confirm(
            "Al borrar la galeria perdera todas las imagenes, ¿está seguro que quiere borrar TODO?"
        );

        if (!confirm) {
            return;
        }

        fetch(`http://localhost:5000/gallery/${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((response) => response.json())
        .then((data) => {
            console.log("Success:", data);
            getGalleries().then((galleries) => {
                my_galleries = galleries;
            });
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    };
    
    const saveGallery= () =>{
        let id = document.getElementById("field_id").value;
        let flyer = document.getElementById("field_flyer").value;
        let title = document.getElementById("field_title").value;
        let date = document.getElementById("field_date").value;

        let components = date.split("-");
        let new_date = `${components[2]}-${components[1]}-${components[0]}`;

        let gallery = {
            id: id,
            flyer: flyer, 
            title: title,
            date: new_date,
        };

        fetch("http://localhost:5000/gallery", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(gallery),
        })
        .then((response) => response.json())
        .then((data) => {
            console.log("Success:", data);
            getGalleries().then((galleries) => {
                my_galleries = galleries;
            });

            toggle();
        })

        .catch((error) => {
            console.error("Error:", error);
        }); 
    }
    
    let formLabel = "text-align: left; font-weight: bold;";
    
</script>
    
<div class="page-container">
    <h3 class="titel">Galerias</h3>
    <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th>Flyer</th>
            <th>Titulo</th>
            <th>Fecha</th>
            <th colspan="2">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {#each my_galleries as gallery}
          <tr>
            <td style="white-space: nowrap;">{gallery.flyer}</td>
            <td style="white-space: nowrap;">{gallery.title}</td>
            <td style="white-space: nowrap;">{gallery.date}</td>
            <td>
            <button on:click={()=>openEditGallery(gallery)} class="btn btn-primary btn-sm btn-berkut boton-uno">Editar</button>
            </td>
            <td>
              <button class="btn btn-danger btn-sm btn-berkut boton-dos" on:click={()=>{deleteGallery(gallery.id)}}>Eliminar</button>
            </td>
          </tr>
          {/each}
    
        </tbody>
    
    </table>
    
    <div>           
        <Modal on:open={fill} isOpen={open} {toggle} id="gallery_modal">
          <ModalHeader {toggle}>Galeria</ModalHeader>
          <ModalBody>
            <Form>              
                    <input value="" 
                    id="field_id" 
                    type="hidden"
                    name="id"/>
                
                <FormGroup style={formLabel}>
                    <Label for="flyer">Flyer</Label>
                    <Input value="" 
                        id="field_flyer" 
                        name="flyer"/>
                    </FormGroup>
                    
                <FormGroup style={formLabel}>
                    <Label for="title">Titulo</Label>
                    <Input type="textarea" 
                    name="title" 
                    id="field_title"/>
                </FormGroup> 
    
                <FormGroup style={formLabel}>
                    <Label for="date">Fecha</Label>
                    <Input
                    type="date"
                    name="date"
                    id="field_date"
                    placeholder="date placeholder"/>
                </FormGroup>
            </Form>
          </ModalBody>
    
          <ModalFooter>
            <Button color="primary" on:click={saveGallery}>Guardar</Button>
            <Button color="secondary" on:click={toggle}>Cancelar</Button>
          </ModalFooter>
    
        </Modal>
    
    </div>
    
</div>
    
    
    
<style>
      
    .page-container {
        background-color: #e3e2df7d;
        padding: 35px;
        margin-top: 39px;
        border-radius: 25px;
        text-align: left;
        font-family: cursive;
        font-size: x-large;
    }
    
    .btn-berkut {
        width: 95px;
        height: 45px;
    } 
    
    .boton-uno{
        border: ridge;
        background-color: #084298;
    }

    .boton-dos{
        border: ridge;
        background-color: #c00011;
    }

</style>