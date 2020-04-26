
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