
import Vuex from 'vuex';
import Vue from 'vue';

import * as actions from './actions'
import * as mutations from './mutations'
import * as getters from './getters'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        articulos_pedidos: [],
        articulos: [],
        pagina_siguiente: '',
        pagina_atras: ''
    },
    actions,
    mutations,
    getters
})