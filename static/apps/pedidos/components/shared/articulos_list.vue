<template>
    <div>
        <b-button  v-b-modal.modal-1><i class="fa fa-search"></i></b-button>
        <b-modal size="lg" id="modal-1" title="Lista de Artículos" >
            <div class="col-md-7">
                <input @keypress="buscar"  v-model="search" placeholder="ingrese la busqueda del artículo" type="text"  required="required" class="form-control col-md-12 ">
            </div>
            
            <table class="table table-striped">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Descripción</th>
                        <th>Marca</th>
                        <th>Rubro</th>
                        <th>Precio Compra</th>
                        <th>Precio Venta</th>
                        <th>Stock</th>
                    </tr>
                    </thead>
                    <tbody>
                        
                    <tr v-for="articulo in get_articulos" :key="articulo.id" @click="seleccionar(articulo)">
                        <th scope="row" v-text="articulo.id" ></th>
                        <td v-text="articulo.descripcion"> </td>
                        <template v-if="articulo.marca">
                            <td v-text="articulo.marca.descripcion"> </td>
                        </template>
                        <template v-else>
                            <td> -- </td>
                        </template>
                        <template v-if="articulo.rubro">
                            <td v-text="articulo.rubro.descripcion"> </td>
                        </template>
                         <template v-else>
                            <td> -- </td>
                        </template>
                        <td v-text="'$' + articulo.precio_compra" ></td>
                        <td v-text="'$' + articulo.precio_venta" ></td>
                        <td v-text="articulo.stock" ></td>
                    </tr>
                    </tbody>
                </table>
                <div v-if="get_articulos.length == 0" class="alert alert-danger" role="alert">
                            No existen registro
                        </div>
                    <template v-slot:modal-footer>
                        <nav aria-label="Page navigation example">
                            <ul class="pagination justify-content-end">
                                <li v-if="get_pagina_atras"  class="page-item">
                                    <a class="page-link" @click="atras(get_pagina_atras)" href="#" tabindex="-1">Atrás</a>
                                </li>
                                <li v-if="get_pagina_siguiente" class="page-item">
                                <a class="page-link" @click="siguiente(get_pagina_siguiente)"  href="#">Siguiente</a>
                                </li>
                            </ul>
                        </nav>
                        <div class="w-100">
                        <p class="float-left"></p>
                        <b-button
                            variant="primary"
                            size="sm"
                            class="float-right"
                            @click="hideModal">
                        Cerrar
                        </b-button>
                    </div>
                </template>
        </b-modal>
    </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex';

export default {
    data(){
        return{
            search : ''
        }
    },
    methods: {
          ...mapActions(['set_articulos', 'set_pedidos_articulos', 'set_total']),
          hideModal() {
            this.$root.$emit('bv::hide::modal', 'modal-1', '#btnShow')
            },
            siguiente(url){
                this.set_articulos(url);
            },
            atras(url){
                this.set_articulos(url);
            },
            buscar(){
                this.set_articulos('/articulos/api/?search=' + this.search);
            },
            seleccionar(articulo){
                var cantidad = prompt("Ingrese la cantidad", "1");
                articulo['cantidad'] = cantidad;
                var total = 0.0;
                if (articulo['precio_compra']){
                    total = parseFloat(articulo['precio_compra']) * parseFloat(cantidad);
                }
                articulo['total'] = total;
                this.set_total(total);
                this.set_pedidos_articulos(articulo);
            }
    },
     mounted(){
        this.set_articulos('/articulos/api');
    },
    computed:{
        ...mapGetters(['get_articulos', 'get_pagina_siguiente', 'get_pagina_atras']),
    }
}
</script>