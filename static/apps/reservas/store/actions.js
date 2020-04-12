import axios from 'axios';

export const set_reservas = ({commit}) =>{
    axios.get('/reservas/api/')
    .then((response) => {
        commit('set_reservas', response.data);
    })
    .catch((error) => {
        console.log(error)
    })
}