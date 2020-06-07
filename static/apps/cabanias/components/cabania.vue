<template>
    <div class="col-sm-3" >
        <template v-if="reserva">
            <div class="col-sm-10">
                <h3>Ocupado</h3>
                <h6>{{ cabania.cabania }}</h6>
                <img src="/media/logos/cabania_ocupada.jpeg" width="240px" height="240px" alt="..." class="img-thumbnail">
                <button @click="abrirInventario(cabania.cabania_id)"  type="button" class="btn btn-success" data-toggle="modal" data-target="#id_inventory_detail">
                <i class="fa fa-search">Inventario</i></button>
                <!-- Button trigger modal -->
                <button @click="abrirReserva(cabania)" type="button" class="btn btn-success" data-toggle="modal" data-target="#id_cliente_detail">
                <i class="fa fa-search">Ver reserva</i></button>
                 
            </div>
        </template>
        <template v-else>
            <div class="col-sm-10"> 
                <h3>Disponible</h3>
                <h6>{{ cabania.cabania }}</h6>
                <img src="/media/logos/cabania_libre.jpeg" width="240px" height="240px" alt="..." class="img-thumbnail">
                <button @click="abrirInventario(cabania.cabania_id)" type="button" class="btn btn-success" data-toggle="modal" data-target="#id_inventory_detail">
                <i class="fa fa-search">Inventario</i></button>
            </div>
        </template>

       

       <inventory-detail></inventory-detail>

    </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'
import inventoryDetail from '@/apps/cabanias/components/inventario_detail.vue'



export default {
    data(){
        return{
            
        }
    },
    methods: {
        ...mapActions(['set_reserva_unico', 'set_inventarios_cabania']),
        abrirReserva(cabania){
            console.log(cabania, '=============')
             /* Open detail of reserva */
            this.$emit('selected_reserva',cabania)
            //this.$forceUpdate()
        },
        abrirInventario(cabania_id){
            this.set_inventarios_cabania(cabania_id);
        }
    },
    mounted(){
        console.log(this.cabania);
    },
    props: {
        cabania: {
            required: true
        },
        reserva: {
            required: false
        }
    },
    components: {
        inventoryDetail
    }
}
</script>