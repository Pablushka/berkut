<script>
  import Timeline from "../components/timeline.svelte";
	import { onMount } from 'svelte';

  let my_events
  
  // fetch from endpoint
  async function getEvents() {

    let response = await fetch("http://localhost:5000/events");
    let events = await response.json();
    return events;

  }

  onMount(async () => {
    my_events = await getEvents()
  })



</script>

<h1 class="mt-5">Historia del grupo y coso...</h1>

<Timeline events={my_events} caption="Historia de Berkut" />