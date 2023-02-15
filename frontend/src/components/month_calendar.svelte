<script>
  export let month = "Enero";
  export let onClick = null;
</script>

<div class="mes">
  <h2 class="h5 text-center">{month}</h2>
  <table class="table table-striped text-center" role="presentation">
    <tbody>
      <tr>
        <td aria-hidden="true" class="text-center dias">Dom</td>
        <td aria-hidden="true" class="text-center dias">Lun</td>
        <td aria-hidden="true" class="text-center dias">Mar</td>
        <td aria-hidden="true" class="text-center dias">Mié</td>
        <td aria-hidden="true" class="text-center dias">Jue</td>
        <td aria-hidden="true" class="text-center dias">Vie</td>
        <td aria-hidden="true" class="text-center dias">Sáb</td>
      </tr>
      <tr>
        <td class="today bg-primary">1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
      </tr>
      <tr>
        <td>8</td>
        <td>9</td>
        <td>10</td>
        <td>11</td>
        <td>12</td>
        <td>13</td>
        <td>14</td>
      </tr>
      <tr>
        <td>15</td>
        <td>16</td>
        <td>17</td>
        <td>18</td>
        <td>19</td>
        <td>20</td>
        <td>21</td>
      </tr>
      <tr>
        <td>22</td>
        <td>23</td>
        <td>24</td>
        <td>25</td>
        <td>26</td>
        <td>27</td>
        <td>28</td>
      </tr>
      <tr>
        <td>29</td>
        <td>30</td>
        <td>31</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
      </tr>
      <tr>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
      </tr>
    </tbody>
  </table>
</div>

<style>
  .mes {
    background-color: #f7f6f6a3;
    margin: 15px;
  }
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
