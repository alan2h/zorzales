
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