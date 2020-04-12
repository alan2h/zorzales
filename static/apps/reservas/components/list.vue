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
         <div class="title_left">
                <div class="col-md-10 col-sm-10 form-group row pull-left">
                  <button @click="alta" class="btn btn-success" type="button">Realizar una reserva</button>
                </div>
         </div>


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

        

         <table class="table table-striped">
           
            <thead>
            <tr>
                <th>#</th>
                <th>Fecha de Ingreso</th>
                <th>Fecha de Salida</th>
                <th>Cliente</th>
                <th>Cabaña</th>
            </tr>
            </thead>
            <tbody>
              <template v-for="reserva in get_reservas">
                <tr :key="reserva.id">
                    <th scope="row">{{ reserva.id }}</th>
                    <td>{{ reserva.fecha_ingreso|format_date }}</td>
                    <td>{{ reserva.fecha_salida|format_date }}</td>
                    <td>{{ reserva.cliente.nombre }} {{ reserva.cliente.apellido }}</td>
                    <td>{{ reserva.cabania.descripcion }}</td>
                </tr>
              </template>
            </tbody>
        </table>
    </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'
import {format_date} from '@/libs/filters.js'

export default {
    data(){
        return{

        }
    },
    methods: {
      ...mapActions(['set_reservas']),
      alta(){
        this.$router.push('/alta');
      }
    },
    mounted(){
      this.set_reservas();
    },
    computed: {
      ...mapGetters(['get_reservas'])
    },
    filters: {
      format_date
    }
}
</script>