<template>
            
            <div class="row">
              <div class="col-md-12 col-sm-12 ">
                <div class="x_panel">
                  <div class="x_title">
                    <h2>Realizar una reserva</h2>
                    <ul class="nav navbar-right panel_toolbox">
                      <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                      </li>
                      <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-wrench"></i></a>
                       
                      </li>
                      <li><a class="close-link"><i class="fa fa-close"></i></a>
                      </li>
                    </ul>
                    <div class="clearfix"></div>
                  </div>
                  <div class="x_content">
                    <br />
                    <form id="demo-form2" data-parsley-validate class="form-horizontal form-label-left">
                            
                            <!-- controles -->
                              <div class="item form-group">
                                  <label class="col-form-label col-md-3 col-sm-3 label-align" >Cabañas <span class="required">*</span>
                                  </label>
                                  <div class="col-md-6 col-sm-6 ">
                                    <select v-model="reserva.cabania" class="form-control">
                                      <template v-for="cabania in get_cabanias">
                                        <option :key="cabania.id" :value="cabania.id">{{ cabania.descripcion }}</option>
                                      </template>
                                    </select>
                                  </div>
                              </div>
                            <!-- controles -->

                             <!-- controles -->
                              <div class="item form-group">
                                  <label class="col-form-label col-md-3 col-sm-3 label-align" >Clientes <span class="required">*</span>
                                  </label>
                                  <div class="col-md-6 col-sm-6 ">
                                    <input v-model="cliente_datos" class="form-control" disabled>
                                  </div>
                                  <b-button v-b-modal.modalPopover>Buscar cliente</b-button>
                              </div>
                            <!-- controles -->

                             <!-- controles -->
                              <div class="item form-group">
                                  <label class="col-form-label col-md-3 col-sm-3 label-align" >Fecha de ingreso <span class="required">*</span>
                                  </label>
                                  <div class="col-md-6 col-sm-6 ">
                                    <date-picker @change="formato_fecha_ingreso" format="DD/MM/YYYY" v-model="fecha_ingreso" :lang="lang" type="date"></date-picker>
                                  </div>
                              </div>
                            <!-- controles -->

                            <!-- controles -->
                              <div class="item form-group">
                                  <label class="col-form-label col-md-3 col-sm-3 label-align" >Hora de ingreso 
                                  </label>
                                  <div class="col-md-6 col-sm-6 ">
                                    <date-picker v-model="reserva.hora_ingreso" :lang="lang" type="time"></date-picker>
                                  </div>
                              </div>
                            <!-- controles -->

                             <!-- controles -->
                              <div class="item form-group">
                                  <label class="col-form-label col-md-3 col-sm-3 label-align" >Fecha de salida 
                                  </label>
                                  <div class="col-md-6 col-sm-6 ">
                                    <date-picker format="DD/MM/YYYY" v-model="reserva.fecha_salida" :lang="lang" type="date"></date-picker>
                                  </div>
                              </div>
                            <!-- controles -->

                            <!-- controles -->
                              <div class="item form-group">
                                  <label class="col-form-label col-md-3 col-sm-3 label-align" >Hora de salida 
                                  </label>
                                  <div class="col-md-6 col-sm-6 ">
                                    <date-picker v-model="reserva.hora_salida" :lang="lang" type="time"></date-picker>
                                  </div>
                              </div>
                            <!-- controles -->

                             <!-- controles -->
                              <div class="item form-group">
                                  <label class="col-form-label col-md-3 col-sm-3 label-align" >Observación 
                                  </label>
                                  <div class="col-md-6 col-sm-6 ">
                                    <textarea v-model="reserva.observacion" class="form-control"></textarea>
                                  </div>
                              </div>
                            <!-- controles -->
                            
                            <!-- botones -->
                              <div class="ln_solid"></div>
                              <div class="item form-group">
                                  <div class="col-md-6 col-sm-6 offset-md-3">
                                  <button class="btn btn-primary" type="button">Cancelar</button>
                                  <button type="submit" class="btn btn-success">Guardar</button>
                                  </div>
                              </div>
                             <!-- botones -->

                    </form>
                  </div>
                </div>
              </div>
              <clientes_list @selected="select"></clientes_list>
            </div>

</template>

<script>
/*
{
  "cabania": {
    "inventario": [
      {
        "cantidad": -2147483648,
        "articulo": 0
      }
    ],
    "descripcion": "string",
    "precio": "string",
    "habitacion": -2147483648,
    "estado": "DISPONIBLE"
  },
  "cliente": {
    "nombre": "string",
    "apellido": "string",
    "fecha_nacimiento": "2020-04-12",
    "email": "string",
    "telefono": "string",
    "motivo": "string",
    "observacion": "string",
    "baja": true,
    "fecha_baja": "2020-04-12"
  },
  "fecha_ingreso": "2020-04-12",
  "hora_ingreso": "string",
  "fecha_salida": "2020-04-12",
  "hora_salida": "string",
  "observacion": "string"
}
*/


import {mapActions, mapGetters} from 'vuex'

import clientes_list from './clientes_list.vue'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';

import {lang} from '@/libs/globals_conf.js'
import {pad} from '@/libs/functions.js'

export default {
    data(){
        return{
            cliente_datos: '',
            lang: lang,
            fecha_ingreso: null,
            reserva: {
              cabania: '',
              cliente: '',
              fecha_ingreso: null,
              hora_ingreso: null,
              fecha_salida: null,
              hora_salida: null,
              observacion: ''
            }
        }
    },
    methods: {
      ...mapActions(['set_cabanias']),
      select(cliente){

        this.cliente_datos = cliente.nombre + ' ' + cliente.apellido;
        if (cliente.numero_documento){
          this.cliente_datos += ' ' + cliente.numero_documento
        }
        this.reserva.cliente = cliente.id;
      },
      formato_fecha_ingreso(){
        this.reserva.fecha_ingreso = pad(this.fecha_ingreso.getFullYear()) + '-' + pad(this.fecha_ingreso.getMonth() + 1) + '-' + pad(this.fecha_ingreso.getDate());
        console.log(this.reserva);
        
      }
    },
    mounted(){
      this.set_cabanias();
    },
    computed: { 
      ...mapGetters(['get_cabanias'])
    },
    components: {
      clientes_list,
      DatePicker
    }
}
</script>