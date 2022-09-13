<script>
  let count = 0

  const increment = () => {
    count += 1
  }

  const reset = () => {
    count = 0
  }

</script>

<button on:click={reset}>Volver a 0</button>

<button on:click={increment}>
  count is {count}
</button>


<style>
  button {
    background: #ff3e00;
    border: none;
    border-radius: 0.9rem;
    color: rgb(35, 255, 54);
    cursor: pointer;
    font-size: 1.25rem;
    font-weight: 700;
    padding: 1.5rem 1rem;
    margin: 1.5rem;
  }
</style>