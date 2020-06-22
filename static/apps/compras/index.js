import Vue from 'vue';
//import vuex from 'vuex';
import VueRouter from 'vue-router';

// components App
import app from './App.vue';

// rutas
import {routes} from './router';

Vue.use(VueRouter);

const router = new VueRouter({
    routes
})

new Vue({
    el: '#app',
    router,
    render(h){
        return h(app)
    }
})