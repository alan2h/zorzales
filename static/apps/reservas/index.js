import Vue from 'vue';
import VueRouter from 'vue-router'

//components
import content_reservas from './components/content.vue'

// rutas
import {routes} from './router'

Vue.use(VueRouter)

const router = new VueRouter({
  routes // short for `routes: routes`
})

new Vue({
    el: '#app',
    router,
    render(h) { 
      return h(content_reservas) 
    }
  })