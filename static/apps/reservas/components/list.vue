<template>
     <div>
         <!--
                fecha_ingreso 
                hora_ingreso 
                fecha_salida 
                hora_salida 
                cliente 
                alquiler
                observacion
        -->
          <div class="title_right">
                <div class="col-md-5 col-sm-10   form-group row pull-right top_search">
                <div class="input-group">
                    <select class="form-control">
                        <option>Estados</option>
                        <option>Fecha Reserva</option>
                        <option>Alquiler</option>
                        <option>Cliente</option>
                    </select>
                </div>
                  <div class="input-group">
                    <input type="text" class="form-control" placeholder="Ingrese la busqueda ...">
                    <span class="input-group-btn">
                      <button class="btn btn-default" type="button">Aceptar</button>
                    </span>
                  </div>
                </div>
              </div>

         <table class="table table-striped">
            <thead>
            <tr>
                <th>#</th>
                <th>Fecha de Ingreso</th>
                <th>Fecha de Salida</th>
                <th>Cliente</th>
                <th>Alquiler</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
                <td>@mdo</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    data(){
        return{

        }
    }
}
</script>