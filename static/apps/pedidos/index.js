import Vue from 'vue';
import Vuex from 'vuex'
// bootstrap 
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// store
import pedidos from './store'

//components
import content_pedidos from './components/content.vue'

Vue.use(Vuex);
Vue.use(BootstrapVue);

const storer = new Vuex.Store({
  modules: {pedidos}
})


new Vue({
    el: '#app',
    store: storer,
    render(h) { 
      return h(content_pedidos) 
    }
  })