<template>
          <div class="">  
            <div :class="'alert alert-' + get_message.status" role="alert">
                {{ get_message.text }}
            </div> 
            <search></search>
            <pedidos_list></pedidos_list>
            <totales></totales>
          </div>
</template>

<script>
import search from './shared/search_pedidos.vue'
import pedidos_list from './shared/pedidos_list.vue'
import totales from './shared/totales.vue'

import {mapGetters} from 'vuex'

export default {
    name: 'content_pedidos',
    data(){
        return{

        }
    },
    methods: {
      
    },
    components: {
        search,
        pedidos_list,
        totales
    },
    computed: mapGetters(['get_message'])
}
</script>

