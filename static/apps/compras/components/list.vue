<template>
       <div>
        
          <div class="title_left">

                <div class="col-md-5 col-sm-10 form-group row pull-right top_search">
             
                  <div class="input-group">
                    <input type="text" class="form-control" placeholder="Ingrese la busqueda ...">
                    <span class="input-group-btn">
                      <button class="btn btn-default" type="button">Aceptar</button>
                    </span>
                  </div>
                </div>
                
          </div>

           <div class="form-group">

              <div class="col-md-3 col-sm-3  offset-md-3">
                 <button @click="alta" class="btn btn-dark" type="button"><i class="fa fa-file"></i></button>
                 <button class="btn btn-dark" type="button"><i class="fa fa-print"></i></button>
              </div>

          </div>

         <table class="table table-striped">
           
            <thead>
            <tr>
                <th>#</th>
                <th>Fecha de Ingreso</th>
                <th>Hora de Ingreso</th>
                <th>Cliente</th>
                <th>Cabaña</th>
                <th>Cobrar</th>
                <th>Anular</th>
            </tr>
            </thead>
            <tbody>
             
            </tbody>
        </table>
        

          <nav aria-label="Page navigation conatiner"></nav>
          <ul class="pagination justify-content-center">
          
          </ul>

    </div>
</template>
<script>
export default {
    data(){
        return{

        }
    },
    methods: {
      alta(){
        this.$router.push('/alta')
      }
    }
}
</script>