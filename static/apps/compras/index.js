import Vue from 'vue';
import vuex from 'vuex';
import VueRouter from 'vue-router';

// components App
import app from './App.vue';

// store
import compras from './store'
import pedidos from '@/apps/pedidos/store'

// rutas
import {routes} from './router';

Vue.use(VueRouter);
Vue.use(vuex);

const router = new VueRouter({
    routes
})


const storer = new vuex.Store({
    modules: {compras, pedidos}
})


new Vue({
    el: '#app',
    router,
    store: storer,
    render(h){
        return h(app)
    }
})