
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