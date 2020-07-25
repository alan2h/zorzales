
import Vuex from 'vuex';
import Vue from 'vue';

import * as actions from './actions'
import * as mutations from './mutations'
import * as getters from './getters'

Vue.use(Vuex);

const pedidos = {
    state: {
        articulos_pedidos: [],
        articulos: [],
        pagina_siguiente: '',
        pagina_atras: '',
        total: 0.0,
        fecha: '',
        message: {status: '', text: ''}
    },
    actions,
    mutations,
    getters
}

export default pedidos;