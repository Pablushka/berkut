<script>
// @ts-nocheck


  // routes imports
  import Router from 'svelte-spa-router';
  import HomePage from './pages/home_page.svelte';
  import HistoryPage from './pages/history_page.svelte';
  import GalleryPage from './pages/gallery_page.svelte';
  import CalendarPage from './pages/calendar_page.svelte';
  import MarketPage from './pages/market_page.svelte';
  import AdminTimelinePage from './pages/admin_timeline_page.svelte';


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
    DropdownToggle,
    ButtonDropdown
  } from 'sveltestrap';
  import MembersPage from './pages/members_page.svelte';

  let isOpen = false;
  let isAdminOpen = false;
  

  // Esta funciion invierte el valor de isOpen
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
    '/members': MembersPage,
    '/gallery': GalleryPage,
    '/calendar': CalendarPage,
    '/market': MarketPage,
    '/admin_timeline': AdminTimelinePage
  };

</script>

<header>
  <Navbar class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <NavbarBrand href="#/" class="me-auto">BERKUT</NavbarBrand>
    <NavbarToggler on:click={toggle} class="me-2" />
    <Collapse {isOpen} navbar expand="md">
      <Nav class="ms-auto" navbar>
        <NavItem>
          <NavLink on:click={toggle} href="#/history">Historia</NavLink>
        </NavItem>
        <NavItem>
          <NavLink on:click={toggle}  href="#/members">Miembros</NavLink>
        </NavItem>
        <NavItem>
          <NavLink on:click={toggle}  href="#/gallery">Galería</NavLink>
        </NavItem>
        <NavItem>
          <NavLink on:click={toggle}  href="#/calendar">Calendario</NavLink>
        </NavItem>
        <NavItem>
          <NavLink on:click={toggle}  href="#/market">Tienda</NavLink>
        </NavItem>

        <NavItem>
          <ButtonDropdown {isAdminOpen}>
            <DropdownToggle color="danger" caret on:click={() => (isAdminOpen = !isAdminOpen)}>
              Administrador
            </DropdownToggle>
            <DropdownMenu>
              <DropdownItem header>Time line</DropdownItem>
              <DropdownItem>
                <a href="#/admin_timeline" class="link">Administrar Timeline</a>
              </DropdownItem>

              <DropdownItem divider />
              <DropdownItem header>Usuarios</DropdownItem>
              <DropdownItem>
                <a href="#/admin_users" class="link">Administrar Usuarios</a>
              </DropdownItem>
              <DropdownItem>
                <a href="#/role_users" class="link">Dar Permisos</a>
              </DropdownItem>

              <DropdownItem divider />
              <DropdownItem disabled>Action (disabled)</DropdownItem>
              <DropdownItem>Foo Action</DropdownItem>
              <DropdownItem>Bar Action</DropdownItem>
              <DropdownItem>Quo Action</DropdownItem>
              <DropdownItem>
                <a href="#/members" class="link">Miembros</a>
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
</style>
