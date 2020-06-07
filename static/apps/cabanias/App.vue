<template>
      <div class="x_panel">
        <div class="x_title">
        <h2>Mapa de cabañas .- </h2>
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
            <div class="container">
                <div class="row">
                    <template v-for="cabania in get_reserva_result">
                        <cabania @selected_reserva="selected_reserva" :reserva="cabania.reserva" :key="cabania.id" :cabania="cabania"></cabania>
                    </template>
                </div>
                </div>
        </div>



        <!-- reserva detail -->
            <reserva-detail v-if="reserva_open_detail" :reserva_open_detail="reserva_open_detail"></reserva-detail>
        <!-- reserva detail -->


    </div>
</template>

<script>

import cabania from './components/cabania.vue'
import reservaDetail from '@/apps/reservas/components/detail.vue'

import {mapActions, mapGetters} from 'vuex'


export default {
    data(){
        return{
            reserva_open_detail: ""
        }
    },
    methods: {
        ...mapActions(['set_cabanias', 'set_reserva_unico']),
        selected_reserva(value){
            this.reserva_open_detail = value;
        }
    },
    mounted(){
        this.set_reserva_unico(1);
    },
    components: {
        cabania,
        reservaDetail
    },
    computed: {
        ...mapGetters(['get_cabanias', 'get_reserva_result'])
    }
    
}
</script>