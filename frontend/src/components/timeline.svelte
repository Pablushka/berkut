<script>
  import { onMount, afterUpdate, beforeUpdate } from "svelte";
  

  export let events = [];

  export let caption = 'Historia de Berkut';

  let last_event_ix;

  // console.log('script', events.length -1);
  // console.log('script', $$props);

  onMount(async () => {
    last_event_ix = events.length - 1;
    // console.log("onMount", last_event_ix);
    // console.log('onMount', $$props);
  });

  beforeUpdate(async () => {
    last_event_ix = events.length - 1;
    // console.log("beforeUpodate", last_event_ix);
  });

  afterUpdate(async () => {
    last_event_ix = events.length - 1;
    // console.log("afterUpdate", last_event_ix);
  });


</script>

<h2 class="text-center py-3">{caption}</h2>

    <div class="container py-2 mt-1 mb-1">
        <div class="container py-2 mt-1 mb-1">
          {#each events as { date, title, text }, i}
            <!-- timeline item 1 -->
            <div class="row">
                <!-- timeline item 1 left dot -->
                <div class="col-auto text-center flex-column d-none d-sm-flex">
                    <div class="row h-50">
                      <div class="col {i==0 ? "":"border-end border-primary line"}">&nbsp;</div>
                      <div class="col">&nbsp;</div>
                    </div>
                    <h5 class="m-2">
                        <span class="badge bg-primary border shadow-sm">&nbsp;</span>
                    </h5>
                    <div class="row h-50">
                      <div class="col {i==last_event_ix ? "":"border-end border-primary line"}">&nbsp;</div>
                      <div class="col">&nbsp;</div>
                    </div>
                </div>
                <!-- timeline item 1 event content -->
                <div class="col py-2">
                    <div class="card shadow">
                        <div class="card-body">
                            <div class="float-right text-muted">{date}</div>
                            <h4 class="card-title">{title} {i} {last_event_ix}</h4>
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

    <style>
      .line {
        border-right: 4px solid #0d6efd!important;
      }
    </style>