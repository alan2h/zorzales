<template>
          <div class="">   
            <search></search>
            <pedidos_list></pedidos_list>
            <totales></totales>
          </div>
</template>

<script>
import search from './shared/search_pedidos.vue'
import pedidos_list from './shared/pedidos_list.vue'
import totales from './shared/totales.vue'

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
    }
}
</script>

