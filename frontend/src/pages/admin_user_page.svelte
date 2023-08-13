<script>
  // @ts-nocheck

  import { onMount } from "svelte";
  import {
    Form,
    Button,
    FormGroup,
    FormText,
    Input,
    Label,
    Modal,
    ModalBody,
    ModalFooter,
    ModalHeader,
  } from "sveltestrap";
  import { bad_words_validator } from "../helpers/admin_helpers.js";

  let bad_words = ["culo", "puto el que lee", "macri", "chupito el pame"];

  let open = false;

  let current_user = null;

  const toggle = () => (open = !open);

  const fill = () => {
    // if (current_user == null) {
    //   let date_parts = new Date().toLocaleDateString().split("/");
    //   let today = date_parts[2] + "-" + date_parts[1] + "-" + date_parts[0];

    //   document.getElementById("field_date").value = today;
    //   return;
    // }

    document.getElementById("field_id").value = current_user.id;
    document.getElementById("field_user").value = current_user.name;
    document.getElementById("field_is_active").value = current_user.is_active;
    document.getElementById("field_is_admin").value = current_user.is_admin;
    document.getElementById("field_level").value = current_user.level;
  };

  const form_fill = (the_user) => {
    toggle();

    current_user = the_user;

    // console.log(current_user);
  };

  // function toggle2() {
  //   open = !open;
  // }

  let radioGroup;
  let my_users = [];
  let modal;

  async function getUsers() {
    let response = await fetch("http://localhost:5000/users");
    let users = await response.json();

    return users;
  }

  onMount(async () => {
    my_users = await getUsers();
  });

  const deleteUser = (id) => {
    let confirmed = confirm(
      "¿Está usted seguro que quiere hacer mierda al usuario?"
    );

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
  };

  const saveUser = () => {
    let id = document.getElementById("field_id").value;
    let name = document.getElementById("field_user").value;
    // let email = document.getElementById("field_email").value;
    // let last_login = document.getElementById("field_last_login").value;
    let is_active = document.getElementById("field_is_active").value;
    let is_admin = document.getElementById("field_is_admin").value;
    let level = document.getElementById("field_level").value;

    let user = {
      id: id,
      name: name,
      is_active: is_active,
      is_admin: is_admin,
      level: level,
    };

    // console.log("user ->", user);

    fetch("http://localhost:5000/users", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(user),
    })
      .then((response) => response.json())
      .then((data) => {
        // console.log("Success:", data);
        getUsers().then((users) => {
          my_users = users;
        });

        toggle();
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  // const editUser = () => {
  //   toggle();

  //   current_user = null;
  // };

  let formLabel = "text-align: left; font-weight: bold;";
</script>

<div class="page-container">
  <h3 class="titulo">Usuarios</h3>
  <table class="table table-striped table-hover">
    <thead>
      <tr class="text">
        <th>Usuario</th>
        <th>Email</th>
        <th>Ultima conexión</th>
        <th>Estado</th>
        <th>Admin</th>
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
          <td style="white-space: nowrap;"
            >{user.is_active == 0 ? "INACTIVO" : "ACTIVO"}</td
          >
          <td style="white-space: nowrap;"
            >{user.is_admin == 0 ? "NO" : "SI"}</td
          >
          <td style="white-space: nowrap;"
            >{user.level == 2 ? "Super" : "Colab"}</td
          >
          <td>
            <button
              on:click={() => form_fill(user)}
              class="btn btn-primary btn-sm btn-berkut boton-uno">Editar</button
            >
          </td>
          <td>
            <button
              class="btn btn-danger btn-sm btn-berkut boton-dos"
              on:click={() => {
                deleteUser(user.id);
              }}>Desactivar</button
            >
          </td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>

<div>
  <Modal on:open={fill} isOpen={open} {toggle} id="event_modal">
    <ModalHeader {toggle}>Usuarios</ModalHeader>
    <ModalBody>
      <Form>
        <input value="" id="field_id" type="hidden" name="id" />

        <FormGroup style={formLabel}>
          <Label for="user">Usuario</Label>
          <Input value="" id="field_user" name="user" readonly />
        </FormGroup>

        <FormGroup style={formLabel}>
          <Label for="status">Estado</Label>
          <Input type="select" value="" id="field_is_active" name="status">
            <option value="false">Inactivo</option>
            <option value="true">Activo</option>
          </Input>
        </FormGroup>

        <FormGroup style={formLabel}>
          <Label for="is_admin">Es Admin?</Label>
          <Input type="select" value="" id="field_is_admin" name="is_admin">
            <option value="false">No</option>
            <option value="true">Si</option>
          </Input>
        </FormGroup>

        <FormGroup style={formLabel}>
          <Label for="level">Nivel</Label>
          <Input type="select" value="" id="field_level" name="level">
            <option value="1">Colaborador</option>
            <option value="2">Super Admin</option>
          </Input>
        </FormGroup>
      </Form>
    </ModalBody>

    <ModalFooter>
      <Button color="primary" on:click={saveUser}>Guardar</Button>
      <Button color="secondary" on:click={toggle}>Cancelar</Button>
    </ModalFooter>
  </Modal>
</div>

<style>
  .page-container {
    background-color: #4d4c4a7d;
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
  .titulo{
    font-size: 65px;
    text-align: center;
    color: aliceblue;
    font-family: monospace;
    text-decoration: underline;
  }

  .text{
        color:#fff
  }

</style>
