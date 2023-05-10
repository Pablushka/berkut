<script>
  // @ts-nocheck

  // routes imports
  import Router from "svelte-spa-router";
  import HomePage from "./pages/home_page.svelte";
  import HistoryPage from "./pages/history_page.svelte";
  import GalleryPage from "./pages/gallery_page.svelte";
  import CalendarPage from "./pages/calendar_page.svelte";
  import MarketPage from "./pages/market_page.svelte";
  import AdminTimelinePage from "./pages/admin_timeline_page.svelte";
  import NewUserPage from "./pages/new_user_page.svelte";
  import NewUserValidationPage from "./pages/new_user_validation_page.svelte";

  // full camelcase: HomePage, UnaLindaVariable
  // camelcase: homePage, unaLindaVariable

  import Timeline from "./components/timeline.svelte";

  import svelteLogo from "./assets/svelte.svg";
  import Counter from "./components/Counter.svelte";

  import {
    Col,
    Container,
    Row,
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
    DropdownToggle,
    ButtonDropdown,
  } from "sveltestrap";
  import MembersPage from "./pages/members_page.svelte";

  let isOpen = false;
  let isAdminOpen = false;

  // Esta funciion invierte el valor de isOpen
  const toggle = () => {
    isOpen = !isOpen;
  };

  const eat = () => {
    alert("I am eating. Sweeeeet!");
  };

  function handleUpdate(event) {
    isOpen = event.detail.isOpen;
  }

  let routes = {
    "/": HomePage,
    "/history": HistoryPage,
    "/members": MembersPage,
    "/gallery": GalleryPage,
    "/calendar": CalendarPage,
    "/market": MarketPage,
    "/admin_timeline": AdminTimelinePage,
    "/new_user": NewUserPage,
    "/new_user_validation/:email": NewUserValidationPage,
  };
</script>

<header>
  <Navbar class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <NavbarBrand href="#/" class="me-auto"
      ><span class="berkut-header">BERKUT</span></NavbarBrand
    >
    <NavbarToggler on:click={toggle} class="me-2" />
    <Collapse {isOpen} navbar expand="md">
      <Nav class="ms-auto" navbar>
        <NavItem>
          <NavLink href="#/"
            ><span class="berkut-sub-header"
              >Recreación Medieval del Este de Europa</span
            ></NavLink
          >
        </NavItem>

        <NavItem>
          <ButtonDropdown {isAdminOpen}>
            <div style="margin-top: 12px;">
              <DropdownToggle
                color="info"
                caret
                on:click={() => (isAdminOpen = !isAdminOpen)}
              >
                MENÚ
              </DropdownToggle>
            </div>
            <DropdownMenu>
              <DropdownItem header class="titular">Time line</DropdownItem>
              <DropdownItem>
                <a href="#/admin_timeline" class="link">Administrar Timeline</a>
              </DropdownItem>

              <DropdownItem divider />
              <DropdownItem header class="titular">Admin</DropdownItem>
              <DropdownItem>
                <a href="#/admin_users" class="link">Administrar Usuarios</a>
              </DropdownItem>
              <DropdownItem>
                <a href="#/role_users" class="link">Dar Permisos</a>
              </DropdownItem>

              <DropdownItem divider />
              <DropdownItem header class="titular">Publico</DropdownItem>
              <DropdownItem>
                <a href="#/new_user" class="link">Crear Usuario</a>
              </DropdownItem>
              <DropdownItem>
                <a href="#/members" class="link">Miembros</a>
              </DropdownItem>
              <DropdownItem>
                <a href="#/history" class="link">Historia</a>
              </DropdownItem>
              <DropdownItem>
                <a href="#/gallery" class="link">Galeria</a>
              </DropdownItem>
              <DropdownItem>
                <a href="#/calendar" class="link">Calendario de Ferias</a>
              </DropdownItem>
              <DropdownItem>
                <a href="#/market" class="link">Shop</a>
              </DropdownItem>
            </DropdownMenu>
          </ButtonDropdown>
        </NavItem>
      </Nav>
    </Collapse>
  </Navbar>
</header>

<main>
  <Router {routes} />
</main>

<style>
  :global(.titular) {
    background-color: #474747;
    margin-left: 10px;
    margin-right: 10px;
    color: #f8f9fa;
    border-radius: 10px;
    text-align: center;
  }

  .link {
    display: block;
    width: 100%;
    clear: both;
    font-weight: 400;
    color: #212529;
    text-align: inherit;
    text-decoration: none;
    white-space: nowrap;
    background-color: transparent;
    border: 0;
  }

  .berkut-header {
    font-family: Viking Hell;
    font-size: 35pt;
  }

  .berkut-sub-header {
    font-family: PR Viking;
    font-size: 25pt;
  }

  :global(.boton-color) {
    background-color: blue-800;
  }
</style>
