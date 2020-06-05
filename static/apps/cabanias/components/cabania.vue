<template>
    <div class="col-sm-3" >
        <template v-if="reserva">
            <div class="col-sm-10">
                <h3>Ocupado</h3>
                <h6>{{ cabania.cabania }}</h6>
                <img src="/media/logos/cabania_ocupada.jpeg" width="240px" height="240px" alt="..." class="img-thumbnail">
                <button type="button" class="btn btn-success" data-toggle="modal" data-target="#id_inventory_detail">
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
                <button type="button" class="btn btn-success" data-toggle="modal" data-target="#id_inventory_detail">
                <i class="fa fa-search">Inventario</i></button>
            </div>
        </template>

       <reserva-detail v-if="cabania_open" :cabania="cabania_open"></reserva-detail>
       <inventory-detail></inventory-detail>

    </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'
import reservaDetail from '@/apps/reservas/components/detail.vue'
import inventoryDetail from '@/apps/cabanias/components/inventario_detail.vue'

export default {
    data(){
        return{
            cabania_open: ""
        }
    },
    methods: {
        ...mapActions(['set_reserva_unico']),
        abrirReserva(cabania){
             /* Open detail of reserva */
            this.cabania_open = cabania;
        }
    },
    mounted(){},
    props: {
        cabania: {
            required: true
        },
        reserva: {
            required: false
        }
    },
    components: {
        reservaDetail,
        inventoryDetail
    }
}
</script>