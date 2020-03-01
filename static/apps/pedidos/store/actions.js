
import axios from 'axios';

export const set_articulos = (context, url) => {
    axios.get(url)
    .then(function(response){
        context.commit('set_articulos', response.data.results);
        context.commit('set_pagina_siguiente', response.data.next);
        context.commit('set_pagina_atras', response.data.previous);
    })
}

export const set_pedidos_articulos = (context, articulo) => {
    context.commit('set_pedidos_articulos', articulo);
}

export const set_total = ({commit}, precio_compra) => {
    commit('set_total', precio_compra);
}