<script>

  export let month = "Enero";
  export let onClick = null;

</script>

<div class="card" on:click={onClick}>{month}</div>

<style>
  .card {
    width: 100px;
    height: 100px;
    background-color: rgb(233, 222, 222);
    margin: 10px;
    flex: 25%;
    
  }

  .card:hover {
    background-color: rgb(255, 255, 255);
    cursor: pointer;
  }
</style>