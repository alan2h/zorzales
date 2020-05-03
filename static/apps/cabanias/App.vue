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
                    <template v-for="cabania in get_cabanias">
                        <cabania :key="cabania.id" :cabania="cabania"></cabania>
                    </template>
                </div>
                </div>
        </div>
    </div>
</template>

<script>

import cabania from './components/cabania.vue'

import {mapActions, mapGetters} from 'vuex'

export default {
    data(){
        return{
            
        }
    },
    methods: {
        ...mapActions(['set_cabanias'])
    },
    mounted(){
        this.set_cabanias();
    },
    components: {
        cabania
    },
    computed: {
        ...mapGetters(['get_cabanias'])
    }
}
</script>