<script>
  import { CardTitle } from "sveltestrap";

  export let events = [
      {
        datetime: '9 de dic de 1989', 
        title: 'Fundación de Berkut', 
        text: 'Fundación de Berkut en la ciudad de Bogotá, Colombia.'
      }
    ];

  export let caption = 'Historia de Berkut';

  let last_event_ix = events.length - 1;



</script>

<h2 class="text-center py-3">{caption}</h2>

    <div class="container py-2 mt-1 mb-1">
        <div class="container py-2 mt-1 mb-1">

          {#each events as { datetime, title, text }, i}
            <!-- timeline item 1 -->
            <div class="row">
                <!-- timeline item 1 left dot -->
                <div class="col-auto text-center flex-column d-none d-sm-flex">
                    <div class="row h-50">
                      {#if i == 0}
                        <div class="col">&nbsp;</div>
                      {:else}
                        <div class="col border-end border-primary">&nbsp;</div>
                      {/if}
                        <div class="col">&nbsp;</div>
                    </div>
                    <h5 class="m-2">
                        <span class="badge bg-primary border shadow-sm">&nbsp;</span>
                    </h5>
                    <div class="row h-50">
                      {#if i == last_event_ix}
                        <div class="col">&nbsp;</div>
                      {:else}
                        <div class="col border-end border-primary">&nbsp;</div>
                      {/if}
                        <div class="col">&nbsp;</div>
                    </div>
                </div>
                <!-- timeline item 1 event content -->
                <div class="col py-2">
                    <div class="card shadow">
                        <div class="card-body">
                            <div class="float-right text-muted">{datetime}</div>
                            <h4 class="card-title">{title}</h4>
                            <p class="card-text">{text}</p>
                        </div>
                    </div>
                </div>
            </div>
            <!--/row-->
          {/each}

        </div>
        <!--container-->
    </div>