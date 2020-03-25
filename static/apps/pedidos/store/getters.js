
export const get_articulos = (state) => { return state.articulos; }; //obtener lista de articulos
export const get_pagina_siguiente = (state) => { return state.pagina_siguiente; };
export const get_pagina_atras = (state) => { return state.pagina_atras; };
// obtener articulos pedidos para la compra
export const get_articulos_pedidos = (state) => { return state.articulos_pedidos; };
export const get_total = (state) => { return state.total; };

export const get_fecha = (state) => { return state.fecha; }; // obtener la fecha del pedido
export const get_message = (state) => { return state.message; }; // obtiene el mensaje del guardado