import Vue from 'vue';
import Vuex from 'vuex'
// bootstrap 
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// store
import {store} from './store'

//components
import content_pedidos from './components/content.vue'

Vue.use(Vuex);
Vue.use(BootstrapVue);

new Vue({
    el: '#app',
    store: store,
    render(h) { 
      return h(content_pedidos) 
    }
  })