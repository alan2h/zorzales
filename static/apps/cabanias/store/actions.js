
import axios from 'axios';

export const set_cabanias = ({commit}) => {
    axios.get('/cabanias/api/')
    .then((response) => {
        commit('set_cabanias', response.data)
    })
    .catch((error) => {
        console.log(error);
    })
}

export const set_inventarios_cabania = ({commit}, payload) => {
    /*------
    obtiene todos los articulos 
    perteneciente a una cabania
    ------*/
    axios.get(`/cabanias/api/${payload}`)
    .then((response) => {
        commit('set_inventarios_cabania', response.data.inventario)
    })
    .catch((error) => {
        console.log(error);
    })
}