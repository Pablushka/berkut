<script>
  import Timeline from "../components/timeline.svelte";


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

<h1 class="mt-5">Historia del grupo y coso...</h1>

<Timeline events={my_events} caption="Historia de Berkut" />