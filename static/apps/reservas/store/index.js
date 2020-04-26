import Vue from 'vue'
import vuex from 'vuex'

import * as actions from './actions'
import * as mutations from './mutations'
import * as getters from './getters'

import cabanias from '@/apps/cabanias/store'
import clientes from '@/apps/clientes/store'

Vue.use(vuex);

const reservas = {
    state: {
        reservas: [],
        errores: [],
        message: ''
    },
    actions,
    mutations,
    getters,
    modules:{
        cabanias,
        clientes
    }
}

export default reservas;