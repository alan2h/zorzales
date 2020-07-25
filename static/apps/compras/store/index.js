import Vuex from 'vuex';
import Vue from 'vue';

import * as actions from './actions'
import * as mutations from './mutations'
import * as getters from './getters'

Vue.use(Vuex);

const compras = {
    state: {
        compras: []
    },
    actions,
    mutations,
    getters
}

export default compras;
