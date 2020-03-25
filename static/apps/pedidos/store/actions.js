
import axios from 'axios';
import {pad} from '../../../libs/functions.js'

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

export const delete_pedidos_articulos = ({commit}, index) => {
    commit('delete_pedidos_articulos', index)
}

export const delete_pedidos_articulos_all = ({commit}) => {
    commit('delete_pedidos_articulos_all')
}

export const set_message = ({commit}, payload) => {
    commit('set_message', payload);
}

export const set_fecha = ({commit}, fecha) => {
    let fecha_formato = fecha.getFullYear() + '-' + pad(fecha.getMonth() + 1) + '-' + pad(fecha.getDate())
    commit('set_fecha', fecha_formato)
}