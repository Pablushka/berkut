<script>
    // @ts-nocheck
    
      import { onMount } from 'svelte';
      import { Form, Button, FormGroup, FormText, Input, Label, Modal, ModalBody, ModalFooter, ModalHeader } from 'sveltestrap';
      import {bad_words_validator} from '../helpers/admin_helpers.js'
    
      let bad_words = ['culo', 'puto el que lee', 'macri', 'chupito el pame']
    
      let open = false;
    
      let current_event = null;
      
      const toggle = () => (open = !open);
      
      const fill = () => {
        
        if (current_user == null) {
          
          let date_parts = (new Date()).toLocaleDateString().split('/')
          let today = date_parts[2] + '-' + date_parts[1] + '-' + date_parts[0];
    
          document.getElementById("field_date").value = today;
          return;
        }
    
        let components = current_user.date.split("-");
        
        // convierto la fecha a YYYY-MM-DD por requerimiento de chrome
        let new_date = `${components[2]}-${components[1]}-${components[0]}`;
    
        document.getElementById("field_date").value = new_date;
        document.getElementById("field_id").value = current_user.id;
        document.getElementById("field_name").value = current_user.name;
        document.getElementById("field_email").value = current_user.email;
        document.getElementById("field_last_login").value = current_user.last_login;
        document.getElementById("field_is_active").value = current_user.is_active;
        document.getElementById("field_is_admin").value = current_user.is_admin;
      }
    
      const form_fill = (the_user) => {
    
        toggle();
    
        current_user = the_user;
      };
        
    
      // function toggle2() {
      //   open = !open;
      // }
    
      let radioGroup;
      let my_users=[];
      let modal;
    
      async function getUsers() {
    
        let response = await fetch("http://localhost:5000/users");
        let users = await response.json();
      
        return users;
    
      }
    
      onMount(async () => {
        my_users = await getUsers();
     })
    
      const deleteUser = (id) => {
    
        let confirmed = confirm("¿Está usted seguro que quiere hacer mierda al usuario?");
    
        if (!confirmed) {
          return;
        }
    
        fetch(`http://localhost:5000/users/${id}`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => response.json())
        .then((data) => {
          console.log("Success:", data);
          getUsers().then((users) => {
            my_users = users;
          });
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    
      }
    
      const saveUser = () => {
    
        let id = document.getElementById("field_id").value;
        let name = document.getElementById("field_name").value;
        let email = document.getElementById("field_email").value;
        let last_login = document.getElementById("field_last_login").value;
        let is_active = document.getElementById("field_is_active").value;
        let is_admin = document.getElementById("field_is_admin").value;
    
        // regular expression to check for bad words
        let pattern = /culo|puto el que lee|macri|chupito el pame/gmi
    
        let result = pattern.test(title + ' ' + text)
        
        if (result) {
          alert("Por favor no utilice estas palabras en el formulario: ")
          return
        }
        
        let components = date.split("-");
    
        // convierto la fecha a DD-MM-YYYY por requerimiento de la API
        let new_date = `${components[2]}-${components[1]}-${components[0]}`;
    
        let user = {
          id: id,
          name: name,
          email: email,
          last_login: last_login,
          is_active: is_active,
          is_admin: is_admin,
        };
    
        let httpMethod = id == '' ? "POST" : "PATCH";
    
        fetch("http://localhost:5000/users", {
          method: httpMethod,
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(user),
        })
        .then((response) => response.json())
        .then((data) => {
          console.log("Success:", data);
          getUsers().then((users) => {
            my_users = users;
          });
    
          toggle();
    
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    
      }
    
      const newEvent = () => {
        toggle();
    
        current_user = null;
    
      }
    
      let formLabel = "text-align: left; font-weight: bold;";
    
    </script>
    
    <div class="page-container">
      <h3>Usuarios</h3>
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th>Usuario</th>
            <th>Email</th>
            <th>Ultima conexión</th>
            <th>Estado</th>
            <th>Nivel</th>
            <th colspan="2">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {#each my_users as user}
          <tr>
            <td style="white-space: nowrap;">{user.name}</td>
            <td style="white-space: nowrap;">{user.email}</td>
            <td style="white-space: nowrap;">{user.last_login}</td>
            <td style="white-space: nowrap;">{user.is_active}</td>
            <td style="white-space: nowrap;">{user.is_admin}</td>
            <td>
              <button on:click={()=>form_fill(user)} class="btn btn-primary btn-sm btn-berkut">Editar</button>
            </td>
            <td>
              <button class="btn btn-danger btn-sm btn-berkut" on:click={()=>{deleteUser(user.id)}}>Eliminar</button>
            </td>
          </tr>
          {/each}
    
        </tbody>
    
      </table>
    
    </div>
    
    
    
    <style>
      
      .page-container {
        background-color: #f0dfc1eb;
        padding: 38px;
        margin-top: 39px;
        border-radius: 25px;
        text-align: left;
      }
    
      .btn-berkut {
        width: 77px;
      } 
    
      .event-field {
       text-align: left;
      }
    
    </style>