import Vue from 'vue'
import vuex from 'vuex'

import * as actions from './actions'
import * as mutations from './mutations'
import * as getters from './getters'


Vue.use(vuex);

const reservas = {
    state: {
        reservas: [],
        errores: [],
        message: '',
        pagina_siguiente_reservas: '',
        pagina_atras_reservas: '',
        reserva_result: []
    },
    actions,
    mutations,
    getters
}

export default reservas;