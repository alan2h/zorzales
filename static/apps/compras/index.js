import Vue from 'vue';
//import vuex from 'vuex';
import VueRouter from 'vue-router';

// bootstrap 
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

// components App
import app from './App.vue';

// rutas
import {routes} from './router';

Vue.use(VueRouter);
Vue.use(BootstrapVue);
Vue.use(VueSweetalert2);

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