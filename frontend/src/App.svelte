<script>

  // routes imports
  import Router from 'svelte-spa-router';
  import HomePage from './pages/home_page.svelte';
  import HistoryPage from './pages/history_page.svelte';

  // full camelcase: HomePage, UnaLindaVariable
  // camelcase: homePage, unaLindaVariable

  import Timeline from './components/timeline.svelte';
  
  import svelteLogo from './assets/svelte.svg'
  import Counter from './components/Counter.svelte'
  import golum from './assets/golumbrandt.png'

  import {
    Col, Container, Row,
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    Dropdown,
    DropdownItem,
    DropdownMenu,
    DropdownToggle
  } from 'sveltestrap';

  let isOpen = false;

  const toggle = () => {
    isOpen = !isOpen;
  }

  const eat = () => {
    alert('I am eating. Sweeeeet!')
  }

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }

  let routes = {
    '/': HomePage,
    '/history': HistoryPage,
  };
  
  let my_events = [
    {
      datetime: '9 de dic de 1989', 
      title: 'Fundación de Berkut', 
      text: 'Fundación de Berkut en la ciudad de Bogotá, Colombia.'
    },

    {
      datetime: '25 de enero de 2007', 
      title: 'Primer campamento con cero muertos', 
      text: 'Todo un hito porque nadie salio herido!'
    },

    {
      datetime: '1 de marzo de 2020', 
      title: 'Ultimo campamento', 
      text: 'Realizado en la ciudad de Kyoto con los chicos del fan clu de anime.'
    },

  ];

</script>

<header>
  <Navbar class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <NavbarBrand href="/" class="me-auto">BERKUT</NavbarBrand>
    <NavbarToggler on:click={toggle} class="me-2" />
    <Collapse {isOpen} navbar expand="md">
      <Nav class="ms-auto" navbar>
        <NavItem>
          <NavLink href="#/history">Historia</NavLink>
        </NavItem>
        <NavItem>
          <NavLink href="">Miembros</NavLink>
        </NavItem>
        <NavItem>
          <NavLink href="">Galería</NavLink>
        </NavItem>
        <NavItem>
          <NavLink href="">Calendario</NavLink>
        </NavItem>
        <NavItem>
          <NavLink href="">Tienda</NavLink>
        </NavItem>
      </Nav>
    </Collapse>
  </Navbar>

</header>

<main>

  <Container>
    <Row>
      <Col sm="3" style="border: 1px solid">
        Nada aqui
      </Col>
      <Col>
        <Router {routes} />
      </Col>
    </Row>
  </Container>

  <Timeline events={my_events}/>

  <Timeline caption="Hola manola!"/>

</main>


<!-- <main >

  <div class="container">
    <h1 class="mt-5">Bienvenidos a Berkut</h1>
    <p class="lead">Pin a footer to the bottom of the viewport in desktop browsers with this custom HTML and CSS. A fixed navbar has been added with <code class="small">padding-top: 60px;</code> on the <code class="small">main &gt; .container</code>.</p>
    <p>Back to <a href="/docs/5.0/examples/sticky-footer/">the default sticky footer</a> minus the navbar.</p>
  </div>
 
  <img on:click={eat} src={golum} alt="">

  <div>
    <a href="https://vitejs.dev" target="_blank"> 
      <img src="/vite.svg" class="logo" alt="Vite Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank"> 
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>Vite + Svelte</h1>

  <div class="card">
    <Counter />
  </div>

  <p>
    Check out <a href="https://github.com/sveltejs/kit#readme" target="_blank">SvelteKit</a>, the official Svelte app framework powered by Vite!
  </p>

  <p class="read-the-docs">
    Click on the Vite and Svelte logos to learn more
  </p>
</main> -->

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }

  .background-header {
    background-color: #000;
  }
</style>
