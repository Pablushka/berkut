<script>
  import { Form, FormGroup, Input } from "sveltestrap";

  const newUser = () => {
    let name = document.getElementById("name").value;

    let email = document.getElementById("email").value;

    let new_user = {
      name: name,
      email: email,
    };

    fetch("http://localhost:5000/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(new_user),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
</script>

<div class="border p-3 fondo">
  <h1>¡Date de alta como usuario!</h1>

  <Form>
    <FormGroup floating label="Tu e-mail aquí">
      <Input id="email" type="email" placeholder="Ingrese un e-mail" />
    </FormGroup>

    <FormGroup floating label="Tu nombre aquí">
      <Input id="name" placeholder="Ingrese su nombre" />
    </FormGroup>

    <button on:click={newUser}> Enviar </button>
  </Form>
</div>

<style>
  .fondo {
    backdrop-filter: blur(5px);
    background-color: #29b75f !important;
    border: solid 3px red;
  }
</style>
