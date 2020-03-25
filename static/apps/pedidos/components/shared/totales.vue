<template>
     <div class="x_panel">
        <div class="x_title">
        <h2>Precio Total .- </h2>
        <ul class="nav navbar-right panel_toolbox">
            <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
            </li>
            <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><i class="fa fa-wrench"></i></a>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                
            </div>
            </li>
            <li><a class="close-link"><i class="fa fa-close"></i></a>
            </li>
        </ul>
        <div class="clearfix"></div>
        </div>
        <div class="x_content">
        <br />
            
             <div class="form-group row">
                <label class="control-label col-md-3" for="first-name">Total a pagar <span class="required">*</span>
                </label>
                <div class="col-md-7">
                    <input v-model="total" type="text" required="required" class="form-control col-md-12 ">
                </div>
            </div>

            <div class="ln_solid"></div>
            <div class="form-group">
              <div class="col-md-9 col-sm-9  offset-md-3">
                <a  href="#" type="button" class="btn btn-primary">Cancelar</a>
                <button @click="guardar" type="button" class="btn btn-success">Guardar</button>
              </div>
            </div>

        </div>
    </div>
</template>

<script>

import {mapGetters, mapActions} from 'vuex'
import {config} from '../../../../libs/globals_conf.js'
import axios from 'axios'

export default {
    data(){
        return{
            total: 0.0
        }
    },
    methods: {
        ...mapActions(['delete_pedidos_articulos_all', 'set_message']),
        /*
            {
                "fecha": null,
                "precio_compra": null,
                "observacion": "",
                "baja": false,
                "fecha_baja": null,
                "articulos": []
            }
        */
       guardar(){
           
           let fecha = this.get_fecha
           let precio_compra = this.get_total
           let articulos = []
            for (var x=0; x < this.get_articulos_pedidos.length; x++){
                articulos.push(this.get_articulos_pedidos[x].id)
            }
            let pedido = {
               fecha: fecha,
               precio_compra: precio_compra,
               articulos: articulos
            }

              axios.post('/pedidos/api/', pedido, config)
                .then((response)  => {
                   console.log(response)
                   this.delete_pedidos_articulos_all();
                   this.set_message({'status': 'success', 'text':'el pedido se guardo correctamente'})
                })
                .catch((error) => {
                   console.log(error)
                   this.set_message({'status':'error', 'text': 'Faltan datos'})
                });
        }
    },
    computed:{
        ...mapGetters(['get_total', 'get_fecha', 'get_articulos_pedidos']),
        
    },
    watch: {
        get_total(value){
            this.total = value;
        }
    }
}
</script>