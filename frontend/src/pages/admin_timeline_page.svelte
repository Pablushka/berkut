<script>
// @ts-nocheck

  import { onMount } from 'svelte';
  import { Form, Button, FormGroup, FormText, Input, Label, Modal, ModalBody, ModalFooter, ModalHeader } from 'sveltestrap';


  let open = false;

  let current_event = null;
  
  const toggle = () => (open = !open);
  
  const fill = () => {
    
    if (current_event == null) {
      
      let date_parts = (new Date()).toLocaleDateString().split('/')
      let today = date_parts[2] + '-' + date_parts[1] + '-' + date_parts[0];

      document.getElementById("field_date").value = today;
      return;
    }

    let components = current_event.date.split("-");
    
    // convierto la fecha a YYYY-MM-DD por requerimiento de chrome
    let new_date = `${components[2]}-${components[1]}-${components[0]}`;

    document.getElementById("field_date").value = new_date;
    document.getElementById("field_id").value = current_event.id;
    document.getElementById("field_title").value = current_event.title;
    document.getElementById("field_text").value = current_event.text;
  }

  const form_fill = (the_event) => {

    toggle();

    current_event = the_event;
  };
    

  // function toggle2() {
  //   open = !open;
  // }

  let radioGroup;
  let my_events=[];
  let modal;

  async function getEvents() {

    let response = await fetch("http://localhost:5000/events");
    let events = await response.json();
  
    return events;

  }

  onMount(async () => {
    my_events = await getEvents();
    const modal = new bootstrap.Modal('#exampleModal');
    modal.show();
    // console.log(my_events);
  })

  const deleteEvent = (id) => {

    let confirmed = confirm("¿Está usted seguro que quiere hacer mierda el evento?");

    if (!confirmed) {
      return;
    }

    fetch(`http://localhost:5000/events/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      getEvents().then((events) => {
        my_events = events;
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });

  }

  const saveEvent = () => {

    let id = document.getElementById("field_id").value;
    let date = document.getElementById("field_date").value;
    let title = document.getElementById("field_title").value;
    let text = document.getElementById("field_text").value;

    let components = date.split("-");

    // convierto la fecha a DD-MM-YYYY por requerimiento de la API
    let new_date = `${components[2]}-${components[1]}-${components[0]}`;

    let event = {
      id: id,
      date: new_date,
      title: title,
      text: text,
    };

    let httpMethod = id == '' ? "POST" : "PATCH";

    fetch("http://localhost:5000/events", {
      method: httpMethod,
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(event),
    })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      getEvents().then((events) => {
        my_events = events;
      });

      toggle();

    })
    .catch((error) => {
      console.error("Error:", error);
    });

  }

  const newEvent = () => {
    toggle();

    current_event = null;

  }

  let formLabel = "text-align: left; font-weight: bold;";

</script>

<div class="page-container">
  <h3>Eventos</h3>
  <table class="table table-striped table-hover">
    <thead>
      <tr>
        <th>Fecha</th>
        <th>Titulo</th>
        <th>Texto</th>
        <th colspan="2">Acciones</th>
      </tr>
    </thead>
    <tbody>
      {#each my_events as event}
      <tr>
        <td style="white-space: nowrap;">{event.date}</td>
        <td style="white-space: nowrap;">{event.title}</td>
        <td>{event.text}</td>
        <td>
          <button on:click={()=>form_fill(event)} class="btn btn-primary btn-sm btn-berkut">Editar</button>
        </td>
        <td>
          <button class="btn btn-danger btn-sm btn-berkut" on:click={()=>{deleteEvent(event.id)}}>Eliminar</button>
        </td>
      </tr>
      {/each}

    </tbody>

  </table>

  <div>
    

    <Modal on:open={fill} isOpen={open} {toggle} id="event_modal">
      <ModalHeader {toggle}>Evento</ModalHeader>
      <ModalBody>
        <Form>
          
            <input value="" 
            id="field_id" 
            type="hidden"
            name="id"/>

          <FormGroup style={formLabel}>
            <Label for="date">Fecha</Label>
            <Input
              type="date"
              name="date"
              id="field_date"
              placeholder="date placeholder"
            />
          </FormGroup>

          <FormGroup style={formLabel}>
            <Label for="title">Título</Label>
            <Input value="" 
            id="field_title" 
            name="title"/>
          </FormGroup>

          <FormGroup style={formLabel}>
            <Label for="text">Texto</Label>
            <Input type="textarea" 
            name="text" 
            id="field_text"/>
          </FormGroup>

        </Form>

      </ModalBody>

      <ModalFooter>
        <Button color="primary" on:click={saveEvent}>Guardar</Button>
        <Button color="secondary" on:click={toggle}>Cancelar</Button>
      </ModalFooter>

    </Modal>

  </div>




<!-- Button trigger modal -->
<button type="button" on:click={newEvent} class="btn btn-primary">
  Nuevo Evento
</button>




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