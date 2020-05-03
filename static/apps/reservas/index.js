import Vue from 'vue';
import vuex from 'vuex';
import VueRouter from 'vue-router'
// bootstrap 
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';


//components
import content_reservas from './components/content.vue'

// store
import reservas from './store'
import cabanias from '@/apps/cabanias/store'
import clientes from '@/apps/clientes/store'

// rutas
import {routes} from './router'

Vue.use(VueRouter)
Vue.use(vuex);
Vue.use(BootstrapVue);
Vue.use(VueSweetalert2);

const router = new VueRouter({
  routes // short for `routes: routes`
})

const storer = new vuex.Store({
  modules: {reservas, clientes, cabanias}
})

new Vue({
    el: '#app',
    router,
    store:storer,
    render(h) { 
      return h(content_reservas) 
    }
  })