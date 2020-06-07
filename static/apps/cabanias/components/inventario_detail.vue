<template>
    <div class="modal fade" id="id_inventory_detail" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Inventario </h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <img src="/media/logos/inventory_cabania.png" width="140px" height="140px" alt="..." class="img-thumbnail">
                <div v-if="get_inventarios_cabania.length == 0" class="alert alert-dark" role="alert">
                        Esta cabaña no contiene un inventario registrado
                </div>
                <table v-if="get_inventarios_cabania.length > 0" class="table">
                <thead>
                    <tr>
                    <th scope="col">Código</th>
                    <th scope="col">Articulo</th>
                    <th scope="col">Cantidad</th>
                    </tr>
                </thead>
                
                <tbody>
                     
                    <template v-for="inventario in get_inventarios_cabania">
                        <tr :key="inventario.id">
                            <th>{{ inventario.articulo.codigo_barra }}</th>
                            <th>{{ inventario.articulo.descripcion }}</th>
                            <td>{{ inventario.cantidad }}</td>
                        </tr>
                    </template>
                </tbody>
                </table>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-times"></i></button>
                <button v-if="get_inventarios_cabania.length > 0" type="button" class="btn btn-primary"><i class="fa fa-print"></i></button>
            </div>
            </div>
        </div>
    </div>
</template>
<script>

import {mapActions, mapGetters} from 'vuex'

export default {
    data(){
        return{

        }
    },
    methods: {
    },
    mounted(){
    },
    filters: {
        
    },
    computed: {
        ...mapGetters(['get_inventarios_cabania'])
    },
    watch: {
    }
}
</script>
