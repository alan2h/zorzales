
export const set_articulos = (state, payload) => {
    // carga de articulos para el listado de paginas
    state.articulos = payload;
}

export const set_pagina_siguiente = (state, payload) => {
    state.pagina_siguiente = payload;
}

export const set_pagina_atras = (state, payload) => {
    state.pagina_atras = payload;
}

export const set_pedidos_articulos = (state, payload) => {
    // cargar pedidos desde el form de articulos
    state.articulos_pedidos.push(payload); // agrego un articulo nuevo 
}

export const set_total = (state, payload) => {
    state.total += parseFloat(payload);
}

export const delete_pedidos_articulos = (state, payload) => {
    state.total -= state.articulos_pedidos[payload].total
    state.articulos_pedidos.splice(payload, 1);
}

export const delete_pedidos_articulos_all = (state) => {
    state.total = 0.0;
    state.articulos_pedidos = [];
}

export const set_fecha = (state, payload) => {
    state.fecha = payload;
}

export const set_message = (state, payload) => {
    state.message.status = payload.status;
    state.message.text = payload.text;
}