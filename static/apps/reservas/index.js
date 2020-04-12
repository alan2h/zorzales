import Vue from 'vue';
import vuex from 'vuex';
import VueRouter from 'vue-router'
// bootstrap 
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

//components
import content_reservas from './components/content.vue'

// store
import reservas from './store'

// rutas
import {routes} from './router'
import {store} from './store'

Vue.use(VueRouter)
Vue.use(vuex);
Vue.use(BootstrapVue);

const router = new VueRouter({
  routes // short for `routes: routes`
})

const storer = new vuex.Store({
  modules: {reservas}
})

new Vue({
    el: '#app',
    router,
    store:storer,
    render(h) { 
      return h(content_reservas) 
    }
  })