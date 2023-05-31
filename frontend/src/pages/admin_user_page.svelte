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
    
        fetch("http://localhost:5000/events", {
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
    
    
    <div style="display: none">
    
      <br />
      <br />
      <br />
      <br />
      <br />
      
      <hr>
    
      <Form>
        <FormGroup>
          <Label for="exampleEmail">Plain Text (Static)</Label>
          <Input plaintext value="Some plain text/ static value" />
        </FormGroup>
        <FormGroup>
          <Label for="exampleEmail">Email</Label>
          <Input 
            type="email" 
            name="email" 
            id="exampleEmail" 
            placeholder="with a placeholder" 
          />
        </FormGroup>
        <FormGroup>
          <Label for="examplePassword">Password</Label>
          <Input
            type="password"
            name="password"
            id="examplePassword"
            placeholder="password placeholder"
          />
        </FormGroup>
        <FormGroup>
          <Label for="exampleUrl">Url</Label>
          <Input
            type="url"
            name="url"
            id="exampleUrl"
            placeholder="url placeholder"
          />
        </FormGroup>
        <FormGroup>
          <Label for="exampleRange">Range</Label>
          <Input
            type="range"
            name="range"
            id="exampleRange"
            min={0}
            max={100}
            step={5}
            placeholder="Range placeholder"
          />
        </FormGroup>
        <FormGroup>
          <Label for="exampleNumber">Number</Label>
          <Input
            type="number"
            name="number"
            id="exampleNumber"
            placeholder="number placeholder"
          />
        </FormGroup>
        <FormGroup>
          <Label for="exampleDatetime">Datetime</Label>
          <Input
            type="datetime-local"
            name="datetime"
            id="exampleDatetime"
            placeholder="datetime placeholder"
          />
        </FormGroup>
        <FormGroup>
          <Label for="exampleDate">Date</Label>
          <Input
            type="date"
            name="date"
            id="exampleDate"
            placeholder="date placeholder"
          />
        </FormGroup>
        <FormGroup>
          <Label for="exampleTime">Time</Label>
          <Input
            type="time"
            name="time"
            id="exampleTime"
            placeholder="time placeholder"
          />
        </FormGroup>
        <FormGroup>
          <Label for="exampleColor">Color</Label>
          <Input
            type="color"
            name="color"
            id="exampleColor"
            placeholder="color placeholder"
          />
        </FormGroup>
        <FormGroup>
          <Label for="exampleSearch">Search</Label>
          <Input
            type="search"
            name="search"
            id="exampleSearch"
            placeholder="search placeholder"
          />
        </FormGroup>
        <FormGroup>
          <Label for="exampleSelect">Select</Label>
          <Input type="select" name="select" id="exampleSelect">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </Input>
        </FormGroup>
        <!-- <FormGroup>
          <Label for="exampleSelectMulti">Select Multiple</Label>
          <Input type="select" name="selectMulti" id="exampleSelectMulti" multiple>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </Input>
        </FormGroup> -->
        <FormGroup>
          <Label for="exampleText">Text Area</Label>
          <Input type="textarea" name="text" id="exampleText" />
        </FormGroup>
        <FormGroup>
          <Label for="exampleFile">File</Label>
          <Input type="file" name="file" id="exampleFile" />
          <FormText color="muted">
            This is some placeholder block-level help text for the above input. It's a
            bit lighter and easily wraps to a new line.
          </FormText>
        </FormGroup>
        <FormGroup>
          <Input
            id="r1"
            type="radio"
            bind:group={radioGroup}
            value="eenie"
            label="Eenie"
          />
          <Input
            id="r2"
            type="radio"
            bind:group={radioGroup}
            value="meanie"
            label="Meanie"
          />
          <Input
            id="r3"
            type="radio"
            bind:group={radioGroup}
            value="minie"
            label="Minie"
          />
          <Input
            id="r4"
            type="radio"
            bind:group={radioGroup}
            value="moe"
            label="Moe"
          />
        </FormGroup>
        <FormGroup>
          <Input id="c1" type="checkbox" label="Check me out" />
        </FormGroup>
        <FormGroup>
          <Input id="c2" type="checkbox" label="Reverse Label" />
        </FormGroup>
        <FormGroup>
          <Input id="c3" type="switch" label="Switch me on" />
        </FormGroup>
    
        <Button color="primary">Enviar</Button>
      </Form>
    </div>
    
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