<script>
  import {
    Form,
    FormGroup,
    Input,
    Badge,
    InputGroupText,
    Button,
  } from "sveltestrap";

  const newUser = () => {
    let new_user_email = document.getElementById("email");
    let new_user_name = document.getElementById("name");

    let new_user = {
      name: new_user_name.value,
      email: new_user_email.value,
    };

    alert(
      `Desde el server ${import.meta.env.BACKEND_URL} El usuario ${
        new_user_name.value
      } se ha registrado con el email ${new_user_email.value}`
    );

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

    alert(
      `El usuario ${new_user_name.value} se ha registrado con el email ${new_user_email.value}`
    );
  };
</script>

<div class="fondo">
  <h1>¿Querés ser parte de Berkut?</h1>
  <div class="border p-3">
    <h2>Date de alta como usuario</h2>
    <Form>
      <FormGroup floating label="Tu email aquí">
        <Input id="email" type="email" placeholder="Ingrese un email" />
      </FormGroup>

      <FormGroup floating>
        <Input id="name" placeholder="Enter a value" />
        <div slot="label">Tu nombre</div>
      </FormGroup>

      <button class="btn btn-warning btn-lg hammer" on:click={newUser}
        ><h1 class="text-warning">¡Quiero!</h1></button
      >
    </Form>
  </div>
</div>

<style>
  .fondo {
    backdrop-filter: blur(5px);
  }

  .hammer {
    width: 299px;
    height: 135px;
    background-image: url(/img/thor.gif);
    border-radius: 15px;
    margin: 20px;
    background-size: 100% 100%;
  }
</style>
