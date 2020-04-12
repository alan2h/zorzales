
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