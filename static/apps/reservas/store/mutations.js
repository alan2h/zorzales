
export const set_reservas = (state, payload) => {
    state.reservas = payload;
}

export const set_errores = (state, payload) => {
    state.errores.push(payload);
}

export const remove_errores = (state, payload) => {
    state.errores = [];
}

export const set_message = (state, payload ) => {
    state.message = payload;
}

export const set_pagina_siguiente_reservas = (state, payload) => {
    state.pagina_siguiente_reservas = payload;
}

export const set_pagina_atras_reservas = (state, payload) => {
    state.pagina_atras_reservas = payload;
}

export const set_reserva_result = (state, payload) => {
    state.reserva_result = payload;
}