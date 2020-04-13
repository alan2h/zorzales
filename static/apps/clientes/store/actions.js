
import axios from 'axios'

export const set_clientes = ({commit}) => {
    axios.get('/clientes/api/')
    .then((response) => {
        commit('set_clientes', response.data)
    })
    .catch((error) => {
        console.log(error);
    })
}

export const set_buscador = ({commit}, payload) => {
    axios.get('/clientes/api/?buscador=' + payload)
    .then((response) => {
        commit('set_clientes', response.data)
    })
    .catch((error) => {
        console.log(error);
    })
}