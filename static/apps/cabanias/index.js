import Vue from 'vue';
import vuex from 'vuex';
//components
import App from './App.vue'

import cabanias from '@/apps/cabanias/store'

Vue.use(vuex)

const storer = new vuex.Store({
  modules: {cabanias}
})

new Vue({
    el: '#app',
    store:storer,
    render(h) { 
      return h(App) 
    }
  })