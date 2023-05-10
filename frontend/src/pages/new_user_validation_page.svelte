<script>
  import { Form, FormGroup, Input } from "sveltestrap";

  export let params = {};

  const new_user_email = params.email;

  const validateNewUserToken = () => {
    let token = document.getElementById("token").value;
    let email = document.getElementById("email").value;

    let new_validation = {
      token: token,
      email: email,
    };

    fetch("http://localhost:5000/users/verify", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(new_validation),
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

<div class="fondo2">
  <h1 class="block">¡Valida tu código de acceso!</h1>

  <Form>
    <FormGroup floating label="Tu e-mail aquí" style="display: none;">
      <Input
        id="email"
        type="email"
        placeholder="Ingrese un e-mail"
        value={new_user_email}
        readonly
      />
    </FormGroup>

    <p>
      Querido usurio, por favor revise su correo electrónico y copie el código
      de acceso que le hemos enviado.
    </p>

    <FormGroup floating label="Código de acceso">
      <Input
        id="token"
        name="token"
        type="number"
        pattern="[0-9]+"
        placeholder="Ingrese el código de acceso"
      />
    </FormGroup>

    <button on:click|preventDefault={validateNewUserToken}> Enviar </button>
  </Form>
</div>

<style>
  .fondo2 {
    font-family: PR Viking;
    border: solid 3px;
    background-color: #ffffffa8;
    border-radius: 42px;
    width: 650px;
    padding: 0 50px 20px 50px;
  }
  .block {
    margin-block: revert;
    margin: 10pt;
    text-align: center;
  }
</style>
