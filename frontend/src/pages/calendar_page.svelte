<script>
import MonthCalendar from '../components/month_calendar.svelte'

const monthClick = (e) => {
  console.log(e)
  console.log("Uste hizo click en " + e.target.month)
}

</script>


<h1 class="mt-5"><span class="months_titel"> Calendario de Ferias </span></h1>

<div class="months">
  <MonthCalendar month="Enero" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Febrero" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Marzo" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Abril" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="MAyonesa" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Junio" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Julia" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Agosto" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Septiembre" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Obtubre" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Noviembre" onClick={monthClick}></MonthCalendar>
  <MonthCalendar month="Diciembre" onClick={monthClick}></MonthCalendar>
</div>



<style>

@font-face {
    font-family: PR Viking;
    src: url('fonts/PR_Viking.ttf');
  }

  .months {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
  }

  .months_titel{
    font-family: PR Viking;
    font-size: 50pt;
    text-align: center;
  }
</style>