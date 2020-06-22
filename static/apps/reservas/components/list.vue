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
              
         </div>


          <div class="title_left">
                <div class="col-md-5 col-sm-10 form-group row pull-right top_search">
             
                  <div class="input-group">
                    <input v-model="texto_buscar" type="text" class="form-control" placeholder="Ingrese la busqueda ...">
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
              <template v-for="reserva in get_reservas">
                <tr :key="reserva.id">
                    <th scope="row">{{ reserva.id }}</th>
                    <template v-if="reserva.fecha_ingreso">
                      <td>{{ reserva.fecha_ingreso|format_date }}</td>
                    </template>
                    <template v-else>
                      <td>--</td>
                    </template>
                    <template v-if="reserva.hora_ingreso">
                    <td>{{ reserva.hora_ingreso }}</td>
                    </template>
                    <template v-else>
                      <td>--</td>
                    </template>
                    <td>{{ reserva.cliente.nombre }} {{ reserva.cliente.apellido }}</td>
                    <td>{{ reserva.cabania.descripcion }}</td>
                    <td> <button @click="abrirCobranza(reserva.id)" class="btn btn-primary"><i class="fa fa-dollar"></i></button> </td>
                    <td> <button class="btn btn-danger"><i class="fa fa-ban"></i></button> </td>
                </tr>
              </template>
            </tbody>
        </table>
        

          <nav aria-label="Page navigation conatiner"></nav>
          <ul class="pagination justify-content-center">
            <template v-if="get_pagina_atras_reservas">
              <li><a @click="siguiente(get_pagina_atras_reservas)" href="#" class="page-link">&laquo; Atrás </a></li>
            </template>
            <template v-if="get_pagina_siguiente_reservas">
              <li><a href="#" @click="atras(get_pagina_siguiente_reservas)" class="page-link"> Siguiente &raquo;</a></li>
            </template>
          </ul>

    </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'
import {format_date, format_} from '@/libs/filters.js'

export default {
    data(){
        return{
          texto_buscar: ''
        }
    },
    methods: {
      ...mapActions(['set_reservas']),
      alta(){
        this.$router.push('/alta');
      },
      siguiente(url){
        this.set_reservas(url)
      },
      atras(url){
        this.set_reservas(url)
      },
      abrirCobranza(reserva_id){
        window.location.href = "/reservas/cobrar/" + reserva_id;
      }
    },
    mounted(){
      this.set_reservas();
    },
    computed: {
      ...mapGetters(['get_reservas', 'get_pagina_siguiente_reservas', 'get_pagina_atras_reservas'])
    },
    filters: {
      format_date
    },
    watch: {
      texto_buscar(value){
        this.set_reservas('/reservas/api/' + '?buscador=' + value)
      }
    }
}
</script>