<template>
          <div class="">   
            <search></search>
            <pedidos_list></pedidos_list>
          </div>
</template>

<script>
import search from './search_pedidos.vue'
import pedidos_list from './pedidos_list.vue'

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
        pedidos_list
    }
}
</script>

