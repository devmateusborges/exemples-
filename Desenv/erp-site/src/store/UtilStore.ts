import { createSlice, PayloadAction } from '@reduxjs/toolkit';

const util = createSlice({
  name: "util",

  initialState: {
    loading: false,
    contatoOrigin: 0,
    textloading: "",
  },
  reducers: {
    loading(state, action: PayloadAction<boolean>) {
      state.loading = action.payload;
    },
    contatoOrigin(state, action: PayloadAction<number>) {
      state.contatoOrigin = action.payload;
    },
    textloadingAction(state, action: PayloadAction<any>) {
      state.textloading = action.payload;
    },
  },
});

export const { loading, contatoOrigin, textloadingAction } = util.actions;

export default util.reducer;
