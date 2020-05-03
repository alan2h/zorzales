import Vue from 'vue';
import vuex from 'vuex';
//components
import App from './App.vue'

import cabanias from '@/apps/cabanias/store'
import reservas from '@/apps/reservas/store'

Vue.use(vuex)

const storer = new vuex.Store({
  modules: {cabanias, reservas}
})

new Vue({
    el: '#app',
    store:storer,
    render(h) { 
      return h(App) 
    }
  })