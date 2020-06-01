<template>
    <div class="col-sm-3" >
        <template v-if="reserva">
            <div class="col-sm-10">
                <h3>Ocupado</h3>
                <h6>{{ cabania.cabania }}</h6>
                <img src="/media/logos/cabania_ocupada.jpeg" width="240px" height="240px" alt="..." class="img-thumbnail">
                <button class="btn btn-success"><i class="fa fa-search">Inventario</i></button>
                <button class="btn btn-success"><i class="fa fa-search">Cliente</i></button>
            </div>
        </template>
        <template v-else>
            <div class="col-sm-10">
                <h3>Disponible</h3>
                <h6>{{ cabania.cabania }}</h6>
                <img src="/media/logos/cabania_libre.jpeg" width="240px" height="240px" alt="..." class="img-thumbnail">
                <button class="btn btn-success"><i class="fa fa-search">Inventario</i></button>
            </div>
        </template>
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
        ...mapActions(['set_reserva_unico'])
    },
    mounted(){
        console.log(this.cabania)
    },
    props: {
        cabania: {
            required: true
        },
        reserva: {
            required: false
        }
    }
}
</script>