<script>
  import berkut_logo from "../assets/img/berkut_logo_fa.jpg";
  import vite_logo from "../../public/vite.svg";

  import { getCookie, setCookie } from "../helpers/cookies";

  let user_name = "";

  // fetch("http://localhost:5000/set/user/pablushka", {
  //   credentials: "include",
  // })
  //   .then((response) => response.json())
  //   .then((data) => {
  //     console.log("Success:", data);
  //   });

  let user = getCookie("berkut_session.user");
  if (user) {
    user = JSON.parse(user);
    user_name = user.name ?? "";
  } else {
    user_name = "";
  }
</script>

<div class="welcome_text">
  <h1>Bienvenido {user_name}</h1>

  <p class="titel_text">
    Berkut es un grupo argentino, sin fines de lucro, de recreación histórica
    que busca encarnar el estilo de vida de la población del este de Europa,
    abarcando los siglos IX al XIII. En nuestro campamento podrán disfrutar de
    la inmersión de los miembros del grupo en sus roles, llevando al espectador
    por un recorrido de las áreas comunes de un campamento. Pudiendo apreciar la
    cocina donde se prepara pan sin levadura y la comida para alimentar al
    grupo. Comida que será consumida en el comedor principal junto con un buen
    hidromiel. Siguiendo el recorrido podremos ver una típica habitación con
    cama, arcones, alfombras y ropas típicas exhibidas. Pasaremos por el sector
    de armas, donde podrán apreciar el peso del armamento, escudos y armaduras.
    Los miembros del grupo estarán disponibles para contestar cualquier duda y
    realizar combates de exhibición para su disfrute. El espectador podrá
    participar de nuestro juego de lanzas, formar parte del muro de escudos y la
    venta de esclavos. Terminando el recorrido con el salón del trono, en el
    cual el espectador podrá ser parte de la historia usando las vestimentas de
    la época y así retratarse en foto esperando se lleven un lindo recuerdo de
    lo que es Berkut.
  </p>
</div>

<style>
  .titel_text {
    font-family: PR Viking;
    font-size: 20pt;
    text-align: center;
  }

  .welcome_text {
    font-family: PR Viking;
    background-color: #bbb0b163;
    color: #000000;
    padding-left: 84px;
    margin: 50px;
    padding-right: 84px;
    border-radius: 95px;
    padding-bottom: 13px;
    padding-top: 13px;
  }
</style>
