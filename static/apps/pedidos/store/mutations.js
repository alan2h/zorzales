
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