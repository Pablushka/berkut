<script>
  import Timeline from "../components/timeline.svelte";
	import { onMount } from 'svelte';
  import { ButtonToolbar } from "sveltestrap";

  // let events;
  // fetch from endpoint
  // async function getEvents() {
    
  //   let response = await fetch("http://localhost:5000/events");
  //   let events = await response.json();

  //   return await events;
    
  // }

  let my_events;
  fetch("http://localhost:5000/events").then((response) => response.json()).then((data) => {
      my_events = data;
    });

  
  onMount(async () => {

    console.log("OnMount ha sido ejecutado");
    
  })



</script>

<h1 class="mt-5">Historia del grupo y coso...</h1>
{#await my_events}
<p><img src="https://gifdb.com/images/high/dancing-monkey-action-8omvxbqaq0qqpsgx.gif" alt="Monito bailarin"></p>
{:then events}
  <Timeline events={my_events} caption="Historia de Berkut!" />
{/await}
  
