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
  import { getCookie, setCookie } from "./helpers/cookies";
  import AdminUserPage from "./pages/admin_user_page.svelte";
  import { push, pop, replace } from "svelte-spa-router";

  // full camelcase: HomePage, UnaLindaVariable
  // camelcase: homePage, unaLindaVariable

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
    Button,
  } from "sveltestrap";
  import MembersPage from "./pages/members_page.svelte";
  import FmDelSur from "./pages/photo_page.svelte";

  let isOpen = false;
  let isAdminOpen = false;

  // Esta funciion invierte el valor de isOpen
  const toggle = () => {
    isOpen = !isOpen;
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
    "/new_user_validation/:email?": NewUserValidationPage,
    "/admin_users": AdminUserPage,
    "/fm_del_sur": FmDelSur,
  };

  let cookie_user = JSON.parse(getCookie("berkut_session.user"));

  // user = false;
  const LogOut = () => {
    document.cookie =
      "berkut_session.user=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

    // replace("/")
    window.location = "/";
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
              {#if cookie_user}
                <DropdownItem header class="titular">Time line</DropdownItem>
                <DropdownItem>
                  <a href="#/admin_timeline" class="link">Administrar Eventos</a
                  >
                </DropdownItem>

                <DropdownItem divider />
                <DropdownItem header class="titular">Administrador</DropdownItem
                >
                <DropdownItem>
                  <a href="#/admin_users" class="link">Administrar Usuarios</a>
                </DropdownItem>
                <DropdownItem>
                  <a href="#/post_edit" class="link">Editar posts</a>
                </DropdownItem>

                <DropdownItem divider />
              {/if}

              <DropdownItem header class="titular">Publico</DropdownItem>
              {#if cookie_user == null}
                <DropdownItem>
                  <a href="#/new_user" class="link">Crear Usuario</a>
                </DropdownItem>
                <DropdownItem>
                  <a href="#/new_user_validation" class="link">Log In Usuario</a
                  >
                </DropdownItem>
              {/if}
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
              {#if cookie_user}
                <Button header class="titular-dos" on:click={LogOut}
                  >Log Out</Button
                >
              {/if}
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

  :global(.titular-dos) {
    background-color: #a01b1b;
    margin-left: 50px;
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
