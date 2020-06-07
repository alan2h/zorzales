
export const set_cabanias = (state, payload) => {
    state.cabanias = payload;
}

export const set_inventarios_cabania = (state, payload) => {
    /*------
    mutations del estado de inventarios perteneciente a una cabania 
    -----*/
    state.inventarios = payload;
}