import axios from 'axios';

import {config} from '@/libs/globals_conf.js'

export const set_reservas = ({commit}, url='/reservas/api/') =>{
    axios.get(url)
    .then((response) => {
        commit('set_reservas', response.data.results);
        commit('set_pagina_siguiente_reservas', response.data.next);
        commit('set_pagina_atras_reservas', response.data.previous);
    })
    .catch((error) => {
        console.log(error.response)
    })
}


export const set_reserva = ({commit}, payload) => {
    commit('remove_errores');
    axios.post('/reservas/api/', payload, config)
    .then((response) => {
        console.log(response.data);
        commit('remove_errores');
        commit('set_message', 'success')
    })
    .catch((error) => {
        console.log(error.response.data)
        commit('set_errores', error.response.data)
    })
}

export const set_message = ({commit}, payload) => {
    commit('set_message', payload)
}